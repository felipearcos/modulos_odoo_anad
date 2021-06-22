# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	tiene_ubicacion_almacen = fields.Boolean(string="Ubicacion almacen", compute="_calculo_ubicacion")

	@api.depends('product_id', 'order_id.state')
	def _calculo_ubicacion(self):
		for rec in self:
			# Primero extrae el almacén de la venta
			ubicacion = None

			id_almacen = rec.order_id.warehouse_id.id
			''' Almacenes:
			1 - Central
			2 - Torrellano
			7 - Elda
			8 - Murcia
			'''
			if id_almacen == 1:
				ubicacion = rec.product_id.ref_c
				if ubicacion:
					if 'ALC' in ubicacion:
						rec.tiene_ubicacion_almacen = True
				
			elif id_almacen == 2:
				ubicacion = rec.product_id.ref_t
				if ubicacion:
					if 'ALT' in ubicacion:
						rec.tiene_ubicacion_almacen = True
				
			elif id_almacen == 7:
				ubicacion = rec.product_id.ref_cu
				if ubicacion:
					if 'ALE' in ubicacion:
						rec.tiene_ubicacion_almacen = True
				
			elif id_almacen == 8:
				ubicacion = rec.product_id.ref_m
				if ubicacion:
					if 'ALM' in ubicacion:
						rec.tiene_ubicacion_almacen = True
				
			else:
				rec.tiene_ubicacion_almacen = False

class SaleOrder(models.Model):
	_inherit = 'sale.order'
	suma_verdes = fields.Float(string="Total productos con ubicacion", compute="_calculo_total_ubicacion", store=True, default=False)
	suma_rojos = fields.Float(string="Total productos sin ubicacion", compute="_calculo_total_sin", store=True, default=False)

	@api.depends('order_line','order_line.price_subtotal')
	def _calculo_total_ubicacion(self):
		for rec in self:
			suma_verdes = 0.0
			for line in rec.order_line:
				if line.tiene_ubicacion_almacen == True:
					suma_verdes = suma_verdes + (line.price_subtotal)

			rec.suma_verdes = suma_verdes * 1.21

	@api.depends('order_line','order_line.price_subtotal')
	def _calculo_total_sin(self):
		for rec in self:
			suma_rojos = 0.0
			for line in rec.order_line:
				if line.tiene_ubicacion_almacen == False:
					suma_rojos	= suma_rojos + (line.price_subtotal)
			rec.suma_rojos = suma_rojos * 1.21