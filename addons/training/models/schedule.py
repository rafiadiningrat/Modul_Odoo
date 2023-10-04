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
    route_id = fields.Many2one('bus.route', string='Route')
    baggage_line_ids = fields.One2many('baggage.baggage', 'schedule_id', string='Baggage_line')
    passanger_ids = fields.Many2many('res.passanger', string='Passanger')


    class BaggageBaggage(models.Model):
        _name = 'baggage.baggage'
        _description = 'Baggage'

        name = fields.Char('')
        weight = fields.Float('weight (kg)') 

        schedule_id = fields.Many2one('bus.schedule', string='Schedule') 