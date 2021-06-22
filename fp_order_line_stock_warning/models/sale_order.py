# -*- coding: utf-8 -*-
# 2020 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'
	
	def product_id_change_with_wh(self, cr, uid, ids, pricelist, product, qty=0, uom=False, qty_uos=0, uos=False, name='', partner_id=False,lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, warehouse_id=False, context=None,location_id=False):
		context = context or {}
		product_uom_obj = self.pool.get('product.uom')
		product_obj = self.pool.get('product.product')
		stringLocation = ''

		product_id = product_obj.browse(cr, uid, [product], context=context)

		warning_msgs = ''

		warning = {}
		
		res = super(SaleOrderLine,self).product_id_change(cr, uid, ids, pricelist, product, qty=qty, uom=False, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, fiscal_position=fiscal_position, flag=flag, context=context)
	
		if product:
			if warehouse_id == 1: # CAMPOLLANO
				#if not context['location_id']:
				location = 12
				stringLocation = 'Almacen Central'

				context=dict(context)
				context.update({'location_id': location})
				context.update({'location': location})

				availability = self.pool.get('product.product')._product_available(cr,uid,[product],context=context)

			if warehouse_id == 2: # TORRELLANO
				location = 19
				stringLocation = 'Almacen Torrellano'

				context=dict(context)
				context.update({'location_id': location})
				context.update({'location': location})

				availability = self.pool.get('product.product')._product_available(cr,uid,[product],context=context)
			
			if warehouse_id == 7: # ELDA
				location = 6572
				stringLocation = 'Almacen Elda'

				context=dict(context)
				context.update({'location_id': location})
				context.update({'location': location})

				availability = self.pool.get('product.product')._product_available(cr,uid,[product],context=context)

			if warehouse_id == 8: # MURCIA
				location = 6579
				stringLocation = 'Almacen Murcia'

				context=dict(context)
				context.update({'location_id': location})
				context.update({'location': location})

				availability = self.pool.get('product.product')._product_available(cr,uid,[product],context=context)

			if qty>availability[product]['qty_available']:
				warn_msg = 'Se quieren vender %.0f unidad(es) pero solo hay disponibles %.0f unidad(es).\n El stock total del almacen es %.0f unidad(es), sin contar las unidades reservadas' % \
				(qty, max(0,availability[product]['virtual_available']), max(0,availability[product]['qty_available']))

				warning_msgs += warn_msg
		
			if warning_msgs:
				warning = {
							'title': '¡Stock insuficiente en %s!' % stringLocation,
							'message' : warning_msgs
						}
			res.update({'warning': warning})
			return res


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	@api.multi
	def calculate_stock(self, context=None):
		self.ensure_one()
		for rec in self:
			stringStock = ''
			
			if context['warehouse_id'] == 1: # CAMPOLLANO
				location = 12
					
			if context['warehouse_id'] == 2: # TORRELLANO
				location = 19
				
			if context['warehouse_id'] == 7: # ELDA
				location = 6572
				

			if context['warehouse_id'] == 8: # MURCIA
				location = 6579

			for line in rec.order_line:

				if location:
					cantidad = self.return_qty_by_product(location,line.product_id,context)

					if cantidad >= line.product_uom_qty:
						stringQty = ': Hay disponibilidad de las '+ str(int(line.product_uom_qty))+ ' ud. que se quieren vender'
					elif cantidad > 0:
						stringQty = ': Solo hay disponibles '+str(int(cantidad))+ ' ud. en este almacen'
					else:
						stringQty = ': No hay disponibilidad de este producto en este almacen'

					# CALCULAR STOCK DE CADA UNO DE LOS PRODUCTOS
					stringStock += '['+line.product_id.default_code+'] '
					stringStock += line.product_id.name
					stringStock += stringQty
					stringStock += '\n\n'
				else:
					stringStock = 'No se ha podido recuperar la informacion'

		view_id = self.env['calculate.stock.wizard']
		params = {'stringStock': stringStock}
		#new = view_id.create(params[0])
		new = view_id.create(params)

		return {
			'type': 'ir.actions.act_window',
			'name': 'Calculo de stock',
			'res_model': 'calculate.stock.wizard',
			'view_type': 'form',
			'view_mode': 'form',
			'res_id'    : new.id,
			'view_id': self.env.ref('fp_order_line_stock_warning.fp_wizard_stock_calculation',False).id,
			'target': 'new',
		}

	def return_qty_by_product(self, location, product, context=None):
		
		if product:
			if location:
				context=dict(context)
				context.update({'location_id': location})
				context.update({'location': location})

				availability = self.pool.get('product.product')._product_available(self.env.cr, self.env.uid, [product.id],context=context)

				return availability[product.id]['virtual_available']		
