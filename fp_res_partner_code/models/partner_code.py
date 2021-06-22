# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class PartnerCode(models.Model):
	_name = 'partner.code'

	name = fields.Char(string='Código')
	active = fields.Boolean(string='Activo', default=True)
	partner_id = fields.Many2one('res.partner', string='Cliente relacionado')

	@api.multi
	def deactivate(self):
		for rec in self:
			rec.active = False
			rec.partner_id = False
		return True




