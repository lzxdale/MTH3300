# ******************************************************************************
# beverages.py
# ******************************************************************************
# Name: Zexiang Lin
# ******************************************************************************
# Collaborators/outside sources used 
# (IMPORTANT! Write "NONE" if none were used):
# From Lecture 16 with the matplotlib
# https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot
#
# Reminder: you are to write your own code.
# ******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math

file = open("surveydata.txt", "r")
userx = float(input("Enter Your X coordinate"))
usery = float(input("Enter Your Y coordinate"))


class Resident:

    def __init__(self, x, y, drink):
        self.x = float(x)
        self.y = float(y)
        self.drink = drink  # return coke or pepsi

    def distance(self):
        dis = math.sqrt((userx - self.x) ** 2 + (usery - self.y) ** 2)
        return dis


def main():
    count = {"Pepsi": 0, "Coke": 0}
    for lines in file:
        alist = lines.split()
        a = Resident(alist[0], alist[1], alist[2])
        if a.distance() <= 1:
            count[a.drink] += 1
    print(count)


main()

###Challenge###
import matplotlib.pyplot as plt


def main2():
    file = open("surveydata.txt", "r")
    fig, ax = plt.subplots()
    for resident in file:
        alist = resident.split()
        a = Resident(alist[0], alist[1], alist[2])
        if a.drink == "Coke":
            plt.scatter(a.x, a.y, marker="o", color="r")
        elif a.drink == "Pepsi":
            plt.scatter(a.x, a.y, marker="o", color="b")
    ax.plot(0, 0, marker="o", color="r", label='Coke')
    ax.plot(0, 0, marker="o", color="b", label='Pepsi')
    plt.scatter(userx, usery, s=100, marker='x')  # want the x to be big so can be seen more clearly
    cir = plt.Circle((userx, usery), 1, color='y', fill=False, clip_on=False)
    ax.legend()
    ax.add_artist(cir)
    plt.show()


main2()
