# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	external_barcode = fields.Char(string='Código de barras externo')

	def _generar_ean13_desde_ref(self, values):
		ref = values.get('default_code', False)
		ean13 = '0000000000000'

		# Monta el EAN13 con un prefijo, la referencia y el dígito de control
		if ref:
			if len(ref) == 6:
				ean13_nodc = '200000'+ref
				ean13_dc = str((10 - sum((3, 1)[i % 2] * int(n) for i, n in enumerate(reversed(ean13_nodc)))) % 10)
				ean13 = ean13_nodc + ean13_dc
		values.update({
					'ean13': ean13, })
		return values

	@api.model
	def create(self, values):
		if not values.get('ean13', False):
			values = self._generar_ean13_desde_ref(values)
		product = super(ProductTemplate, self).create(values)
		return product


class ProductProduct(models.Model):
	_inherit = 'product.product'

	external_barcode = fields.Char(string='Código de barras externo', related='product_tmpl_id.external_barcode')
