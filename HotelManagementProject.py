class Guest:
    def __init__(self, guest_id, name, email, phone_number):
        # Creates a new guest with their information like id, name, email, and phone number
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.booking = None # Stores the current booking for the guest
        self.bill = None # Stores the current bill for the guest

    # Books a room for the guest
    def book_room(self, room_id, check_in_date, check_out_date):
        self.booking = {
            "room_id": room_id,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date
        }
        print(f"Guest {self.name} booked Room {room_id} form {check_in_date} to {check_out_date}.")

    def request_room_service(self, service):