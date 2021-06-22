# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    validacion = fields.Boolean(string="Pago validado")

    # Lo llama el botón cada vez que se valida un pago
    @api.multi
    def validar(self):
    	for pago in self:
    		pago.validacion = True
    		self.env['account.invoice'].comprobar_pagos()

    		
