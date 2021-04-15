#TASK ONE:

ab = float (input(" Please insert sideAB: \n"))# The user inserts
bc = float (input("Please insert sideBC: \n"))

if (ab >= 0 and bc >= 0) :
    answer = ab**2 + bc **2
    print(answer)
import math

print("Pythagoras is: \n", math.sqrt(answer)) #// ac = (ab**2 + bc**2) ** (1/2)

#TASK TWO:

list1 = [2,56,12,67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
print(" Max number in my list is: /n" + str (max (list1)))
print( "Min number in my list is: /n" + str (min (list1)))
