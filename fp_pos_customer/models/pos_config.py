# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models,fields,api,osv
from openerp.osv.orm import except_orm
from openerp.exceptions import except_orm, Warning, RedirectWarning

_logger = logging.getLogger(__name__)

class PosConfig(models.Model):
	_inherit= ['pos.config']

	cliente_defecto = fields.Many2one('res.partner', string='Cliente por defecto')