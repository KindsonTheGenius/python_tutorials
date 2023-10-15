# The employee class in python
class Employee:
    employeeCount = 0

    # This is a constructor (initializer)
    def __init__(self, firstname, lastname,  department, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.department = department
        self.salary = salary

    def display(self):
        print("Name: " + self.firstname + ", " + self.lastname)

class Driver(Employee):
    car = " "

    def display(self):
                print("Name: " + self.firstname + ", " + self.lastname)
                print("Assigned car: " + self.car)


employee1 = Employee("Osondu", "Munonye","Admin","5000")

employee2 = Employee("Adaku", "Okeke", "Human Resource", 5400)

driver1 = Employee("Jackson", "Bills","Assets",4400)

driver2 = Employee("Okereke", "Joseph", "Maintenance", 3300)
