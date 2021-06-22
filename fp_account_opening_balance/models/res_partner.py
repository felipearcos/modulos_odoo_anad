# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
	_inherit = 'res.partner'

	opening_balance_customer = fields.Float(string='Saldo de apertura (Cliente)', compute='_compute_customer_opening', store=False, help=u"Saldo de apertura del cliente en el año en curso")
	opening_balance_supplier = fields.Float(string='Saldo de apertura (Proveedor)', compute='_compute_supplier_opening', store=False, help=u"Saldo de apertura del proveedor en el año en curso")

	@api.multi
	def _compute_customer_opening(self):
		for record in self:
			if record.customer:
				query = "SELECT SUM(l.debit-l.credit) " \
						"FROM account_move_line l " \
						"LEFT JOIN account_account a ON (a.id = l.account_id) " \
						"WHERE l.period_id = 82 AND l.partner_id = " + str(record.id) +\
						" AND a.type = 'receivable'"
								
				self.env.cr.execute(query)
				bal_partner = self.env.cr.fetchone()[0]
				record.opening_balance_customer = bal_partner
			else:
				record.opening_balance_customer = 0

	@api.multi
	def _compute_supplier_opening(self):
		for record in self:
			if record.supplier:
				query = "SELECT SUM(l.debit-l.credit) " \
						"FROM account_move_line l " \
						"LEFT JOIN account_account a ON (a.id = l.account_id) " \
						"WHERE l.period_id = 82 AND l.partner_id = " + str(record.id) +\
						" AND a.type = 'payable'"						
								
				self.env.cr.execute(query)
				bal_partner = self.env.cr.fetchone()[0]
				record.opening_balance_supplier = bal_partner

			else:
				record.opening_balance_supplier = 0
