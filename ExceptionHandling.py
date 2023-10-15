# EXCEPTION HANDLING IN PYTHON

# TRY: Normal code to execute
# EXCEPT: Code to execute when error occurs
# ELSE : Code to execute when error does not occur
# FINALLY: Executed whether there is exception  or not

try:
    a = 9/6
    number = input("Enter a number: ") #number is a string
    number = int(number) # number is an integer
    print("YOu entered " + str(number))
except(ValueError):
    print("Wrong input: ")
except(ZeroDivisionError):
    print("You can't divide by 0")
else:
    print("Always execute when error does not occur")
finally:
    print("Whether or not error occurs")

