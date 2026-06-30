from email.policy import default

from odoo import fields,models

class Students(models.Model):
    _name = 'library.students'
    _description = 'Students'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    full_name = fields.Char(string='Full Name')
    card_id = fields.Char(string='Card ID')
    name = fields.Char(string='Name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    email = fields.Char(string='Email')
    date_of_birth = fields.Date(
        string='Date of Birth'
    )
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    status = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('suspend', 'Suspend'),
    ], string='Status', default='ongoing')
    borrow_count = fields.Integer(
        string="Borrow Count",
        compute="_compute_borrow_count",
        default = 0
    )

    def _compute_borrow_count(self):
        for rec in self:
            rec.borrow_count = 0

    def action_view_borrows(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrow Records',
            'res_model': 'library.borrow',
            'view_mode': 'tree,form',
            'domain': [('student_id', '=', self.id)],
        }
