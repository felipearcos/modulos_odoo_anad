# -*- coding: utf-8 -*-
# Copyright (C) 2018 Felipe Arcos <felipe@florprohibida.com>

from openerp import models, fields, api

import logging, time
_logger = logging.getLogger(__name__)

class ProductPricelist(models.Model):
	_inherit = 'product.pricelist'

	@api.model
	def _price_rule_get_multi(self, pricelist, products_by_qty_by_partner):
		context = self.env.context.copy() or {}

		context = context or {}
		date = context.get('date') or time.strftime('%Y-%m-%d')
		date = date[0:10]

		products = map(lambda x: x[0], products_by_qty_by_partner)
		currency_obj = self.pool.get('res.currency')
		product_obj = self.pool.get('product.template')
		product_uom_obj = self.pool.get('product.uom')
		price_type_obj = self.pool.get('product.price.type')

		if not products:
			return {}

		version = False
		for v in pricelist.version_id:
			if ((v.date_start is False) or (v.date_start <= date)) and ((v.date_end is False) or (v.date_end >= date)):
				version = v
				break
		if not version:
			raise osv.except_osv(_('Warning!'), _("At least one pricelist has no active version !\nPlease create or activate one."))
		categ_ids = {}
		pos_categ_ids = {} #F
		for p in products:
			categ = p.categ_id
			while categ:
				categ_ids[categ.id] = True
				categ = categ.parent_id
			
			pos_categ = p.pos_categ_id #F
			while pos_categ:
				pos_categ_ids[pos_categ.id] = True
				pos_categ = pos_categ.parent_id
		
		categ_ids = categ_ids.keys()
		pos_categ_ids = pos_categ_ids.keys() #F

		is_product_template = products[0]._name == "product.template"
		if is_product_template:
			prod_tmpl_ids = [tmpl.id for tmpl in products]
			# all variants of all products
			prod_ids = [p.id for p in
						list(chain.from_iterable([t.product_variant_ids for t in products]))]
		else:
			prod_ids = [product.id for product in products]
			prod_tmpl_ids = [product.product_tmpl_id.id for product in products]

		# Load all rules
		cr = self.env.cr
		cr.execute(
			'SELECT i.id '
			'FROM product_pricelist_item AS i '
			'WHERE (product_tmpl_id IS NULL OR product_tmpl_id = any(%s)) '
				'AND (product_id IS NULL OR (product_id = any(%s))) '
				'AND ((categ_id IS NULL) OR (categ_id = any(%s))) '
				'AND ((pos_categ_id IS NULL) OR (pos_categ_id = any(%s)))'
				'AND (price_version_id = %s) '
			'ORDER BY sequence, min_quantity desc',
			(prod_tmpl_ids, prod_ids, categ_ids, pos_categ_ids, version.id)) #F
		
		uid = self.env.uid
		item_ids = [x[0] for x in cr.fetchall()]
		items = self.pool.get('product.pricelist.item').browse(cr, uid, item_ids, context=context)

		price_types = {}

		results = {}
		for product, qty, partner in products_by_qty_by_partner:
			results[product.id] = 0.0
			rule_id = False
			price = False

			qty_uom_id = context.get('uom') or product.uom_id.id
			price_uom_id = product.uom_id.id
			qty_in_product_uom = qty
			if qty_uom_id != product.uom_id.id:
				try:
					qty_in_product_uom = product_uom_obj._compute_qty(
						cr, uid, context['uom'], qty, product.uom_id.id or product.uos_id.id)
				except except_orm:
					# Ignored - incompatible UoM in context, use default product UoM
					pass

			for rule in items:
				if rule.min_quantity and qty_in_product_uom < rule.min_quantity:
					continue
				if is_product_template:
					if rule.product_tmpl_id and product.id != rule.product_tmpl_id.id:
						continue
					if rule.product_id and not (product.product_variant_count == 1 and product.product_variant_ids[0].id == rule.product_id.id):
						# product rule acceptable on template if has only one variant
						continue
				else:
					if rule.product_tmpl_id and product.product_tmpl_id.id != rule.product_tmpl_id.id:
						continue
					if rule.product_id and product.id != rule.product_id.id:
						continue

				if rule.categ_id:
					cat = product.categ_id
					while cat:
						if cat.id == rule.categ_id.id:
							break
						cat = cat.parent_id
					if not cat:
						continue

				if rule.pos_categ_id: #F
					pos_cat = product.pos_categ_id
					while pos_cat:
						if pos_cat.id == rule.pos_categ_id.id:
							break
						pos_cat = pos_cat.parent_id
					if not pos_cat:
						continue

				if rule.base == -1:
					if rule.base_pricelist_id:
						price_tmp = self._price_get_multi(
								rule.base_pricelist_id, [(product,
								qty, partner)], context=context)[product.id]
						ptype_src = rule.base_pricelist_id.currency_id.id
						price_uom_id = qty_uom_id
						price = currency_obj.compute(cr, uid,
								ptype_src, pricelist.currency_id.id,
								price_tmp, round=False,
								context=context)
				elif rule.base == -2:
					seller = False
					for seller_id in product.seller_ids:
						if (not partner) or (seller_id.name.id != partner):
							continue
						seller = seller_id
					if not seller:
						if pricelist.type == 'purchase':
							continue
						elif product.seller_ids:
							seller = product.seller_ids[0]
					if seller:
						qty_in_seller_uom = qty
						seller_uom = seller.product_uom.id
						if qty_uom_id != seller_uom:
							qty_in_seller_uom = product_uom_obj._compute_qty(cr, uid, qty_uom_id, qty, to_uom_id=seller_uom)
						price_uom_id = seller_uom
						for line in seller.pricelist_ids:
							if line.min_quantity <= qty_in_seller_uom:
								price = line.price

				else:
					if rule.base not in price_types:
						price_types[rule.base] = price_type_obj.browse(cr, uid, int(rule.base))
					price_type = price_types[rule.base]

					# price_get returns the price in the context UoM, i.e. qty_uom_id
					price_uom_id = qty_uom_id
					price = currency_obj.compute(
							cr, uid,
							price_type.currency_id.id, pricelist.currency_id.id,
							product_obj._price_get(cr, uid, [product], price_type.field, context=context)[product.id],
							round=False, context=context)

				if price is not False:
					price_limit = price
					price = price * (1.0+(rule.price_discount or 0.0))
					if rule.price_round:
						price = tools.float_round(price, precision_rounding=rule.price_round)

					convert_to_price_uom = (lambda price: product_uom_obj._compute_price(
												cr, uid, product.uom_id.id,
												price, price_uom_id))
					if rule.price_surcharge:
						price_surcharge = convert_to_price_uom(rule.price_surcharge)
						price += price_surcharge

					if rule.price_min_margin:
						price_min_margin = convert_to_price_uom(rule.price_min_margin)
						price = max(price, price_limit + price_min_margin)

					if rule.price_max_margin:
						price_max_margin = convert_to_price_uom(rule.price_max_margin)
						price = min(price, price_limit + price_max_margin)

					rule_id = rule.id
					break

			# Final price conversion to target UoM
			price = product_uom_obj._compute_price(cr, uid, price_uom_id, price, qty_uom_id)

			results[product.id] = (price, rule_id)
		return results
