# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Precio tachado para ofertas y etiquetas personalizadas',
    'description': '' ,
    'version': '8.0.1',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'sale', 'stock',
    ],
    'data': [
        'views/product_template.xml',
        'views/product_product_label_view.xml',
        'report/label.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
