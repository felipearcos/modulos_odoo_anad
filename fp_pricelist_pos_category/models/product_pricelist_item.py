# -*- coding: utf-8 -*-
# Copyright (C) 2018 Felipe Arcos <felipe@florprohibida.com>

from openerp import models, fields

import logging
_logger = logging.getLogger(__name__)


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    pos_categ_id = fields.Many2one('pos.category', string='Categoría de TPV')

    

