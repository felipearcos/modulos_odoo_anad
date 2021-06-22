# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields, api, _

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    check_double = fields.Boolean(string="Doble ubicacion Central", default=False)
    text_double = fields.Char(string="Doble ubicacion Central (Texto)")
    check_expo = fields.Boolean(string="Exposición", compute="_calculate_expo")
    check_vp = fields.Boolean(string="Venta prioritaria Central", default=False)

    check_double_tr = fields.Boolean(string="Doble ubicacion Torrellano", default=False)
    text_double_tr = fields.Char(string="Doble ubicacion Torrellano (texto)")
    check_vp_tr = fields.Boolean(string="Venta prioritaria Torrellano", default=False)

    check_double_el = fields.Boolean(string="Doble ubicacion Elda", default=False)
    text_double_el = fields.Char(string="Doble ubicacion Elda (texto)")
    check_vp_el = fields.Boolean(string="Venta prioritaria Elda", default=False)

    check_double_mu = fields.Boolean(string="Doble ubicacion Murcia", default=False)
    text_double_mu = fields.Char(string="Doble ubicacion Murcia (texto)")
    check_vp_mu = fields.Boolean(string="Venta prioritaria Murcia", default=False)

    @api.multi
    def _calculate_expo(self):
    	for rec in self:
            if rec.ref_c:
    		    if "ALC/EXPO" in rec.ref_c:
    			    rec.check_expo = True
    		    else:
    			    rec.check_expo = False
   

