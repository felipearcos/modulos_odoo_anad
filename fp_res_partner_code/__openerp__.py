# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Códigos de barras de cliente',
    'description': 'Sustituye el antiguo campo de EAN13 en el partner, por un Code128 que permite además poner valores múltiples' ,
    'version': '8.0.2',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'sale',
    ],
    'data': [
        'views/res_partner.xml',
        'views/partner_code.xml',
        'data/codes.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
