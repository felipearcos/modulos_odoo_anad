# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models,fields,api, osv
from openerp.osv.orm import except_orm
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _


_logger = logging.getLogger(__name__)

class PosSession(models.Model):
	_inherit= ['pos.session']

	num_tickets = fields.Integer(string="Numero de tickets de tarjeta")
	suma_tarjeta = fields.Float(string="Suma total de los tickets")
	tarjeta_contada = fields.Boolean(string="Tarjeta contada", default=False)

	@api.multi
	def aviso(self):
		texto = " "
		self.tarjeta_contada = True		
		if self.num_tickets > 1:
			texto = "Ha especificado que hay un total de " + str(self.num_tickets) + " tickets de tarjeta en esta sesión de TPV, que hacen un total de " + str(self.suma_tarjeta) +" EUR. Si es correcto, vuelva a pulsar el boton de Fin de Sesion. En caso contrario rellene el numero de tickets de tarjeta y su suma antes de finalizar la sesion." 
		else:
			texto = "Ha especificado que no ha habido pagos con tarjeta para esta sesion. Si es correcto, vuelva a pulsar el boton de Fin de Sesion. En caso contrario rellene el numero de tickets de tarjeta y su suma antes de finalizar la sesion."
		
		value=self.env['fp.message'].sudo().create({'text':texto})
		return{
		'type':'ir.actions.act_window',
		'name':'Informacion',
		'res_model':'fp.message',
		'view_type':'form',
		'view_mode':'form',
		'target':'new',
		# 'context':{'thesis_obj':self.id,'flag':'course Work completed'},
		'res_id':value.id                
       }