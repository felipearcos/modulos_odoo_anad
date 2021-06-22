# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
	_inherit = 'purchase.order.line'

	destino_producto = fields.Char(string='Destino producto')


