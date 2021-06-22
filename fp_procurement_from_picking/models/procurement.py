# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class ProcurementOrder(models.Model):
	_inherit = 'procurement.order'

	supplier = fields.Many2one("res.partner", string="Proveedor del abastecimiento", readonly=True)
	destino_producto = fields.Char(string="Destino del producto")

class MakeProcurement(models.Model):
	_inherit = 'make.procurement'

	supplier = fields.Many2one("res.partner", string="Proveedor del abastecimiento")
	destino_producto = fields.Char(string="Destino del producto")

	def default_get(self, cr, uid, fields, context=None):
		''' To get default values for the object.
		@param self: The object pointer.
		@param cr: A database cursor
		@param uid: ID of the user currently logged in
		@param fields: List of fields for which we want default values
		@param context: A standard dictionary
		@return: A dictionary which of fields with values.
		'''
		if context is None:
			context = {}
		record_id = context.get('active_id')
		# context.get('product_id') no se actualiza, hay que extraerlo del stock.move
		# Para ello buscamos el producto asociado a ese stock.move y lo usamos en vez del recuperado por contexto
		move = self.pool.get('stock.move')
		move_ids = move.search(cr, uid, [('id', '=', record_id)], context=context)
		real_product = move.browse(cr, uid, move_ids, context=context).product_id
		# fin

		# Si viene de stock.move rellena los campos de una forma, si no los rellena por defecto
		if context.get('active_model') == 'stock.move':
			product_ids = self.pool.get('product.product').search(cr, uid, [('id', '=', context.get('product_id'))], context=context)

			if len(product_ids) == 1:
				record_id = product_ids[0]

			res = super(MakeProcurement, self).default_get(cr, uid, fields, context=context)

			if record_id and 'product_id' in fields:
				proxy = self.pool.get('product.product')
				product_ids = proxy.search(cr, uid, [('id', '=', record_id)], context=context, limit=1)
				if product_ids:
					product_id = product_ids[0]
					product = self.pool.get('product.product').browse(cr, uid, product_id, context=context)
					# Establece los campos por defecto
		
					res['product_id'] = real_product.id
					res['supplier'] = real_product.seller_id.id
					res['uom_id'] = product.uom_id.id
					res['location_id'] = context.get('custom_location_id')

					# Novedad 14-05-19 Recuperar cantidad y ponerla en el make.procurement
					move = self.pool.get('stock.move')
					move_ids = move.search(cr, uid, [('id', '=', context.get('active_ids')[0])], context=context, limit=1)
					for rec in move.browse(cr, uid, move_ids, context=context):
						res['qty'] = rec.product_uom_qty

					# Pone procurement_done a True en el movimiento para desactivar el botón y que no se pueda volver a pedir
					picking = self.pool.get('stock.picking')
					picking_ids = picking.search(cr, uid, [('move_lines', 'in', context.get('active_ids')[0])], context=context, limit=1)
					for rec in picking.browse(cr, uid, picking_ids, context=context):
						# Pasa el campo "destino_producto" por contexto
						res['destino_producto'] = rec.pick_location_id.name
					

			if 'warehouse_id' in fields:
				warehouse_id = self.pool.get('stock.warehouse').search(cr, uid, [], context=context)
				res['warehouse_id'] = warehouse_id[0] if warehouse_id else False

			return res
		else:
			res = super(MakeProcurement, self).default_get(cr, uid, fields, context=context)
			return res
