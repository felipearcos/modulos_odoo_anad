# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields, netsvc

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	pick_location_id = fields.Many2one('pick.location', string="Ubicación de pick", copy=True)

	''' Sobreescribe el método do_transfer para que cuando se transfiera el albarán OUT
		, y quitar la ubicación de pick a este y a los relacionados '''
	@api.multi
	def do_transfer(self):
		res = super(StockPicking, self).do_transfer()
		for rec in self:
			if rec.picking_type_code == 'outgoing':
				if rec.sale_id:
					sale = rec.sale_id
					if sale.picking_ids:
						all_done = all([x.state == 'done' for x in sale.picking_ids])
						if all_done == True:
							for picking in sale.picking_ids:
								picking.update({'pick_location_id': False})
		return res
