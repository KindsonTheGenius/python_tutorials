# ************** INSERTION SORT CODE *************
import random
values = [21,2, 7, 2, 4, 100, 8, 1]

# BEFORE INSERTION SORT
print(values)


# WE WILL WRITE THE INSERTION SORT CODE HERE
for i in range(1, len(values)):
    for j in range(i, 0, -1):
        if values[j] < values[j-1]:
            # swap
            temp = values[j]
            values[j] = values[j-1]
            values[j-1] = temp

# AFTER INSERTION SORT
print("Sorted List: ")
print(values)

for i in range(1,0):
    print(i)
