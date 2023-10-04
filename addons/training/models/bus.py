from odoo import _, api, fields, models

class  ResBus(models.Model):
    _name = 'res.bus'
    _description = 'Bus'

    name = fields.Char('')
    code = fields.Char('')
    image = fields.Binary('')
    capacity = fields.Float('')

    state = fields.Selection([ 
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('mt', 'Maintenance'),
        ('dp', 'Depricated'),
    ], string='Status', default='draft', copy=False)