from odoo import fields, models

class Department(models.Model):
    _name = 'school.department'
    _description = 'Department'
    _inherit = ['mail.thread']
    name = fields.Char(string="Department Name", required=True, tracking=True)
    note = fields.Text(string="Note")