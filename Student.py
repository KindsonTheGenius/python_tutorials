# ***************** HOW TO CREATE A CLASS IN PYTHON **************************
# Written by: Kindson The Genius
# Date: December 26th, 2018

class Student:

    # Class Variable
    studentCount = 0

    # Constructor
    def __init__(self, regno, firstname, lastname, course, email, level, gpa):
        self.regno = regno
        self.firstname = firstname
        self.lastname = lastname
        self.address = course
        self.email = email
        self.phone = level
        self.gpa = gpa

    # Member Function
    def display(self):
        print("Name: %s %s; Reg No. %s" %(self.firstname, self.lastname, self.regno))

# ******************************** END OF CLASS ****************************************
