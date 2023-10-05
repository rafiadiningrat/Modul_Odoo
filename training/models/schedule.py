from odoo import _, api, fields, models

class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description = 'Bus Schedule'
    _order = 'name desc'

    name = fields.Char('')
    schedule = fields.Datetime('')
    departure = fields.Datetime('')
    arrival = fields.Datetime('')
    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('tf', 'Transfer'),
    ], string='Payment Type')

    capacity = fields.Float(related='bus_id.capacity')
    bus_id = fields.Many2one('res.bus', string='Bus')
    route_id = fields.Many2one('bus.route', string='Route')
    baggage_line_ids = fields.One2many('baggage.baggage', 'schedule_id', string='Baggage_line')
    passanger_ids = fields.Many2many('res.passanger', string='Passanger')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('run', 'On Going'),
        ('done', 'Done'),
    ], string='status', default='draft', copy=False)

    @api.model
    def create(self, value):
        value['name'] = self.env['ir.sequence'].next_by_code('bus.schedule')
        return super(BusSchedule, self).create(value)
    
    def button_submit(self):
        self.state = 'submit'

    def button_run(self):
        self.state = 'run'

    def button_done(self):
        self.state = 'done'

    def button_draft(self):
        self.state = 'draft'


    class BaggageBaggage(models.Model):
        _name = 'baggage.baggage'
        _description = 'Baggage'

        name = fields.Char('')
        weight = fields.Float('weight (kg)') 

        schedule_id = fields.Many2one('bus.schedule', string='Schedule') 