# File: Guest.py
# Description: This file contains the implementation of the Guest class, which contains
#              guest's name, id, email and phone number. Also, includes methods for
#              booking rooms, requesting room services and viewing bills.
# Author: Raul Herrera
# Date: 2024-11-23
class Guest:
    def __init__(self, guest_id, name, email, phone_number):
        # Creates a new guest with their information like id, name, email, and phone number
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.booking = None  # Stores the current booking for the guest
        self.bill = None  # Stores the current bill for the guest

    # Books a room for the guest using a dictionary
    def book_room(self, room_id, check_in_date, check_out_date):
        self.booking = {
            "room_id": room_id,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date
        }
        print(f"Guest {self.name} booked Room {room_id} form {check_in_date} to {check_out_date}.")

    # Guest can request room service
    def request_room_service(self, service):
        print(f"Guest {self.name} requested room service: {service}")

    # Prints total amount due and status of the payment fo the guest
    '''def view_bill(self, total_amount, status):
        self.bill = {
            "total_amount" : total_amount,
        }'''


