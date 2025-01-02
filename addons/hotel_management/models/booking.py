from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Booking(models.Model):
    _name = "hotel.management.booking"
    _description = "Room Booking"

    booking_code = fields.Char(string="Booking Code", required=True, unique=True)
    customer_name = fields.Char(string="Customer Name", required=True)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    hotel_id = fields.Many2one("hotel.management.hotel", string="Hotel", required=True)
    room_type = fields.Selection([
        ("single", "Single"),
        ("double", "Double")
    ], string="Room Type", required=True)
    room_id = fields.Many2one("hotel.management.room", string="Room", domain="[('hotel_id', '=', hotel_id), ('status', '=', 'available')]", required=True)
    check_in_date = fields.Date(string="Check-In Date", required=True)
    check_out_date = fields.Date(string="Check-Out Date", required=True)
    status = fields.Selection([
        ("new", "New"),
        ("confirmed", "Confirmed")
    ], string="Status", default="new")

    @api.constrains("check_in_date", "check_out_date")
    def _check_dates(self):
        for record in self:
            if record.check_in_date > record.check_out_date:
                raise ValidationError("Check-in date cannot be later than check-out date.")

    def confirm_booking(self):
        self.write({"status": "confirmed"})
        self.room_id.write({"status": "booked"})