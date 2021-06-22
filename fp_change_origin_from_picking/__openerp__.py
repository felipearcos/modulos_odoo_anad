# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Cambio de origen desde interfaz de código de barras y check de Entregado corregido',
    'description': 'Recopilación de métodos para actualización asíncrona desde la interfaz de código de barras' ,
    'version': '8.0.4',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'stock','sale', 'sale_stock'
    ],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
