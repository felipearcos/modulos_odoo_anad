# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos
# License AGPL-3.0 or later <http://www.gnu.org/licenses/agpl.html>.
from openerp import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Creación de un campo enlazado con la referencia del pedido
    client_order_ref = fields.Char(string='Ref. de pedido', related="sale_id.client_order_ref")
