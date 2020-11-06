#******************************************************************************
# quadratic.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#None
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math

a = float(input("Enter x^2 coefficient:"))
b = float(input("Enter x^1 coefficient:"))
c = float(input("Enter x^0 coefficient:"))

if a == 0 and b == 0:
    print("This is not a function")
    print(c,"=",c)
elif a == 0 and b != 0:
    x = -c/b
    if x != 0:
        print("One real solution: x = {:.4}".format(x))
    elif x == 0: # To avoid printing out x = -0
        print("One real solution: x = 0")
#x = (-b +or- math.sqrt(b^2 - 4ac))/2a
elif a != 0:
    root_val = b**2 - 4*a*c
    if root_val > 0: # it will generate two real solution
        root = math.sqrt(b**2- 4*a*c)
        x1 = (-b + root)/2/a
        x2 = (-b - root)/2/a
        print("Two real solution: x = {0:.4}, and x = {1:.4}".format(x1, x2))
    elif root_val == 0:
        if b == 0 and c == 0:  # eliminate printing out x = -0
            print("One real solution: x = 0")
        # it will only generate one
        else:
            x = (-b) / 2 / a
            print("One real solution: x = {:.4}".format(x))
    else:
        root = math.sqrt(abs(b ** 2 - 4 * a * c))/2/a #turn b**2 - 4ac into absolute value so sqrt can be done
        x = (-b) / 2 / a # real number and imaginary number will be separate.
        if x != 0:
            root = abs(root) # eliminate printing out x = - -4i or + - 4i
            print("Complex solution: x = {0:.4} - {1:.4}i and x = {0:.4} + {1:.4}i".format(x, root))
        else:
            print("Complex solution: x = -{0:.4}i and x = {0:.4}i".format(root))
