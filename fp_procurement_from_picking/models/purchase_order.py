# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
	_inherit = 'purchase.order.line'
	# No es el mismo destino_producto que el de base en compras
	# No se puede calcular porque puede tener varios destinos así que se calcula y se concatena
	#destino_producto_move = fields.Char(string='Destino producto move', related="procurement_ids.destino_producto")
	destino_producto_mv = fields.Char(string='Destino producto', compute="concatenar_destino")

	# Concatena los destinos desde sus abastecimientos(movimientos) relacionados
	def concatenar_destino(self):
		for rec in self:
			destino_temp= ''
			# Si no viene de abastecimiento, se pone por defecto "Almacén"
			if not rec.procurement_ids:
				rec.update({'destino_producto_mv': "PEDIDO" })
			else:
				for proc in rec.procurement_ids:
					destino_producto_actual = proc.destino_producto
					if destino_producto_actual:
						if destino_temp == '':
							destino_temp = destino_producto_actual
						else:
							destino_temp = destino_temp + " - " + destino_producto_actual
						rec.update({'destino_producto_mv': destino_temp })
