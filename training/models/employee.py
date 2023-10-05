from odoo import _, api, fields, models

class HrEmpoyee(models.Model):
    _inherit = 'hr.employee'

    is_driver = fields.Boolean('Is Driver')
    driver_license = fields.Char('Driver License')
    driver_license_exp = fields.Date('Driver License Expired')
