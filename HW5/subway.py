#******************************************************************************
# subway.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#Rong, to improve efficiency
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import random

#my original method
def train_test1():
    total = 0
    late = 0
    for i in range(0, 20):
        new = random.randint(1,100)
        if total+new <= 1000:
            total += new
        elif total+new > 1000: #the existing plus new is more than 1000
            if total < 1000: #thus some still can get in the train
                late += total+new-1000
                total = 1000
            elif total == 1000:
                late += new
    return late

#method from Rong
def train_test2():
    total = 0
    late = 0
    alist = []
    for i in range(0, 20):
        alist.append(random.randint(1, 100))
        if sum(alist) >= 1000:
            late = sum(alist)-1000
        else:
            late = 0
    return late

late = 0
totallate= 0
#for i in range(100000):
#    late += train_test2()
#print(late/100000)

##challenge##

import matplotlib.pyplot as plt

#https://stackoverflow.com/questions/16010869/python-plot-a-bar-using-matplotlib-using-a-dictionary
#names = list(data.keys())
#values = list(data.values())

numperlate = {}
for i in range(1001): #if all are 100, the the late would be 1000
    numperlate[i] = 0

for i in range(100000):
    late = train_test2()
    totallate += late
    numperlate[late] += 1

print(totallate/100000) #average late per train, answer for question 1

numbers = list(numperlate.keys()) #list each possibile dice total
numbers = numbers[1:]           #delete 0 1 as it is too big
values = list(numperlate.values())#list the frequence of each round dice total
values = values[1:]             #delete value ot 0
plt.bar(numbers, values)
#plt.hist(values)
plt.show()


