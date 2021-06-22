# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	payment_info = fields.Selection([ ('not_paid', 'No pagado'),('partial_paid', 'Parcialmente pagado (+ del 70%)'),('paid', 'Pagado')],'Informacion de pago', default='not_paid', track_visibility='onchange')





