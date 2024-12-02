# File: AdminClass.py
# Description: This file contains the implementation of the Admin class.
#               Here we are adding, viewing, and removing staff members. 
#               We are also viewing reports as well as performing back-ups.
# Author: Enrique Gauna
# Date: 2024-11-25

class Admin:
    def __init__(self, admin_id, name, role):
        self.admin_id = admin_id
        self.name = name
        self.role = role
        self.staff = []
        self.reports = []
        
    def add_staff_member(self, staff_id, name, role):
        staff_member = {
            "staff_id": staff_id,
            "name": name,
            "role": role
        }
        self.staff.append(staff_member)
        print(f"Staff Member: {name} \n Staff ID: {staff_id} \n Role: {role}")
    
    def remove_staff_member(self, staff_id):
        for staff in self.staff:
            if staff["staff_id"] == staff_id:
                self.staff.remove(staff)
                print(f'Staff Member {staff['name']}  with ID: {staff_id} has been removed.')
                return 
        else:
            print(f"Staff Member with ID: {staff_id} not found.")
    def view_staff(self):
        for staff in self.staff:
            print(f"Staff ID: {staff['staff_id']} \n Name: {staff['name']} \n Role: {staff['role']}")
    
    def view_reports(self):
        print("Reports")
        for report in self.reports:
            print(report)
    
   # def perform_backup(self):
    
if __name__ == "__main__":
    admin_id = input("Enter Admin ID: ")
    name = input("Enter Admin Name: ")
    role = input("Enter Admin's Rols:")
    Admin1 = Admin(admin_id=admin_id, name=name, role=role)
    Admin1.add_staff_member(1, "John Doe", "Staff")
    Admin1.add_staff_member(2, "Jane Doe", "Staff")
    Admin1.view_staff()
    Admin1.remove_staff_member(1)
    Admin1.view_staff()
    Admin1.view_reports()
    print(f"Hello, {Admin1.name}! you are now logged in as Admin with ID: {Admin1.admin_id}")