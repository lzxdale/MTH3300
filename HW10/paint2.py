#******************************************************************************
# paint2.py
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
import copy
inter = open("intervals.txt", 'r')
val = []
for i in inter:
    coor = i.split('\n')
    val.append(coor[0])
interval = []
for i in val:
    a = i.split(',')
    coor1 = ''
    coor2 = ''
    for k in a[0]:
        if k != '[':
            coor1 += k
    for k1 in a[1]:
        if k1 != ']':
            coor2 += k1
    interval.append([float(coor1), float(coor2)])

copylist = copy.deepcopy(interval)
newlist = []
while True: # rank the first range in order
    minn = 1000
    if copylist == []:
        break
    for index, j in enumerate(copylist):
        if j[0] < minn:
            minn = j[0]
            smallest = j
    copylist.remove(smallest)
    newlist.append(smallest)

class paint:

    def __init__(self):
        self.distance = 0
        self.coors = []

    def combine(self, item): # this will return the distance between two list EX[1.9938, 9.2224], [12.4618, 16.3501]
        undone = True
        n = 0
        #print(self.coors)
        while undone:
            n +=1
            for index, i in enumerate(self.coors):
                if item[0] > i[0] and item[1] < i[1]: #the new coors is inside the old ones b--a--a--b
                    #print('inside')
                    undone = False
                    break
                elif item[0] < i[0] and item[1] > i[1]: #a--b--b--a
                    #print('a--b--b--a')
                    self.coors[index] = [item[0],item[1]]
                    undone = False
                    break
                elif item[0] < i[0] and i[0] < item[1] < i[1]: #a--b--a--b
                    #print('a--b--a--b')
                    self.coors[index] = [item[0],i[1]]
                    undone = False
                    break
                elif i[1] > item[0] > i[0] and item[1] > i[1]: #b--a--b--a
                    #print('b--a--b--a')
                    self.coors[index] = [i[0], item[1]]
                    undone = False
                    break
            if undone == True:
                #print('append')
                self.coors.append(item) #it is outside all of the coors
                undone = False

    def distance(self):
        diss = 0
        for item in self.coors:
            #print(item)
            diss += abs(item[0]-item[1])
        return diss


    def add(self, item):
        if self.coors == []: # the begining points
            self.coors.append(item)
            self.distance = abs(item[0]-item[1])
        else:
            self.combine(item) # see if the item inside or cross any list



totaldiss = paint()
for item in newlist:
    totaldiss.add(item)
diss = 0
for item in totaldiss.coors:
    #print(item)
    diss += abs(item[0]-item[1])
print("Total distance: {:.4f}".format(diss))

