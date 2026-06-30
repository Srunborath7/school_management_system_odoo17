from odoo import fields, models

class Category(models.Model):
    _name = 'library.category'
    _description = 'library.category'
    _rec_name = 'name'

    name = fields.Char(required=True ,string="Category Name")
    code = fields.Char(required=True ,string="Category Code")
    description = fields.Char(required=True ,string="Description")
    active = fields.Boolean(default=True)
