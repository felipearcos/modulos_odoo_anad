# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos (<felipe@florprohibida.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import models, fields, api, _, SUPERUSER_ID
import re
from openerp.exceptions import Warning as UserError

class PosCategory(models.Model):

    _inherit = 'pos.category'

    # Digito que identifica la categoria. Solo necesario rellenarlo en la categoria PADRE
    code = fields.Char(size=10, string="Digito de categoria")
    # Secuencia que se utilizara para generar automaticamente los digitos pertenecientes al producto
    sequence_id = fields.Many2one('ir.sequence', ondelete='cascade', string="Secuencia de producto", domain="[('code', '=', 'base.producto.auto.sequence')]"
)
    # Secuencia que se utilizara para generar automaticamente los digitos pertenecientes a la referencia hijo
    sequence_cat_id = fields.Many2one('ir.sequence', ondelete='cascade', string="Secuencia de cat.hijo", domain="[('code', '=', 'base.categoria.auto.sequence')]"
)
    # Variable booleana que permite activar o desactivar la secuencia automatica en esta categoria
    use_sequence = fields.Boolean('Activar secuencia')

    # Codigo real y final que va a aparecer en los primeros digitos de la referencia. Calculado automaticamente.
    prefix_code = fields.Char(compute='_prefix_code', store=True, string="Prefijo de referencia")

    ''' 
    Crea una nueva secuencia de producto para cada categoria(hijo 1) de tipo sin hueco. Para generar automaticamente esa
    parte de la referencia cuando se cree un producto de esa categoria.
    '''
    @api.multi
    def create_sequence(self, record): 
        name = record.name_get()[0][1]
        sequence_code = self.env['ir.sequence.type'].search(
            [('code', '=', 'base.producto.auto.sequence')]) or ''
        if sequence_code:
            sequence_code = sequence_code.code
        seq = {
            'name': name,
            'implementation': 'no_gap',
            'padding': 3,
            'number_increment': 1,
            'code': sequence_code,
        }
        return self.env['ir.sequence'].create(seq)


    ''' 
    Crea una nueva secuencia de categoria para cada categoria padre de tipo sin hueco. Para generar automaticamente esa
    parte de la referencia cuando se cree una categoria con esa categoria padre.
    '''
    @api.multi
    def create_cat_sequence(self, record):
        # Crea una nueva secuencia de categoria para cada categoria padre (tipo sin hueco)
        name = record.name_get()[0][1]
        sequence_code = self.env['ir.sequence.type'].search(
            [('code', '=', 'base.categoria.auto.sequence')]) or ''
        if sequence_code:
            sequence_code = sequence_code.code
        cat_seq = {
            'name': 'CAT ' + name,
            'implementation': 'no_gap',
            'padding': 2,
            'number_increment': 1,
            'code': sequence_code,
        }
        return self.env['ir.sequence'].create(cat_seq)    

    '''
    Obtiene el nivel de la categoria con la que se esta trabajando. Si es 0 es una categoria padre. Si es 1 es una categoria
    hijo de primer nivel. Si es 3 es una categoria hijo de un nivel superior.
    '''
    @api.multi
    def getLevel(self):
        level = 0
        for cat in self:
            # Si tiene categoria padre:
            if cat.parent_id:
                cat_padre = cat.parent_id
                # Si la categoria padre tiene padre (nivel 2 o mas)
                if cat_padre.parent_id:
                    level = 3
                    return level
                else:
                    level = 1
                return level
            # Si no tiene categoria padre:
            else:
                level = 0
                return level
    
    '''
    Calcula automaticamente los digitos del campo "code" cuando se establece una categoria padre.
    '''
    @api.onchange('parent_id')
    def setCode(self):
        sequence_model = self.env['ir.sequence']
        for cat in self:
            # Si no tiene categoria padre: No se le pone otro codigo
            if not self.parent_id: 
                self.code = ''
            # Si tiene categoria padre: 
            else:
                parent_cat = self.parent_id     
                self.code = sequence_model.next_by_id(parent_cat.sequence_cat_id.id)

    '''
    Sobreescribe el metodo create para realizar las operaciones necesarias cuando se crea una categoria.
    '''                
    @api.model
    def create(self, vals):
        res = super(PosCategory, self).create(vals)
        # Creacion de la secuencia de producto, si esta "usar secuencia" activado
        level = res.getLevel()
        # Si el nivel no es 3 (categoria hijo nivel 2 o mas) le pone la secuencia automaticamente
        if level != 3:
            if (not res.sequence_id and res.use_sequence and res.parent_id):

                seq_id = res.sudo().create_sequence(res)
                res.sequence_id = seq_id.id

            # Creacion de la secuencia de categoria. Si no la tiene y ademas no tiene categoria padre (es la padre, se la crea)       
            elif (not res.sequence_cat_id and res.use_sequence and not res.parent_id):    
                seq_cat_id = res.sudo().create_cat_sequence(res)
                res.sequence_cat_id = seq_cat_id.id
        return res

    '''
    Sobreescribe el metodo write para realizar las operaciones necesarias cuando se modifica una categoria.
    '''
    @api.multi
    def write(self, vals):
        res = super(PosCategory, self).write(vals)
        for cat in self:
            level = self.getLevel()     
            seq_id = self.sequence_id

            # Si el nivel no es 3 (categoria hijo nivel 2 o mas) le pone la secuencia automaticamente
            if level != 3:

                if (not cat.sequence_id and cat.use_sequence and cat.parent_id):
                    name = cat.name_get()[0][1]
                    seq_id = cat.env['ir.sequence'].search([('name', '=', name)])
                    if not seq_id:
                        seq_id = cat.sudo().create_sequence(cat)
                    cat.sequence_id = seq_id.id
               
                elif (not cat.sequence_cat_id and cat.use_sequence and not cat.parent_id):
                    name = cat.name_get()[0][1]
                    seq_cat_id = cat.env['ir.sequence'].search([('name', '=', 'CAT '+name)])
                    if not seq_cat_id:
                        seq_cat_id = cat.sudo().create_cat_sequence(cat)
                    cat.sequence_cat_id = seq_cat_id.id
        return res

    '''
    Calcula el prefijo de la referencia a partir de los digitos de sus respectivas categorias.
    '''
    @api.one
    @api.depends('code', 'parent_id', 'parent_id.code')
    def _prefix_code(self):
        code = self.code or ''
        if self.parent_id:
            parent_code = self.parent_id.prefix_code or ''
            code = '%s%s' % (parent_code, code)
        self.prefix_code = code

    
    '''
    Comprueba si la categoria tiene una secuencia relacionada para asignarsela
    '''
    def get_product_sequence(self):
        category = self
        code = ''
        if category.use_sequence and category.sequence_id:
            sequence_model = self.env['ir.sequence']
            code = '{prefix_code}{sequence}'
            code = code.format(
                prefix_code=category.prefix_code,
                sequence=sequence_model.next_by_id(category.sequence_id.id))
        return code

    ''' 
    Establece el nombre de la secuencia de categoria, para que se llame igual que la propia categoria.
    '''
    def update_cat_seq_name(self, cat, seq):
        seq.name = cat.name_get()[0][1]



