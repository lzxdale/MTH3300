#******************************************************************************
# population.py
#******************************************************************************
# Name:Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# None
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
from math import e
def main():
    p=float(input("Plz enter initial population: "))
    t1=float(input("Plz enter first time period(in years): "))
    r1=(float(input("plz enter first growth rate (in percent): ")))/100.0
    t2=float(input("Plz enter second time period(in years): "))
    r2=(float(input("plz enter second growth rate (in percent): ")))/100.0
    t3=float(input("Plz enter third time period(in years): "))
    r3=(float(input("plz enter third growth rate (in percent): ")))/100.0
    P1 = p*e**(r1*t1) #first answer of population
    P2 = P1*e**(r2*t2) #second
    P3 = P2*e**(r3*t3) #final
    print(P3)

#challenge
P1 = float(input("Plz enter initial population: "))*e**((float(input("plz enter first growth rate (in percent): ")))/100.0*float(input("Plz enter first time period(in years): ")))
P2 = P1*e**((float(input("plz enter second growth rate (in percent): ")))/100.0*float(input("Plz enter second time period(in years): ")))
P3 = P2*e**((float(input("plz enter third growth rate (in percent): ")))/100.0*float(input("Plz enter third time period(in years): ")))
print(P3)


    



