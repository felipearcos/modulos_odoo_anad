# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	shipped_new = fields.Boolean(string="Entregado", compute="_calculate_shipped_new")

	@api.multi
	def _calculate_shipped_new(self):
		for rec in self:
			if rec.picking_ids:
				if all([x.state == 'done' for x in rec.picking_ids]):
					rec.shipped_new = True
				else:
					rec.shipped_new = False
			else:
				rec.shipped_new = False

	


