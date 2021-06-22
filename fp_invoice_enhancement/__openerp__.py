# coding: utf-8
# © 2018 Felipe Arcos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Mejoras en la factura',
    'description': 'Permite validar las facturas pagadas, calcula las facturas que tienen pago parcial y extrae el numero de Simplificada para mejor legibilidad y ordenacion' ,
    'version': '8.0.6',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'account', 'point_of_sale',
    ],
    'data': [
        'account_invoice.xml',
        'wizard/update_validation.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
