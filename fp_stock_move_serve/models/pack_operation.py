# -*- coding: utf-8 -*-
# © 2019 Felipe Arcos
# License AGPL-3.0 or later <http://www.gnu.org/licenses/agpl.html>.
import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)

class StockPackOperation(models.Model):
	_inherit = 'stock.pack.operation'

	a_servir = fields.Boolean(related='linked_move_operation_ids.move_id.a_servir', string="Producto a servir")
	cantidad_servida = fields.Integer(related='linked_move_operation_ids.move_id.cantidad_servida',string="Cantidad servida")
	picking_pagado = fields.Boolean(related='picking_id.pagado', string="Albarán pagado")