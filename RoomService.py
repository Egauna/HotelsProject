# File: RoomService.py
# Description: This file contains the implementation of the RoomService class, which contains
#              a room service request made by guest. It includes methods
#              to manage room service details, and update request status.
# Author: Raul Herrera
# Date: 2024-11-23
class RoomService:
    def __init__(self, service_id, guest_id, service_type, price, status = "Pending"):
        self.service_id = service_id
        self.guest_id = guest_id
        self.service_type = service_type
        self.price = price
        self.status = status

    def update_status(self, new_status):
        self.status = new_status
        print(f"Room service request {self.service_id} status updated to {new_status}.")

    def get_service_details(self):
        return {
            "service_id": self.service_id,
            "guest_id": self.guest_id,
            "service_type": self.service_type,
            "price": self.price,
            "status": self.status
        }