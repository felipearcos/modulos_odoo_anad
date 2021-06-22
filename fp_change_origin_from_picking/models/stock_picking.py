# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields, _

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	# Actualización 30-04-19 para añadir campo preparation_user y método update_user
	preparation_user = fields.Many2one("res.users", string="Usuario que lo prepara")

	def update_user(self, cr, uid, picking_id, user, context=None):
		# Busca la ID del usuario a partir de su EAN13
		user_obj = self.pool.get('res.users')
		ids = user_obj.search(cr, uid, [('ean13', '=',  user)], context=context)
		for rec in user_obj.browse(cr, uid, ids, context=context):
			# Escribe el usuario en el albarán
			self.write(cr, uid, picking_id, {
				'preparation_user': rec.id
				}, context=context)

	def update_origin(self, cr, uid, picking_id, new_origin, context=None):
		self.write(cr, uid, picking_id, {
			 'origin': new_origin,
			 }, context=context)

	def update_pick(self, cr, uid, picking_id, pick_location, context=None):
		# Busca la ID del pick location a partir de su referencia
		pick_obj = self.pool.get('pick.location')
		#picks = pick_obj.browse(cr, uid, uid, context=context)
		ids = pick_obj.search(cr, uid, [('name', '=', pick_location)], context=context)
		for rec in pick_obj.browse(cr, uid, ids, context=context):
			# Escribe el pick en el albarán
			self.write(cr, uid, picking_id, {
				'pick_location_id': rec.id,
				}, context=context)
			# Cambia el pick_location a no disponible (V3)
			rec.write({'available': False})

			# Actualiza también el OUT asociado.
			picking_obj = self.pool.get('stock.picking')
			for recp in picking_obj.browse(cr,uid,picking_id, context=context):
				# Comprueba cuantos albaranes hay con el mismo sale_id (para ponerles a todos el mismo pick_location)
				if recp.group_id:
					picking_ids = picking_obj.search(cr, uid, [('group_id', '=', recp.group_id.id)], context=context)
					for picking_grouped in picking_ids:
						self.write(cr, uid, picking_grouped, {
						'pick_location_id': rec.id,
						}, context=context)

	''' Método que es llamado cuando se pulsa el botón "Transferir todo" '''
	def transfer_picking(self, cr, uid, picking_id, context=None):
		# Transfiere el albarán
		self.do_transfer(cr, uid, [picking_id], context=context)

		# Quita la ubicación de pick en todos los albaranes relacionados

	'''20-05-19 - Transfiere el propio albarán y TODOS los albaranes con el mismo grupo
	   de abastecimiento desde la interfaz de código de barras
	'''
	def transfer_all(self, cr, uid, picking_id, context=None):
		# Crea una instancia del objeto stock.picking
		picking_obj = self.pool.get('stock.picking')
		# Itera por todos los pickings encontrados con la ID pasada como parametro
		for recp in picking_obj.browse(cr,uid,picking_id,context=context):
			# Comprueba cuantos albaranes hay compartiendo grupo de abastecimiento y en disposicion de transferir
			picking_ids = picking_obj.search(cr, uid, ['&',('state', 'not in', ('done','draft','cancel')),('group_id', '=', recp.group_id.id),('group_id','!=',False)], context=context)
			# Itera cada albarán, transfiriendolo
			for picking in picking_ids:
				picking_obj.force_assign(cr,uid,picking,context=context)
				picking_obj.do_transfer(cr,uid,picking,context=context)
				picking_obj.message_post(cr, uid, picking, body=_("Albarán transferido junto a todos sus albaranes relacionados desde la interfaz de código de barras"), context=context)

