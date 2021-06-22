# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.osv import fields,osv
from openerp import api
from openerp.tools.translate import _

class fp_message(osv.osv_memory):
	_name = "fp.message"
	_columns={
		'text': fields.text(),
	}
	
	@api.one
	def aceptar(self):
		pass