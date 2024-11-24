# File: BillingController.py
# Description: This file uses Bill file as a subclass to generate bills, process payments, add charges, and get bill details.
# Author: Enrique Gauna
# Date: 2024-11-24
from Bill import Bill
class BillingController:
    def __init__(self):
        self.bills = []
        
    def generatebill(self, bill_id, guest_id, booking_id, total_amount):
        new_bill = Bill(bill_id, guest_id, booking_id, total_amount)
        self.bills.append(new_bill)
        print(f"Bill {bill_id} Has been generated")
        return new_bill
    
    def payments(self, bill_id, payment_amount):
        bill = None
        for b in self.bills:
            if b.bill_id == bill_id:
                bill = b
                break
        if bill:
            bill.process_payment(payment_amount)
        else:
            print(f"Bill {bill_id} not found.")
    def add_charge(self, bill_id, amount):
        bill = None
        for b in self.bills:
            if b.bill_id == bill_id:
                bill = b
                break
        if bill:
            bill.add_charge(amount)
        else:
            print(f"Bill {bill_id} not found.")
    def get_bill_details(self, bill_id):
        
        bill = None
        for b in self.bills:
            if b.bill_id == bill_id:
                bill = b
                break
        if bill:
            details = bill.get_bill_details()
            print(
                f"Bill ID: {details['bill_id']}\n"
                f"Guest ID: {details['guest_id']}\n"
                f"Booking ID: {details['booking_id']}\n"
                f"Total Amount: ${details['total_amount']:.2f}\n"
                f"Status: {details['status']}"
            )
            return bill.get_bill_details()
        else:
            return f"Bill {bill_id} not found."