# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	label_price = fields.Float(string="Precio tachado")




