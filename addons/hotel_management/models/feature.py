from odoo import models, fields

class Feature(models.Model):
    _name = "hotel.management.feature"
    _description = "Room Feature"

    name = fields.Char(string="Feature Name", required=True)
