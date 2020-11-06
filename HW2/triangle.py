#******************************************************************************
# triangle.py
#******************************************************************************
# Name:Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#Rong: some help about math formula
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math

L = float(input("Enter largest side length: "))
M = float(input("Enter middle side length: "))
S = float(input("Enter smallest side length: "))

def trangle():
    L_angle=(M**2+S**2-L**2)/(2*M*S)
    L_radian_angle = math.acos(L_angle) #radian of largest angle
    L_angle = L_radian_angle/math.pi*180 # The angle of Largest
    M_angle = math.sin(L_radian_angle)/L*M #thie is sin(M)
    M_radian_angle = math.asin(M_angle)
    M_angle = M_radian_angle/math.pi*180
    S_angle = L_angle - M_angle
    print("The angles are:")
    print(L_angle)
    print(M_angle)
    print(S_angle)

#challenge

if L < 0 or M < 0 or S < 0:
    print("plz enter positive number")
elif L < M or M < S or L < S:
    print("plz enter in descending order")
elif S + M < L:
    print("didn't satisfy the triangle inequality")
else:
    trangle()





