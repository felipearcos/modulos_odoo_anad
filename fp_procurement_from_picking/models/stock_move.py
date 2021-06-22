# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class StockMove(models.Model):
	_inherit = 'stock.move'
	
	procurement_done = fields.Boolean(string="Abastecimiento creado")
	procurement_issue = fields.Boolean(string="Incidencia de abastecimiento")
	destino_producto_mv = fields.Char(string='Destino producto', related="purchase_line_id.destino_producto_mv")

	@api.multi
	def set_issue(self):
		# Marca la línea como incidencia (no se puede pedir)
		for rec in self:
			rec.update({'procurement_issue': True,
				    'procurement_done': False})

	@api.multi
	def set_done(self):
		# Marca la línea como pedida
		for rec in self:
			rec.update({'procurement_done': True,
				    'procurement_issue': False})
