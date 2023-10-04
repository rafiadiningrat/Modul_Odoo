from odoo import _, api, fields, models

class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description = 'Bus Schedule'

    name = fields.Char('')
    schedule = fields.Datetime('')
    departure = fields.Datetime('')
    arrival = fields.Datetime('')
    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('tf', 'Transfer'),
    ], string='Payment Type')

    bus_id = fields.Many2one('res.bus', string='Bus')