# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos (<felipe@florprohibida.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import models, api

class UpdateValidation(models.TransientModel):

    _name = 'update.validation'

    '''
    Actualiza la validacion de las facturas una primera vez
    '''
    @api.multi
    def update_validation(self):
        invoices = self.env['account.invoice'].browse(
            self.env.context.get('active_ids', []))
        invoices.calculo_manual_comprobaciones()
        return {'type': 'ir.actions.act_window_close'}
