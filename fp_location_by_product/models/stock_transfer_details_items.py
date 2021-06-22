# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields

_logger = logging.getLogger(__name__)


class StockTransferDetailsItems(models.Model):
    _inherit = 'stock.transfer_details_items'

    sref_c = fields.Char(string='Ubicacion Campollano', related='product_id.ref_c')
    sref_t = fields.Char(string='Ubicacion Torrellano', related='product_id.ref_t')
    sref_cu = fields.Char(string='Ubicacion Elda', related='product_id.ref_cu')
    sref_m = fields.Char(string='Ubicacion Murcia', related='product_id.ref_m')
