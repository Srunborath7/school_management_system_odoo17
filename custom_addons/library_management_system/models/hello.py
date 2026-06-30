from odoo import models, fields

class Hello(models.Model):
    _name = 'hello.world'
    _description = 'Hello World'
    name = fields.Char(required=True)