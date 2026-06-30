from odoo import fields, models

class Author(models.Model):
    _name = 'library.author'
    _description = 'Author'
    _rec_name = 'name'

    name = fields.Char(string="Author Name")
    age = fields.Integer(string = "Age")
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email Address")
    address = fields.Char(string="Address")
    book_ids = fields.Many2many('library.books', string="Book")
