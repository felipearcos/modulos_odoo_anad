# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
	_inherit = 'account.invoice'

	comprobacion = fields.Boolean(string="Comprobacion registro de pago", compute='comprobar_pagos')
	comprobacion_g = fields.Boolean(string="Validacion del pago", related="comprobacion", store=True)
	pago_parcial = fields.Boolean(string="Pago parcial", compute="tiene_pago_parcial", store=False)
	num_simplificada = fields.Char(string="Numero Simplificada", compute='_calcular_numero', store=True)

	# Cada vez que se valida un pago, comprueba si estan todos validados, si es asi valida el pago total 
	@api.one
	def comprobar_pagos(self):
		for pagos in self.payment_ids:
			if pagos.validacion:
				self.comprobacion = True
				self.calcular_comprobacion(True)
			else:
				self.comprobacion = False
				self.calcular_comprobacion(False)
				break

	@api.multi
	def calcular_comprobacion(self, comprob):
		for record in self:
			if record.state == 'paid':
				record.comprobacion_g = comprob
				record.write({'comprobacion_g': record.comprobacion_g})
			else:
				record.comprobacion = False
				record.comprobacion_g = False
				record.write({'comprobacion_g': False})

	@api.multi
	def calculo_manual_comprobaciones(self):
		for record in self:
			if record.comprobacion:
				record.comprobacion_g = True



	# Comprueba si una factura en estado ABIERTO está simplemente abierta o pagada parcial 
	@api.depends('payment_ids')
	def tiene_pago_parcial(self):
		for record in self:
			if record.state == 'open':
				total_pagado = 0
				if record.payment_ids:
					for pago in record.payment_ids:
						total_pagado = total_pagado + float(pago.credit)

					if record.amount_total == total_pagado:
						record.pago_parcial = False
					else:
						record.pago_parcial = True
				else:
					record.tiene_pago_parcial = False
			else:
				record.tiene_pago_parcial = False

	@api.depends('number')
	def _calcular_numero(self):
		for record in self:
			if 'SIMPLIFICADA' in str(record.number):
				if 'SIMPLIFICADA-' in str(record.number):
					num_s = str(record.number).split("-")[2]
				else:
					num_s = str(record.number).split("-")[1]
				num_s = str(num_s)
				if len(num_s) == 1:
					record.num_simplificada = '0000' + num_s
				elif len(num_s) == 2:
					record.num_simplificada = '000' + num_s
				elif len(num_s) == 3:
					record.num_simplificada = '00' + num_s
				elif len(num_s) == 4:
					record.num_simplificada = '0' + num_s
				else:
					record.num_simplificada = num_s


