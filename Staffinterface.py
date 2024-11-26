# File: StaffInterface.py
# Description: This file contains the staff interface class
#              In this file the staff will have the options to add rooms; change availabity status on the rooms.
#               Add Guest information
#               Process Bookings for Guests
#               Process room services for Guests
#               Generate reports pertaining Avaiable rooms
#               an option to exit the menu
# Author: Enrique Gauna
# Date: 2024-11-25
from staffcontroller import StaffController
from Room import Room
from Guest import Guest

class StaffInterface:
    def __init__(self):
        self.controller = StaffController()
    
    def displaymenu(self):
        print("\nStaff Menu\n")
        print("1. Add Room\n")
        print("2. Add Guest\n")
        print("3. Process Booking\n")
        print("4. Process Room Service\n")
        print("5. Generate Report\n")
        print("6. Exit\n")
        
    def run(self):
        while True:
            self.displaymenu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_room()
            elif choice == '2':
                self.add_guest()
            elif choice == '3':
                self.process_booking()
            elif choice == '4':
                self.process_service_request()
            elif choice == '5':
                self.controller.generate_report()
            elif choice == '6':
                print("You chose to exit the interface. GoodBye")
                break
            else:
                print("Invalid Choice.")
    def add_room(self):
        room_id = int(input("Enter Room ID: "))
        room_type = input("Enter Room Type: ")
        price = float(input("Enter Price: "))
        amenities = input("Enter Amenities: ").split(",")
        room = Room(room_id, room_type, price, amenities)
        self.controller.add_room(room)
        print("Room Added Successfully")
    
    def add_guest(self):
        guest_id = int(input("Enter Guest ID: "))
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        guest = Guest(guest_id, name, email, phone)
        self.controller.add_guest(guest)
        print("Guest Added Successfully")
        
    def process_booking(self):
        booking_id = int(input("Enter Booking ID: "))
        guest_id = int(input("Enter Guest ID: "))
        room_id = int(input("Enter Room ID: "))
        check_in_date = input("Enter Check-In Date: ")
        check_out_date = input("Enter Check-Out Date: ")
        self.controller.process_booking(booking_id, guest_id, room_id, check_in_date, check_out_date)
    
    def process_service_request(self):
        service_id = int(input("Enter Service ID: "))
        guest_id = int(input("Enter Guest ID: "))
        service_type = input("Enter Service Type: ")
        price = float(input("Enter Price: "))
        self.controller.process_service_request(service_id, guest_id, service_type, price)
        
if __name__ == "__main__":
    interface = StaffInterface()
    interface.run()