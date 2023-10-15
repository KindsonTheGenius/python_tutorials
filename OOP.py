# ****************** OBJECT ORIENTED PROGRAMMING OOP IN PYTHON *********************
# CREATING CLASSES
# CREATING OBJECTS
# ACCESSING ATTRIBUTES
# BUILT-IN ATTRIBUTES (__dict__, __doc__, __name__, __module__, __bases__)
# GARBAGE COLLECTION

# INHERITANCE IN PYTHON (is-a retionship)
# child, derived, sub-class


from Employee import Employee, Driver

emp1  = Employee("Kany", "ID", 545000)

drv1 = Driver("Ollie", "Asset",7000)
drv1.car = "Honda Civic"

print(isinstance(emp1,Driver))






