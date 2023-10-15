# ***************** WORKING WITH CONDITIONAL STATEMENTS ********************
# IF STATEMENT
# ELSEIF STATEMENT (ELIF)
# OR OPERATOR
# AND OPERATOR
# NOT OPERATOR
# CREATING A GRADE SHEET (70-100:A, 60-69:B, 50-59:C, BELOW 50:D
try:
    score = input("Please enter a score: ")
    score = float(score) # Convert it to from a string to a integer

    if score >= 70 and score <= 100:
        grade = "A"
    elif score >= 60 and score <= 69:
        grade ="B"
    elif score >= 50 and score <= 59:
        grade = "C"
    elif score < 50 and score >= 0:
        grade = "D"
    else:
        print("Invalid entry")
    print("The grade is %s " %(grade))
except:
    print("Invalid Entry")
