#******************************************************************************
# boxchart.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#Rong: make the speed faster
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#



# PLEASE USE THIS VARIABLE NAME!
# (But you way want to change the specific list, to test if your program works
# in general!)
VALUES = [5, 2, 3, 8, 4]
import turtle

mr_t = turtle.Pen()
scr = turtle.Screen()
mr_t.speed(10)
# Here's some starter code, for you to fix.


for boxnum in VALUES:
    for num in range(boxnum):
        mr_t.forward(30) #going right 30
        mr_t.left(90) # turn to up
        mr_t.forward(30 + num*30) #going up depending the numbers of box
        mr_t.left(90) #turn to left
        mr_t.forward(30) #going left for 30
        mr_t.left(90) #turn to down
        mr_t.forward(30 + num*30) #going back to orginal point
        mr_t.left(90) #turn the direction back to right
    mr_t.forward(30) #going to the next begining potin


##challange##
#the pen will end at the last box right bottom corner
mr_t.color('red')
mr_t.pensize(width=3)
mr_t.left(90) #turn to up
mr_t.forward(30*VALUES[-1]) #cover the right exterior
mr_t.left(90)  # turn to left
mr_t.forward(30) #cover the most right top

#https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
value1 = VALUES[::-1] #return the reversed value
for index in range(len(value1)-1):
    mr_t.left(90) #move down
    move = value1[index]-value1[index+1]
    mr_t.forward(30*move)
    mr_t.right(90)#move back to left
    mr_t.forward(30)

mr_t.left(90)
mr_t.forward(30*VALUES[0])
mr_t.left(90)
mr_t.forward(30*len(VALUES))
scr.mainloop()


