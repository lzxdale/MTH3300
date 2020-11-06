#******************************************************************************
# abc.py
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




################################################################################
#
# GCD function from class
#
################################################################################
import math

def gcd(m, n):
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m

def is_prime(x):
    num = math.sqrt(x)
    if x == 1:
        return False
    for i in range(2,int(num)+1):
        if x%i == 0:
            return False
    return True

#tested all working good
def prime_multi(x):
    multi = 1
    for i in range(2,x+1): #it will return itself if it is a prime already
        if is_prime(i) and x%i==0:
            multi = multi*i
    return multi

def redical(a,b,xlist,ylist): #ylist stand for redical exit and redical>c, xlist stand for redcial exit. Use mutation to count number
    c = a + b
    if gcd(a,b) != 1:
        pass
        #print("a: {0}, b: {1}, GCD: {2}".format(a,b,gcd(a,b)))
    else:
        amulti = prime_multi(a)
        bmulti = prime_multi(b)
        cmulti = prime_multi(c)
        redi = cmulti*amulti*bmulti
        #print("a: {0}, b: {1}, GCD: {2}, c: {3}, Radical: {4}".format(a, b, gcd(a, b),c,redi))
        xlist[0] += 1
        if c < redi:
            ylist[0] +=1


file = open("ab.txt",'r')
alist = file.read().split()
gcdis1=[0] #give how many time redical is printed
cgreaer_r=[0] #give how many time redical and redical>c
for i in range(int(len(alist)/2)):
    redical(a=int(alist[i*2]),b=int(alist[i*2+1]),xlist=gcdis1,ylist=cgreaer_r)
file.close()

print("fraction: {0}/{1}={2}".format(cgreaer_r[0],gcdis1[0],cgreaer_r[0]/gcdis1[0]))

####challange####
#if the prime end with one, find to possibilte of next prime end with1, 3,7,9
def challange(end):
    primes_end = {"1":0,"3":0,"7":0,"9":0}
    for i in range(11,10000000,2): #disregard single digit prime(so 5 would not interfere)
        x = str(i)
        if x[-1] == end: # first determined if it is ending with 1 or 3,7,9 so the is_prime function will not be called
            if is_prime(i): # Then check if it is a prime,
                a = i
                while True: #to find the next prime after i.
                    a += 1
                    if is_prime(a):
                        primes_end[str(a)[-1]] += 1
                        break
    total_prime = sum([primes_end[h] for h in primes_end])
    print("After prime ending with " + end)
    for k in range(1,10,2):
        if k != 5: #there is no 5 in the dictionary as well of ending of primes
            print("Chance to have {0} is {1:0.2f}%".format(k, (primes_end[str(k)]/total_prime)*100))

challange("1") #takes some time to finished
#challange("3")
#challange("7")
#challange("9")