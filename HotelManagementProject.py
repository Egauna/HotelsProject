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


class Room:
    def __init__(self, room_id, room_type, price, availability_status, amenities):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.availability_status = availability_status

    # This function returns room details as a dictionary

    def get_room_info(self):
        return {
            "room_id": self.room_id,
            "room_type": self.room_type,
            "price": self.price,
            "availability_status": self.availability_status,
        }

    # Updates the room's availability
    def update_availability(self, status):
        self.availability_status = status
        status_text = "available" if status else "unavailable"
        print(f"Room {self.room_id} is now {status_text}.")