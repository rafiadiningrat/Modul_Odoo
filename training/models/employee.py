from odoo import _, api, fields, models
from odoo.exceptions import UserError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_driver = fields.Boolean('Is Driver')
    code_driver = fields.Char('Code_Driver')
    driver_license = fields.Char('Driver License')
    driver_license_exp = fields.Date('Driver License Expired')


    @api.model
    def create (self, vals):
        vals['code_driver'] = 'DRVR-' + vals.get('name')
        res=super(HrEmployee, self).create(vals)
        # raise UserError(_("Mohon maaf tidak bisa create .."))
        return res
    
    def write(self, vals):
        print("Berhasil", vals)
        vals['is_driver'] = True
        res=super(HrEmployee, self).write(vals)
        return res
    
    def unlink (self):
        res=super(HrEmployee, self).unlink()
        raise UserError(_("Mohon maaf tidak bisa delete.."))
        return res
    