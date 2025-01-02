from odoo import models, fields, api

class Hotel(models.Model):
    _name = "hotel.management.hotel"
    _description = "Hotel"

    name = fields.Char(string="Hotel Name", required=True, unique=True)
    address = fields.Char(string="Address")
    number_of_floors = fields.Integer(string="Number of Floors")
    number_of_rooms = fields.Integer(string="Number of Rooms", compute="_compute_number_of_rooms")

    @api.depends("room_ids")
    def _compute_number_of_rooms(self):
        for record in self:
            record.number_of_rooms = len(record.room_ids)

    room_ids = fields.One2many("hotel.management.room", "hotel_id", string="Rooms")
