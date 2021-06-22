# -*- coding: utf-8 -*-
# © 2019 Felipe Arcos
# License AGPL-3.0 or later <http://www.gnu.org/licenses/agpl.html>.
import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)

class StockMove(models.Model):
	_inherit = 'stock.move'

	a_servir = fields.Boolean(string="Producto a servir")
	cantidad_servida = fields.Integer(string="Cantidad servida")
	picking_pagado = fields.Boolean(related='picking_id.pagado', string="Albarán pagado")