class ProductTemplate(models.Model):

    _inherit = 'product.template'

    ''' 
    Obtiene la referencia siguiente a partir de la secuencia, comprueba si no esta asignada ya y la devuelve
    '''

    def _get_sequence_vals(self, values):
        pos_categ_id = False
        if values.get('pos_categ_id', False) \
                and not values.get('default_code', ''):
            pos_categ_id = values['pos_categ_id']
        if pos_categ_id:
            category = self.env['pos.category'].browse(pos_categ_id)
            # Recupera el codigo de la categoria
            default_code = category.get_product_sequence()
            # Si ha extraido algun codigo, lo inserta en el producto
            if default_code:
                # Comprueba si el codigo existe
                if self.env['product.template'].search([('default_code',
                                                        '=', default_code)]):
                    raise UserError(
                        _('El codigo {} ya existe'.format(default_code)))
                values.update({
                    'default_code': default_code, })
        return values

    '''
    Actualiza la referencia de producto
    '''    
    @api.multi
    def update_sequence(self):
        for product in self:
            values = product._get_sequence_vals({
                'pos_categ_id': product.pos_categ_id.id,
                })
            if values.get('default_code', ''):
                product.write(values)
        return True

    '''
    Asigna una referencia valida dependiendo de la categoria a la que pertenezca un producto nuevo
    '''
    @api.model
    def create(self, values):
        if not values.get('default_code', False):
            values = self._get_sequence_vals(values)
        product = super(ProductTemplate, self).create(values)
        return product