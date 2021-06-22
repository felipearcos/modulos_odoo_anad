# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields

_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    supplier_date = fields.Date(string="Fecha factura proveedor")
