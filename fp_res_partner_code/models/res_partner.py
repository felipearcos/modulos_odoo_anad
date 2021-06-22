# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
	_inherit = 'res.partner'

	partner_codes = fields.One2many('partner.code','partner_id',string='Códigos de cliente')

	@api.model
	def name_search(self, name, args=None, operator='ilike', limit=100):
		args = args or []
		recs = self.search([('partner_codes', '=', name)] + args, limit=limit)

		if not recs.ids:
			return super(ResPartner, self).name_search(name=name, args=args, operator=operator,limit=limit)
		return recs.name_get()