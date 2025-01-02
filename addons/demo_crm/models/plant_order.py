from odoo import api, fields, models, _


class PlantOrder(models.Model):
    _name = 'demo.plant_order'
    _description = 'Plant Order'
    _inherit = ['mail.thread']
