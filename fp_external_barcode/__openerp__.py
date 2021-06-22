# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Código de barras externo',
    'description': 'Añade un segundo código de barras para rellenar el que trae el producto y diferenciarlo del externo. También calcula el código de barras interno a partir de la referencia en su creación' ,
    'version': '8.0.1',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'account',
    ],
    'data': [
        'views/product.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
