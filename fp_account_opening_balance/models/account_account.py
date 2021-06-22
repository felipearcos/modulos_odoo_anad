# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class AccountAccount(models.Model):
	_inherit = 'account.account'

	balance_w_opening = fields.Float(string='Saldo real (incl. saldo apertura)', compute='_compute_balance', store=False, help='Saldo total de esta cuenta, incluyendo el saldo de apertura')
	
	@api.multi
	def _compute_balance(self):
		for record in self:
			query = "SELECT COALESCE (SUM(l.debit),0) - COALESCE (SUM(l.credit), 0)" \
					"FROM account_move_line l WHERE l.account_id = " + str(record.id)
							
			self.env.cr.execute(query)
			bal_op = self.env.cr.fetchone()[0]
			record.balance_w_opening = bal_op




	