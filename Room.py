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