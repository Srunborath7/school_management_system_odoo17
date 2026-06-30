from odoo import models, fields

class BookTag(models.Model):
    _name = 'library.book.tag'
    _description = 'Book Tag'
    _rec_name = 'name'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Char(string='Tag Color', required=True)
    remark = fields.Char(string='Remark', required=True)