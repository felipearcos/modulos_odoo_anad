# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos (<felipe@florprohibida.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import models, api


class UpdateProductCode(models.TransientModel):

    _name = 'update.product.code'

    '''
    Actualiza las referencias elegidas de forma masiva, llamando al metodo correspondiente
    '''
    @api.multi
    def update_code(self):
        products = self.env['product.template'].browse(
            self.env.context.get('active_ids', []))
        products.update_sequence()
        return {'type': 'ir.actions.act_window_close'}
