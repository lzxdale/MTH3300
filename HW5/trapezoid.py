#******************************************************************************
# trapezoid.py
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
from math import pi, cos,sin, sqrt, ceil

N = int(input("plz enter the value for N: "))
a = -1
b = 1

def fuc(num):
    var = num*pi
    if num < 0:
        p1 = (1+num)
    elif num >= 0:
        p1 = (1-num)
    p2 = cos(var)
    return p1*p2


def trapezoid(a,b,N,fuc):
    diff = (b-a)/N
    thesum = 0
    diff2 = diff / 2
    for i in range(1, N): # this will not include the first and the last
        x = a + diff * i
        x2 = fuc(x)
        thesum += 2*x2  # this include two fuc1(b)
    answer = diff2 * (fuc(a) + thesum + fuc(b))
    return answer

print("the answer for sin square is: {0:.7f}".format(trapezoid(a,b,N,fuc)))

######challenge######
er = float(input("plz enter an error tolerance: "))

'''
def trapezoid_er(a, b, er, fuc):
    true_an = trapezoid(a, b, 10000 , fuc)  # As N goes bigger, the answer would be more accurate to the real answer
    for n in range(1, 10001):  # to test all possible N
        ans = trapezoid(a, b, n, fuc) # each N would return a possible answer
        diff = abs(true_an - ans) # the difference should be the absolute value!!!!!
        if diff <= abs(er): #abs er incase user enter negative er
            print("Begin at {0} steps, the error tolerance is below or equal to {1}".format(n, er))
            print('And the answer is:', ans)
            return
    print("the error tolerance is too low")

trapezoid_er(a, b, er, fuc)
'''

#from https://en.wikipedia.org/wiki/Trapezoidal_rule#CITEREFAtkinson1989 about error tolerance

#cos(πx)+xcos(πx) derivative = -πsin(πx) + cos(πx)- xπsin(πx)
#double derivative = -π^2cos(πx) - sin(πx) - (πx^2cos(πx)+πsin(πx))
# = -π^2cos(πx) - sin(πx) - πx^2cos(πx) - πsin(πx)
#cos(πx)-xcos(πx) derivative = -πsin(πx) -cos(πx) + xπsin(πx)
#double derivative = -π^2cos(πx) + sin(πx) + (πx^2cos(πx)+πsin(πx))

def fuc_dd(x):
    if x < 0:
        ans = -pi**2 * cos(pi*x) - sin(pi*x) - (pi * x ** 2)* cos(pi*x) - pi*sin(pi*x)
    elif x >= 0:
        ans = -pi**2 * cos(pi*x) + sin(pi*x) + (pi * x ** 2) * cos(pi*x) + pi*sin(pi * x)
    return ans
#error = -(b-a)^3/(12N^2) * fuc_dd(h) for h between a,b
#n^2 = (-(b-a)^3)*fuc_dd(h)/12error

def find_N():
    n = ((-(b - a) ** 3) * fuc_dd((a+b)/2))/(12*er) # I am quite confuse what should i use for x in fuc_dd(x), as they are using ξ as notation
    ans = sqrt(n)
    ans_r = ceil(ans) # it will always round up
    print("Begin at {0} steps, the error tolerance is below or equal to {1}".format(ans_r, er))

find_N()

