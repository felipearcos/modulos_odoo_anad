# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields
import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	profit_percentage = fields.Float(string="Rentabilidad (%)", compute="_compute_profit_by_line", store=False, digits_compute=dp.get_precision('Account'))
	#profit_color = fields.Binary(string='Color', attachment=False)
	profit_color_char = fields.Char(string="Rentabilidad", compute="_compute_profit_color")
	
	@api.depends('product_id', 'price_unit')
	def _compute_profit_by_line(self):
		return 0
		
	@api.depends('profit_percentage')
	def _compute_profit_color(self):
		return

class SaleOrder(models.Model):
	_inherit = 'sale.order'
	
	profit_percentage = fields.Float(string="Rentabilidad pedido", compute="_compute_profit_by_order", store=False)
	#profit_color = fields.Selection([ ('red', 'Baja'),('yellow', 'Normal'),('green', 'Alta')],'Rentabilidad', default='red', compute="_compute_profit_color")
	profit_color_char = fields.Char(string="Rentabilidad", compute="_compute_profit_color")

	@api.depends('order_line.profit_percentage', 'order_line.product_uom_qty')
	def _compute_profit_by_order(self):
		return 0

	@api.depends('profit_percentage')
	def _compute_profit_color(self):
		return '1'