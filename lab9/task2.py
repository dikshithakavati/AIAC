# Define a class named sru_student
class sru_student:
    # Initialize the attributes: name, roll_no, hostel_status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Store student's name
        self.roll_no = roll_no  # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel status (True/False)
        self.fee_paid = False  # Initialize fee status as unpaid

    # Method to update fee status
    def fee_update(self, status):
        self.fee_paid = status  # Update fee status

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")  # Print student's name
        print(f"Roll No: {self.roll_no}")  # Print student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Fee Paid: {self.fee_paid}")  # Print fee status

# Create an instance of sru_student
student1 = sru_student("Alice", 101, True)  # Create student with name, roll no, hostel status

# Update fee status for student1
student1.fee_update(True)  # Mark fee as paid

# Display details of student1
student1.display_details()  # Show all details of student1