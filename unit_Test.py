import unittest
from BookingController import BookingController
from Room import Room
from Guest import Guest
from Booking import Booking

class TestBookingController(unittest.TestCase):
    def setUp(self):
        self.controller = BookingController()
        self.room = Room(room_id=101, room_type="Single", price=100, amenities=["WiFi", "TV"], room_status=True)
        self.guest = Guest(guest_id=1, name="John Doe", email="john@example.com", phone_number=97878998)
        self.controller.add_room(self.room)

    def test_add_room(self):
        self.assertEqual(len(self.controller.rooms), 1)
        self.assertEqual(self.controller.rooms[0].room_id, 101)

    def test_create_booking_success(self):
        result = self.controller.create_booking(self.guest, 101, "2024-12-01", "2024-12-05")
        print(f"Result: {result}")
        print(f"Bookings: {self.controller.bookings}")
        print(f"Room status: {self.room.room_status}")
        self.assertEqual(result, "The booking has been successfully created. Booking ID: 1")
        self.assertEqual(len(self.controller.bookings), 1)
        self.assertEqual(self.controller.bookings[0].guest_id, 1)
        self.assertEqual(self.controller.bookings[0].room_id, 101)
        self.assertFalse(self.room.room_status)

    def test_create_booking_room_not_available(self):
        self.room.update_availability(False)
        result = self.controller.create_booking(self.guest, 101, "2024-12-01", "2024-12-05")
        self.assertEqual(result, "Room not available.")
        self.assertEqual(len(self.controller.bookings), 0)

    def test_create_booking_room_not_found(self):
        result = self.controller.create_booking(self.guest, 102, "2024-12-01", "2024-12-05")
        self.assertEqual(result, "Room not available.")
        self.assertEqual(len(self.controller.bookings), 0)

if __name__ == '__main__':
    unittest.main()