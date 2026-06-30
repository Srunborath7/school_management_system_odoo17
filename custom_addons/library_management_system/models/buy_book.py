from odoo import fields, models, api
from odoo.exceptions import ValidationError
class BuyBook(models.Model):
    _name = 'library.buybooks'
    _description = 'Buy Book'

    student_ids = fields.Many2one("library.students",string="Student")
    book_ids = fields.Many2one("library.books",string="Book")
    qty = fields.Float(string="Quantity")
    price = fields.Float(
        string='Price',
        related='book_ids.price',
        store=True,
    )
    note = fields.Char(string="Note")
    total = fields.Float(
        compute='_compute_total',
        store=True
    )

    @api.depends('qty', 'price')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.qty * rec.price

    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:

            book = self.env['library.books'].browse(
                vals.get('book_ids')
            )

            qty = vals.get('qty', 1)

            if book.available_quantity < qty:
                raise ValidationError(
                    f"Only {book.available_quantity} book(s) available."
                )

            if book.quantity < qty:
                raise ValidationError(
                    f"Only {book.quantity} book(s) available."
                )

            book.write({
                'available_quantity': book.available_quantity - qty,
                'quantity': book.quantity - qty,
            })

        return super().create(vals_list)