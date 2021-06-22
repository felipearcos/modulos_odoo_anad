# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class StockMove(models.Model):
	_inherit = 'stock.move'

	destino_producto = fields.Char(string='Destino producto', related="purchase_line_id.destino_producto")


