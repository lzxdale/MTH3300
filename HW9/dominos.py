#******************************************************************************
# dominos.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
#https://stackoverflow.com/questions/17220128/display-a-countdown-for-the-python-sleep-function
#https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#


################################################################################
# This code should be uncommented and run
# after you write __init__ and .dominos()
import random
import time
import sys
import os

class Board:

    def __init__(self):
        self._board = []
        for i in range(6):
            self._board.append(["." for times in range(6)])
        self._numdominos = 0
        # below for the challenge question.
        self._used = []
        self._remain = []
        for i in range(6):
            for x in range(6):
                self._remain.append([i, x])

    def dominos(self):
        return self._numdominos

    def display(self):
        for i in self._board:
            print(i)
            print("")

    def eligible(self,i ,j):
        if 0<= i <= 5 and 0 <= j <= 5 and self._board[i][j] == ".":
            return True
        else:
            return False

    def paint(self,a,b,c,d):
        if self.eligible(a,b) and self.eligible(c,d):
            self._board[a][b] = "P"
            self._board[c][d] = 'P'
            self._numdominos += 1
            self._remain.remove([a,b]) # remove the two points that were used
            self._remain.remove([c,d])
            return True
        else:
            return False


    def random_paint(self):
        for i in range(50): # through testing, 50 times yeilds 0 almost all the time
            if len(self._remain) == 0:
                break
            coor1 = random.choice(self._remain)
            poss = possible(coor1)
            final_poss = []
            for x in poss:
                if x in self._remain:
                    final_poss.append(x)
            if final_poss == []:
                pass
            else:
                coor2 = random.choice(poss) # just using all possible would be close to answer,
                if self.paint(coor1[0],coor1[1],coor2[0],coor2[1]):
                    return True
        return False

''' original methods
    def random_paint(self):
        list = [0, 1, 2, 3, 4, 5]
        for i in range(2000):
            x1 = random.choice(list)
            y1 = random.choice(list)
            x2 = random.choice([x1, x1 - 1, x1 + 1])
            if x2 == x1:
                y2 = random.choice([y1 - 1, y1 + 1])
            else:
                y2 = y1
            if self.paint(x1, y1, x2, y2):
                return True
        return False
'''

def possible(coor):
    poss = [[coor[0] - 1, coor[1]], [coor[0] + 1, coor[1]],
            [coor[0], coor[1] - 1], [coor[0], coor[1] + 1]]
    return poss





################################################################################


b = Board()
print(b.dominos(), " (should print 0)")





################################################################################
# This code should be uncommented and run
# after you write .display()
################################################################################

print("You should see an empty grid below: ")
b.display()




################################################################################
# This code should be uncommented and run
# after you write .eligible()
################################################################################

print(b.eligible(4,2), " (b.eligible(4,2) should be TRUE)")
print(b.eligible(5,0), " (b.eligible(5,0) should be TRUE)")
print(b.eligible(-1,4), " (b.eligible(-1,4) should be FALSE)")
print(b.eligible(3,6), " (b.eligible(3,6) should be FALSE)")




################################################################################
# This code should be uncommented and run
# after you write .paint()
################################################################################
'''
'''

move_one = b.paint(2, 4, 3, 4)
print(move_one, " (move_one should be TRUE)")
b.display()

print(b.eligible(2,4), " (b.eligible(2,4) should now be FALSE)")

move_two = b.paint(5, 0, 5, 1)
print(move_two, " (move_two should be TRUE)")
b.display()

move_three = b.paint(4, 0, 5, 0)
print(move_three, " (move_three should be FALSE)")
b.display()

move_four = b.paint(-1, 5, 0, 5)
print(move_four, " (move_four should be FALSE)")
b.display()









################################################################################
# This code should be uncommented and run
# after you write .random_paint()
################################################################################



print(b.random_paint())
print(b.random_paint())
print(b.random_paint())
print("You should see exactly 10 occupied squares below:")
b.display()


########testing 10000 times

def main(): # about 8-10sec to run, the original method takes about a minuets
    count = 0
    for i in range(10000):
        Find = True
        test = Board()
        while Find:
            Find = test.random_paint()
        if test.dominos() == 18:
            count += 1
    print("Probability of filling the board: {0}%".format(count/100))

