# File: Booking.py
# Description: This file contains the implementation of the Booking class, which contains
#              a booking made by a guest Also, includes methods for
#              to manage booking details, cancel booking and update check in and check out dates.
# Author: Raul Herrera
# Date: 2024-11-23
class Booking:
    def __init__(self,booking_id, guest_id, room_id, check_in_date, check_out_date, status = "Confirmed"):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status

    def modify_booking(self, new_check_in_date, new_check_out_date):
        self.check_in_date = new_check_in_date
        self.check_out_date = new_check_out_date
        print(f"Booking {self.booking_id} has been updated. New dates: {new_check_in_date} to {new_check_out_date}")

    def cancel_booking(self):
        self.status = "Canceled"
        print(f"Booking {self.booking_id} has been canceled.")

    def get_booking_details(self):
        return {
            "booking_id": self.booking_id,
            "guest_id": self.guest_id,
            "room_id": self.room_id,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "status": self.status
        }