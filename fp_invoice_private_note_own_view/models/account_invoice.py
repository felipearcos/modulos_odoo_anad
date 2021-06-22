# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
	_inherit = 'account.invoice'

	private_note = fields.Text(string="Observaciones de la factura")
	shipped = fields.Boolean(string="Entregado", compute="_calculate_shipped_from_order")

	@api.multi
	def _calculate_shipped_from_order(self):
		for rec in self:
			for sale in rec.sale_ids:
				rec.shipped = sale.shipped_new