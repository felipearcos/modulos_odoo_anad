# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos (<felipe@florprohibida.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _


class IrSequence(models.Model):

    _inherit = 'ir.sequence'

    name = fields.Char(size=128)
