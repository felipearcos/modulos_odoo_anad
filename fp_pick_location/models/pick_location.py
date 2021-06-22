# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class PickLocation(models.Model):
	_name="pick.location"

	name = fields.Char(string='Código de ubicación')
	available = fields.Boolean(string='Ubicación libre')
	pick_id = fields.Many2one('stock.picking', string='Albarán relacionado', readonly=True)



	