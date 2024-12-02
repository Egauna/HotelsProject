# File: staffcontroller.py
# Description: This file contains the implementation of the staff controller class, which contains
#              options for staff to process bookings, process room service requests, and generate reports.
# Author: Enrique Gauna
# Date: 2024-11-25

from Room import Room
from RoomService import RoomService
from Booking import Booking
from Guest import Guest

class StaffController:
    def __init__(self):
        self.bookings = []
        self.services = []
        self.guests = []
        self.rooms = []
    def process_booking(self, booking_id, guest_id, room_id, check_in_date, check_out_date):
        room = None
        for r in self.rooms:
            if r.room_id == room_id:
                room = r
                break
        if not room or not room.room_status:
            print(f'Room {room_id} is not available')
            return

        room.update_availability(False)
        new_booking = Booking(booking_id, guest_id, room_id, check_in_date, check_out_date)
        self.bookings.append(new_booking)
        print(f'Booking {booking_id} for Guest {guest_id} Confirmed')
        
    def process_service_request(self, service_id, guest_id, service_type, price):
        new_service = RoomService(service_id, guest_id, service_type, price)
        self.services.append(new_service)
        print(f"Room Service {service_id} for Guest {guest_id} is added")
        
    def generate_report(self):
        print("Generating Reports\n")
        
        available_rooms=[]
        for room in self.rooms:
            if room.room_status:
                available_rooms.append(room.get_room_info())
        
        print("Available Rooms:")
        for room in available_rooms:
            print(room)
        
        active_bookings = []
        for booking in self.bookings:
            if booking.status == "Confirmed":
                active_bookings.append(booking.get_booking_details())
        
        print("Active Bookings")
        for booking in active_bookings:
            print(booking)
        
        pending_services = []
        for service in pending_services:
            if service.status == "Pending":
                pending_services.append(service.get_service_details())
        print("Pending Room Services:")
        for service in pending_services:
            print(service)
            
    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room {room.room_id} added.")
        
    def add_guest(self, guest):
        self.guests.append(guest)
        print(f"Guest {guest.guest_id} added.")
        
