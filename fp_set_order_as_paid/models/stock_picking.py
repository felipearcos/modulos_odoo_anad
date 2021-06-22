# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	payment_info = fields.Selection([ ('not_paid', 'No pagado'),('partial_paid', 'Parcialmente pagado'),('paid', 'Pagado')], related="sale_id.payment_info")