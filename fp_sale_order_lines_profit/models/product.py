# -*- coding: utf-8 -*-
# 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import api, models, fields
import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Método que calcula el precio de coste de todos los productos que sean Listas de Materiales a partir de sus componentes
    def compute_cost_of_bom(self, cr, uid, context=None):
        
        # Objeto product.template
        product_obj = self.pool.get('product.template')

        # Todos los productos
        product_ids = product_obj.search(cr, uid, [])
        for rec in product_obj.browse(cr, uid, product_ids, context=None):          
            # Comprueba que sea una lista de materiales
            
            if rec.bom_count:
                # Consulta todas sus listas de materiales


                for ldm in rec.bom_ids:
                    ldm_cost = 0
                    if ldm.type == 'phantom':
                        # Extrae todos los componentes de la lista de materiales
                        for component in ldm.bom_line_ids:
                            # Y el producto, cantidades y precios de cada componente
                            product = component.product_id
                            # El coste de esta línea será el coste del producto por la cantidad de productos que forman el kit
                            line_cost = product.standard_price * component.product_qty
                            ldm_cost = ldm_cost + line_cost
                        rec.write({'standard_price':ldm_cost})
                            
                        
