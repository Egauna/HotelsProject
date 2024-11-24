# File: Bill.py
# Description: This file contains the implementation of the Bill class, which contains
#              bill id, guest id, booking id, total amount due, and status. Additionally, it includes
#              methods that manage processing payments, adding charges and requesting billing details.
# Author: Raul Herrera
# Date: 2024-11-23
class Bill:
    def __init__(self, bill_id, guest_id, booking_id, total_amount, status="Unpaid"):
        self.bill_id = bill_id
        self.guest_id = guest_id
        self.booking_id = booking_id
        self.total_amount = total_amount
        self.status = status

    def process_payment(self, payment_amount):
        if payment_amount >= self.total_amount:
            self.status = "Paid"
            print(f"Bill {self.bill_id} has been fully paid. Change: ${payment_amount - self.total_amount:.2f}")
        else:
            print(
                f"Insufficient payment for Bill {self.bill_id}. Amount still due: "
                f"${self.total_amount - payment_amount:.2f}")

    def add_charge(self, amount):
        self.total_amount += amount
        print(f"${amount:.2f} has been added to Bill {self.bill_id}. New total: ${self.total_amount:.2f}")

    def get_bill_details(self):
        return {
            "bill_id": self.bill_id,
            "guest_id": self.guest_id,
            "booking_id": self.booking_id,
            "total_amount": self.total_amount,
            "status": self.status
        }