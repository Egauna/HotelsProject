from BookingController import BookingController
from BillingController import BillingController
from Room import Room
from Guest import Guest

class GuestInterface:
    def __init__(self):
        self.booking_controller = BookingController()
        self.billing_controller = BillingController()
        self.current_guest = None
    
    def displaymenu(self):
        print("\n Guest Menu \n")
        print("1. Display Room Options\n")
        print("2. Book a Room\n")
        print("3. View Bill\n")
        print("4. Exit Menu\n")
    
    def run(self):
        self.setup_rooms()
        
        guest_id = int(input("Enter Guest ID to log in: "))
        name = input("Enter your name: ")
        email = input("Enter your Email: ")
        phone = input("Enter your phone number: ")
        self.current_guest = Guest(guest_id, name, email, phone)
        print(f"Hello {name}!")

        while True:
            self.displaymenu()
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
    # def display_room_options(self):
    
    
    #def book_room(self):
    
    
    #def view_bill(self):