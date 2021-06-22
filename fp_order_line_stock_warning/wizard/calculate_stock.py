# -*- coding: utf-8 -*-
# 2020 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class CalculateStockWizard(models.TransientModel):
    _name = 'calculate.stock.wizard'
    stringStock = fields.Text('Mensaje', readonly=1)
    
