from RoomService import RoomService

# File: room_service_controller.py

# Prologue Comment
# File: room_service_controller.py
# Description: This file contains the implementation of the RoomServiceController class,
#              which manages room service requests made by guests. It includes methods
#              for creating requests, assigning staff, and updating request statuses.
# Author: Raul Herrera
# Date: 2024-11-22

from RoomService import RoomService

class RoomServiceController:
    def __init__(self):
        self.service_requests = []  # List to store all room service requests

    def create_service_request(self, service_id, guest_id, service_type, price):
        new_request = RoomService(
            service_id=service_id,
            guest_id=guest_id,
            service_type=service_type,
            price=price
        )
        self.service_requests.append(new_request)
        print(f"Room service request {service_id} created for Guest {guest_id}.")
        return new_request

    def _find_service_request(self, service_id):
        for request in self.service_requests:
            if request.service_id == service_id:
                return request
        return None

    def assign_staff(self, service_id, staff_id):
        service_request = self._find_service_request(service_id)
        if service_request:
            print(f"Service Request {service_id} assigned to Staff {staff_id}.")
        else:
            print(f"Service Request {service_id} not found.")

    def update_status(self, service_id, new_status):
        service_request = self._find_service_request(service_id)
        if service_request:
            service_request.update_status(new_status)
        else:
            print(f"Service Request {service_id} not found.")

    def get_service_details(self, service_id):
        service_request = self._find_service_request(service_id)
        if service_request:
            details = service_request.get_service_details()
            print(
                f"Service ID: {details['service_id']}\n"
                f"Guest ID: {details['guest_id']}\n"
                f"Service Type: {details['service_type']}\n"
                f"Price: ${details['price']:.2f}\n"
                f"Status: {details['status']}"
            )
            return details
        else:
            print(f"Service Request {service_id} not found.")
            return None
