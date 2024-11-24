# File: Guest.py

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

#Adding the necessary main function to test Guest class attributes 
def main():
    
    guestID = int(input("Enter your Guest ID number: "))
    name1 = input("Enter your name: ")
    email = input("Enter your Email: ")
    phoneNumber = int(input("Enter your phone number: "))

    object1 = Guest(guestID,name1,email, phoneNumber) #creating the Guest object

    print(f"{object1.email}") #random print command to confirm correct literal storage

if __name__ == '__main__':
    main()



