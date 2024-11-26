# File: GuestInterface.py
# Description: This file contains the implementation of the GuestInterface class, which provides
#              menu for guests to interact with the system. Also, includes methods for
#              booking rooms and viewing bills.
# Author: Raul Herrera and Enrique Gauna
# Date: 2024-11-26
from BookingController import BookingController
from BillingController import BillingController
from Room import Room
from Guest import Guest

class GuestInterface:
    def __init__(self):
        self.booking_controller = BookingController()
        self.billing_controller = BillingController()
        self.current_guest = None
    
    def display_menu(self):
        print("\n Guest Menu \n")
        print("1. Display Room Options\n")
        print("2. Book a Room\n")
        print("3. View Bill\n")
        print("4. Exit Menu\n")

    # Use of the Booking Controller class to show some room options
    def setup_rooms(self):
        rooms = [
            Room(room_id=101, room_type="Single", price=100.0, room_status=True, amenities=["WiFi", "TV"]),
            Room(room_id=102, room_type="Double", price=150.0, room_status=True,
                 amenities=["WiFi", "TV", "Mini Bar"]),
            Room(room_id=103, room_type="Suite", price=300.0, room_status=True,
                 amenities=["WiFi", "TV", "Mini Bar", "Jacuzzi"]),
        ]
        for room in rooms:
            self.booking_controller.add_room(room)

    # Display all rooms available to the guest
    def display_room_options(self):
        print("\nAvailable Rooms:")
        for room in self.booking_controller.rooms:
            if room.availability_status:
                print(
                    f"Room ID: {room.room_id}, Type: {room.room_type}, Price: ${room.price:.2f}, Amenities: {', '.join(room.amenities)}")

    # Allows guest  to book a room and enter booking details
    def book_room(self):
        try:
            room_id = int(input("Enter the Room ID you want to book: "))
            check_in_date = input("Enter Check-In Date (YYYY-MM-DD): ")
            check_out_date = input("Enter Check-Out Date (YYYY-MM-DD): ")

            response = self.booking_controller.create_booking(
                guest=self.current_guest,
                room_number=room_id,
                check_in=check_in_date,
                check_out=check_out_date
            )
            if response.get("success"):
                # Generate a bill for the booking
                booking_id = response.get("booking_id")
                self.billing_controller.generate_bill(
                    bill_id=booking_id,
                    guest_id=self.current_guest.guest_id,
                    booking_id=booking_id,
                    total_amount=self.booking_controller.rooms[room_id - 101].price
                )
                print(response.get("message"))
            else:
                print(response.get("message"))
        except ValueError:
            print("Invalid input. Please try again.")

    # Allows the guest to view their bill
    def view_bill(self):
        try:
            bill_id = int(input("Enter your Bill ID to view details: "))
            self.billing_controller.get_bill_details(bill_id)
        except ValueError:
            print("Invalid input. Please enter a valid Bill ID.")

    def run(self):
        self.setup_rooms()
        name = input("Enter your name: ")
        email = input("Enter your Email: ")
        phone = input("Enter your phone number: ")
        self.current_guest = Guest(name=name, email=email, phone_number=phone)
        print(f"Hello {name}!")

        while True:
            self.display_menu()
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                self.display_room_options()
            elif choice == 2:
                self.book_room()
            elif choice == 3:
                self.view_bill()
            elif choice == 4:
                print("You chose to exit the menu.")
                break
            else:
                print("Invalid choice.")

if __name__ =="__main__":
    interface = GuestInterface()
    interface.run()
