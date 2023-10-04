# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class training(models.Model):
#     _name = 'training.training'
#     _description = 'training.training'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import _, api, fields, models

class ResPassanger(models.Model):
    _name = 'res.passanger'
    _description = 'Passanger'

    name = fields.Char('')
    weight = fields.Float('Weight (kg)')
    height = fields.Float('Height (cm)')
    born_date = fields.Date('Born Date')
    