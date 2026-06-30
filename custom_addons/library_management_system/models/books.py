from odoo import fields, models

class Book(models.Model):
    _name = 'library.books'
    _description = 'Library Books'
    _rec_name = 'name'

    name = fields.Char(string="Book Title", required=True)
    isbn = fields.Char(string="ISBN")
    author_ids = fields.Many2many("library.author", string="Authors")
    publisher = fields.Char(string="Publisher")
    publication_date = fields.Date(string="Publication Date")
    edition = fields.Char(string="Edition")
    language = fields.Selection([
        ('khmer', 'Khmer'),
        ('english', 'English'),
        ('other', 'Other')
    ], string="Language")
    pages = fields.Integer(string="Pages")
    description = fields.Text(string="Description")
    price = fields.Float(string="Price")
    quantity = fields.Integer(
        string='Quantity',
        default=1
    )

    available_quantity = fields.Integer(
        string='Available Quantity',
        default=1
    )

    shelf_location = fields.Char(
        string='Shelf Location'
    )
    category_id = fields.Many2one(
        'library.category',
        string='Category',
        required=True
    )
    tag_ids = fields.Many2many(
        'library.book.tag',
        string='Tags'
    )

