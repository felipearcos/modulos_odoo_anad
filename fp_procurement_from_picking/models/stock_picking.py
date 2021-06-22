# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	procurement_done = fields.Boolean(string="Abastecimiento creado", compute="check_done")
	procurement_issue = fields.Boolean(string="Incidencia de abastecimiento", compute="check_issue")

	@api.multi
	def check_done(self):
		# Comprueba si todos los stock.move del albarán tienen el abastecimiento hecho
		# , si es así lo marca como hecho también.
		for rec in self:
			proc_done = all([x.procurement_done == True for x in rec.move_lines])
			if proc_done == True:
				rec.update({'procurement_done': True })


	def check_issue(self):
		# Comprueba si alguno de sus movimientos tiene incidencia, no se puede pedir,
		# y marca el albarán como incidencia de abastecimiento
		for rec in self:
			proc_success = all([x.procurement_issue == False for x in rec.move_lines])
			# Si hay alguno con incidencia, marca la incidencia a verdadero
			if not proc_success:
				rec.update({'procurement_issue': True})