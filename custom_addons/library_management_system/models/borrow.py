from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class Borrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library Borrow'
    _rec_name = 'reference'

    reference = fields.Char(
        string='Reference',
        default='New',
        readonly=True,
        copy=False
    )

    student_id = fields.Many2one(
        'library.students',
        string='Student',
        required=True
    )

    book_id = fields.Many2one(
        'library.books',
        string='Book',
        required=True
    )

    qty = fields.Integer(
        string='Quantity',
        default=1,
        required=True
    )

    borrow_date = fields.Datetime(
        string='Borrow Date',
        default=fields.Datetime.now,
        required=True
    )

    due_date = fields.Datetime(
        string='Due Date'
    )

    return_date = fields.Datetime(
        string='Return Date'
    )

    notes = fields.Text(
        string='Notes'
    )

    state = fields.Selection([
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ], string='Status', default='borrowed')

    display_status = fields.Char(
        string='Display Status',
        compute='_compute_display_status'
    )

    borrow_count = fields.Integer(
        string='Total Borrows',
        compute='_compute_borrow_count'
    )

    @api.depends()
    def _compute_borrow_count(self):
        total = self.search_count([])
        for rec in self:
            rec.borrow_count = total

    @api.depends('state', 'due_date')
    def _compute_display_status(self):
        today = date.today()

        for rec in self:
            if rec.state == 'returned':
                rec.display_status = 'Returned'
            elif rec.due_date:
                days = (rec.due_date.date() - today).days
                rec.display_status = f'Borrow ({days} days)'
            else:
                rec.display_status = 'Borrow'

    @api.constrains('qty')
    def _check_qty(self):
        for rec in self:
            if rec.qty <= 0:
                raise ValidationError(
                    "Quantity must be greater than zero."
                )

    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:

            if vals.get('reference', 'New') == 'New':
                vals['reference'] = self.env[
                    'ir.sequence'
                ].next_by_code('library.borrow') or 'New'

            book = self.env['library.books'].browse(
                vals.get('book_id')
            )

            qty = vals.get('qty', 1)

            if not book:
                raise ValidationError(
                    "Please select a book."
                )

            if book.available_quantity < qty:
                raise ValidationError(
                    f"Only {book.available_quantity} book(s) available."
                )

            book.available_quantity -= qty

        return super().create(vals_list)

    def action_return_book(self):

        for rec in self:

            if rec.state == 'returned':
                continue

            rec.book_id.available_quantity += rec.qty

            rec.write({
                'return_date': fields.Datetime.now(),
                'state': 'returned'
            })

        return True
