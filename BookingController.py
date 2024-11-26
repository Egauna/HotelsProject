# File: BookingController.py
# Description: This is file contains the main controller or main Class
# to create new bookings using Room, Guest, and Booking as subclasses.
# Author: Enrique Gauna
# Date: 2024-11-24
from Room import Room
from Guest import Guest
from Booking import Booking

class BookingController:
    def __init__(self):
        self.bookings = []
        self.rooms = []
      
    
    def add_room(self, room):
        self.rooms.append(room)

    # Creates new booking for a guest if room  is available
    def create_booking(self, guest, room_number, check_in, check_out):
        room = None
        for r in self.rooms:
            if r.room_id == room_number and r.room_status:  # Assuming 'room_status' indicates availability
                room = r
                break

        if room:
            booking_id = len(self.bookings) + 1  # Generate a unique booking ID
            new_booking = Booking(
                booking_id=booking_id,
                guest_id=guest.guest_id,
                room_id=room.room_id,
                check_in_date=check_in,
                check_out_date=check_out,
                status="Confirmed"
            )
            self.bookings.append(new_booking)  # Add the new booking to the list
            room.update_availability(False)  # Mark the room as unavailable
            return {
                "success": True,
                "message": f"Booking successfully created. Booking ID: {booking_id}",
                "booking_id": booking_id
            }

        # If the room is not available
        return {
            "success": False,
            "message": "Room not available."
        }
