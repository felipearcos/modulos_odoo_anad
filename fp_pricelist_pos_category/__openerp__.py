# coding: utf-8
# © 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Regla de tarifa basada en Categoría de TPV',
    'description': 'Incluye la categoría de TPV como elemento a elegir en las reglas para el cálculo de las tarifas' ,
    'version': '8.0.1',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'point_of_sale'
    ],
    'data': [
        'views/product_pricelist_item.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
