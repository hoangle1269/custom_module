from odoo import models, fields

class Room(models.Model):
    _name = "hotel.management.room"
    _description = "Room"

    hotel_id = fields.Many2one("hotel.management.hotel", string="Hotel", required=True)
    room_code = fields.Char(string="Room Code", required=True)
    bed_type = fields.Selection([
        ("single", "Single"),
        ("double", "Double")
    ], string="Bed Type", required=True)
    price = fields.Float(string="Price", required=True)
    features = fields.Many2many("hotel.management.feature", string="Features")
    status = fields.Selection([
        ("available", "Available"),
        ("booked", "Booked")
    ], string="Status", default="available")