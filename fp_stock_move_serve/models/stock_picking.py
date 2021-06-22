# -*- coding: utf-8 -*-
# © 2019 Felipe Arcos
# License AGPL-3.0 or later <http://www.gnu.org/licenses/agpl.html>.
import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	pagado = fields.Boolean(string="Pagado", default=True)