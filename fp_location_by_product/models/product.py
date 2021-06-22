# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Almacenes
    ref_c = fields.Char(size=20, string="Ubicacion Campollano", track_visibility='onchange')
    ref_t = fields.Char(size=20, string="Ubicacion Torrellano", track_visibility='onchange')
    ref_cu = fields.Char(size=20, string="Ubicacion Elda", track_visibility='onchange')
    ref_m = fields.Char(size=20, string="Ubicacion Murcia", track_visibility='onchange')

    # Tiendas
    ref_tienda_alb = fields.Char(size=20, string="Ubicacion Albacete")
    ref_tienda_ali = fields.Char(size=20, string="Ubicacion Alicante")
    ref_tienda_cue = fields.Char(size=20, string="Ubicacion Cuenca")
    ref_tienda_tor = fields.Char(size=20, string="Ubicacion Torrevieja")
    ref_tienda_vil = fields.Char(size=20, string="Ubicacion Villarrobledo")

    # Cálculo de reabastecimientos
    tiene_reab_alb = fields.Boolean(string="Regla de reabastecimiento en Albacete", compute="_calculate_reab_alb", store=False)
    tiene_reab_ali = fields.Boolean(string="Regla de reabastecimiento en Alicante", compute="_calculate_reab_ali", store=False)
    tiene_reab_cue = fields.Boolean(string="Regla de reabastecimiento en Cuenca", compute="_calculate_reab_cue", store=False)
    tiene_reab_tor = fields.Boolean(string="Regla de reabastecimiento en Torrevieja", compute="_calculate_reab_tor", store=False)
    tiene_reab_vil = fields.Boolean(string="Regla de reabastecimiento en Villarrobledo", compute="_calculate_reab_vil", store=False)
    
    @api.multi
    def _calculate_reab_alb(self):
        for rec in self:
            orderpoint_obj = self.pool.get('stock.warehouse.orderpoint')
            ids = orderpoint_obj.search(self.env.cr, self.env.uid, ['&',('product_id', '=', rec.id),('location_id', '=', 24)], context=None)
            if ids:
                rec.tiene_reab_alb = True
            else:
                rec.tiene_reab_alb = False


    def _calculate_reab_ali(self):
        for rec in self:
            orderpoint_obj = self.pool.get('stock.warehouse.orderpoint')
            ids = orderpoint_obj.search(self.env.cr, self.env.uid, ['&',('product_id', '=', rec.id),('location_id', '=', 25)], context=None)
            if ids:
                rec.tiene_reab_ali = True
            else:
                rec.tiene_reab_ali = False

    def _calculate_reab_cue(self):
        for rec in self:
            orderpoint_obj = self.pool.get('stock.warehouse.orderpoint')
            ids = orderpoint_obj.search(self.env.cr, self.env.uid, ['&',('product_id', '=', rec.id),('location_id', '=', 26)], context=None)
            if ids:
                rec.tiene_reab_cue = True
            else:
                rec.tiene_reab_cue = False

    def _calculate_reab_tor(self):
        for rec in self:
            orderpoint_obj = self.pool.get('stock.warehouse.orderpoint')
            ids = orderpoint_obj.search(self.env.cr, self.env.uid, ['&',('product_id', '=', rec.id),('location_id', '=', 28)], context=None)
            if ids:
                rec.tiene_reab_tor = True
            else:
                rec.tiene_reab_tor = False

    def _calculate_reab_vil(self):
        for rec in self:
            orderpoint_obj = self.pool.get('stock.warehouse.orderpoint')
            ids = orderpoint_obj.search(self.env.cr, self.env.uid, ['&',('product_id', '=', rec.id),('location_id', '=', 27)], context=None)
            if ids:
                rec.tiene_reab_vil = True
            else:
                rec.tiene_reab_vil = False

