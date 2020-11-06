#******************************************************************************
# quintic.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
coco = []

for i in range(6):
    coco.append(float(input("Enter x^{} coefficient:".format(i)))) #store all the coefficient

xi = float(input("take a guess plz:")) #will give x0

# derviative = c5*5x^4+c4*4x^3+c3*3x^2+c2*2x+c1
def fuc(alist, x): #geting the func answer with certarin x
    ans = 0
    for power, i in enumerate(alist): #power is the index
        ans += i*x**power
    return ans

def fuc_d(alist, x): #func of derivative
    ans = 0
    for power, i in enumerate(alist): #power is the index
        if power != 0: #so it will pass c0 as there is no x and will be 0
            ans += i*power*x**(power-1)
    return ans

def main():
    global xi
    for i in range(10): #runing 10 times
        xi =  xi- fuc(coco, xi)/fuc_d(coco, xi)
    print(xi)

main()

##challange##
ert = float(input("Enter a error tolerance"))


def challange():
    i = 0
    while True: #running until break
        x =  xi- fuc(coco, xi)/fuc_d(coco, xi)
        i += 1 #it will act as a for loop index
        if abs(fuc(coco,x)) <= abs(ert):
            print(x)
            break
        if i == 10**30:
            print("exit the loop")
            break
challange()
