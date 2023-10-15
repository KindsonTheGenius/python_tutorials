# *************** WRITING FILES IN PYTHON ****************************
# WRITE() FUNCTION
# FILE MODES
# CLOSE STATEMENT
# WITH STATEMENT
# WRITELINE STATEMENT
# WRITELINES  STATEMENT
# FOR LOOP

students_data = open("students.txt", "a")

students_data.write("\nKindson The Tech Pro append")
students_data.write("\nKindson The Tech Pro append")

i = 1
while i != 11:
    students_data.write("\nKindson The Tech Pro append " + str(i))
    i = i + 1


students_data.close()