main()
print("\n"*3)
print('Below are the game mode')




#####Game######
class Board:

    def __init__(self):
        self._board = []
        for i in range(6):
            self._board.append(["." for times in range(6)])
        self._numdominos = 0
        #below for the challenge question.
        self._used = []
        self._remain = []
        for i in range(6):
            for x in range(6):
                self._remain.append([i, x])

    def dominos(self):
        return self._numdominos

    def display(self):
        for i in self._board:
            print(i)
            print("")

    def eligible(self,i ,j):
        if 0 <= i <= 5 and 0 <= j <= 5 and self._board[i][j] != 'P':
            return True
        else:
            return False

    def paint(self,a,b,c,d):
        if self.eligible(a,b) and self.eligible(c,d):
            self._board[a][b] = "P"
            self._board[c][d] = 'P'
            self._numdominos += 1
            self._remain.remove([a,b])
            self._remain.remove([c,d])
            return True
        else:
            return False

    def userdots(self,a,b,c,d):
        if self.eligible(a,b) and self.eligible(c,d):
            self._board[a][b] = "T"
            self._board[c][d] = "t"
            return True
        else:
            return False

    def random_paint(self):
        for i in range(50):
            if len(self._remain) == 0:
                break
            coor1 = random.choice(self._remain)
            poss = possible(coor1)
            final_poss = []
            for x in poss:
                if x in self._remain:
                    final_poss.append(x)
            if final_poss == []:
                pass
            else:
                coor2 = random.choice(final_poss)
                if coor1==[3,3] or coor2 == [3,2] or coor1 == [3,2] or coor2 == [3,3]: #make sure that the
                    pass
                elif self.paint(coor1[0],coor1[1],coor2[0],coor2[1]):
                    return True
        return False

    def clean(self,a,b):
        if self._board[a][b] != '.' and 'P':
            self._board[a][b] = "."
            self._remain.append([a, b])
            return True

    def move(self,T1, T2, order):
        if order in ['a','w','s','d','q','e']:
            NT, Nt = turn(T1, T2, order) #new T and new t
            print(NT,Nt)
            print(self.eligible(NT[0], NT[1]))
            print(self.eligible(Nt[0],Nt[1]))
            if self.eligible(NT[0], NT[1]) and self.eligible(Nt[0],Nt[1]):
                if abs(NT[0]+NT[1]-Nt[0]-Nt[1]) == 1:
                    print("excuted")
                    self.clean(T1[0], T1[1]) #clean original position to prepared for new position
                    self.clean(T2[0], T2[1])
                    self.userdots(NT[0], NT[1], Nt[0],Nt[1])
                    return NT, Nt
        return T1, T2
    
    def userpaint(self, T, t):
        self.paint(T[0], T[1], t[0], t[1])
        poss1 = possible(T)
        poss2 = possible(t)
        Tposs = []
        tposs = []
        if (tposs and Tposs) == None:
            return "game", "over" #game over, there are no wher to go
        for i in poss1:
            if self.eligible(i[0],i[1]):
                Tposs.append(i)
        for x in poss2:
            if self.eligible(x[0],x[1]):
                tposs.append(x)
        combo = connected(Tposs,tposs)
        if combo != []:
            newpoints = random.choice(combo)
            T = newpoints[0]
            t = newpoints[1]
            self.userdots(T[0], T[1], t[0], t[1])
            return T, t
        #there are not points connect to both of them
        if Tposs != []: # first look toward T
            P_P=[]
            for k in Tposs:
                poss_p = []
                plist = possible(k)
                for j in plist:
                    if self.eligible(j[0],j[1]):
                        poss_p.append(j)
                if poss_p != []:
                    P_P.append([k,poss_p]) #all possible points
            if P_P != []:
                selcted = random.choice(P_P)
                T = selcted[0]
                t = random.choice(selcted[1])
                self.userdots(T[0], T[1], t[0], t[1])
                return T, t
        if tposs != []: # Then look toward t
            P_P=[]
            for k in tposs:
                poss_p = []
                plist = possible(k)
                for j in plist:
                    if self.eligible(j[0],j[1]):
                        poss_p.append(j)
                if poss_p != []:
                    P_P.append([k,poss_p]) #all possible points
            if P_P != []:
                selcted = random.choice(P_P)
                t = selcted[0]
                T = random.choice(selcted[1])
                self.userdots(T[0], T[1], t[0], t[1])
                return T, t
        return "game", "over" #game over, there are no wher to go

