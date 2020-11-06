#******************************************************************************
# binary.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#Rong: simplify the formula
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import random
a1 = random.randrange(2)
a2 = random.randrange(2)
a3 = random.randrange(2)
a4 = random.randrange(2)
a5 = random.randrange(2)
a6 = random.randrange(2)
a7 = random.randrange(2)
a8 = random.randrange(2)
print("Here’s a random example of binary!")
print("The binary number",a1,a2,a3,a4,a5,a6,a7,a8,"is the same as the decimal number", (a1*128+a2*64+a3*32+a4*16+a5*8+a6*4+a7*2+a8*1))

# Challenge question
num = int(input("Now, enter a decimal number between 0 and 255: "))
a1 = int(num/128)
a2 = int(num%128/64)
a3 = int(num%128%64/32)
a4 = int(num%128%64%32/16)
a5 = int(num%128%64%32%16/8)
a6 = int(num%128%64%32%16%8/4)
a7 = int(num%128%64%32%16%8%4/2)
a8 = int(num%128%64%32%16%8%4%2)
print("This number is equivalent to the binary number:", a1, a2, a3, a4, a5, a6, a7, a8)