def connected(p1list, p2list):
    combo = []
    for p1 in p1list:
        for p2 in p2list:
            if p2 in possible(p1):  # they are connected:
                combo.append([p1, p2])
    return combo

class WrongInput(Exception):
    pass

def rule():
    print("Rules: try to fill the board with the given constrain")
    print("T on the chart meaning ur points position, they are just temporary, not stored")
    print("Enter 'q' turn 90 degree counter clockwise, Enter 'e' turn in clockwise")
    print("Enter 'w' move up, 's' move down, 'a' move left, 'd' move right")
    print("'T' and 't' position cannot cross 'P', plan carefully")
    print("Press Enter to place dots, and it will return to its previous position which no cross")
    print("HINT! make sure there is a empty dominons position next before you enter, so there is a place for 'T''t' to go")
    print("To quit the game, enter 'quit'")
    print("\n"*2)
    print(":( sometime it is impossible to win, simply type restart to get a workable map")
    #Still trying to figure out a pattern which avoid two dominons sealed a place.
    print()

def turn(T1,T2, order):
    if order == "q":
        if T1[0] == T2[0]: #on the same row
            if T1[1] < T2[1]:
                T4 = [T1[0]-1, T1[1]]
            elif T1[1] > T2[1]:
                T4 = [T1[0]+1, T1[1]]
            return T1, T4
        else: #on the same column
            if T1[0] > T2[0]:
                T4 = [T1[0], T1[1]-1]
            elif T1[0] < T2[0]:
                T4 = [T1[0], T1[1]+1]
            return T1, T4
    elif order == "e":
        if T1[0] == T2[0]: #on the same row
            if T1[1] < T2[1]:
                T4 = [T1[0]+1, T1[1]]
            elif T1[1] > T2[1]:
                T4 = [T1[0]-1, T1[1]]
            return T1, T4
        else: #on the same column
            if T1[0] > T2[0]:
                T4 = [T1[0], T1[1]+1]
            elif T1[0] < T2[0]:
                T4 = [T1[0], T1[1]-1]
            return T1, T4
    elif order == 's':
        T3 = [T1[0]+1, T1[1]]
        T4 = [T2[0]+1, T2[1]]
    elif order == 'w':
        T3 = [T1[0] - 1, T1[1]]
        T4 = [T2[0] - 1, T2[1]]
    elif order == 'a':
        T3 = [T1[0], T1[1]-1]
        T4 = [T2[0], T2[1]-1]
    elif order == 'd':
        T3 = [T1[0], T1[1]+1]
        T4 = [T2[0], T2[1]+1]
    return T3, T4

def countdown(): #from online source
    for i in [5,4,3,2,1]:
        print(i, end=" ")
        sys.stdout.flush()
        time.sleep(1)

def main2():
    os.system('cls')  # to clean the screen
    rule()
    Playing = True
    countdown()
    print("Begin")
    while Playing:
        play = Board()
        T = [3, 3]
        t = [3, 2]
        play.userdots(T[0], T[1], t[0], t[1])
        try:
            print("1:Essay, 2:Medium, 3:Hard")
            level = int(input("Enter: "))
        except ValueError:
            print("Plz only enter 1 or 2 or 3")
            break
        except NameError:
            print("Plz only enter 1 or 2 or 3")
            break
        if level not in [1,2,3]:
            print("Plz only enter 1 or 2 or 3")
            break
        for i in range(level):
            play.random_paint()
        play.display()
        while True:
            action = input("Enter:")
            if action == "quit":
                Playing = False
                break
            elif action == "restart":
                break
            T, t = play.move(T,t,action)
            if action == "":
                T, t = play.userpaint(T,t)
            print()
            play.display()
            if play.dominos() == 18:
                print("You Win! another one?")
                action = input("Enter restart/quit")
            elif T == "game":
                print('Game over, you are trapped!!!')
                print('restarting')
                countdown()
                print()
                break

Toplay = input("Want to play a game? y/n ")
if Toplay == 'y':
    main2()

