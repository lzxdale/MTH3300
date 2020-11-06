#******************************************************************************
# scrabble.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used
#(IMPORTANT! Write "NONE" if none were used):
#https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# For challenge part
# This is quite hard as I was going though a wrong approach in the beginning
# first I tried to get all possible combination of letter, which is 7! Then I found it unwork after spending quite some hours
# spend some time in figuring out delete items in dictionary by .pop (which is not need at all!)
# Then I realize! I can keep doing reducation untill all the word fit, and find one word with max value.
# The end
# Takes a long time to run! SOOOOO many loop
################################################################################
#
# POINTS
#
################################################################################
points = {"a":1,
          "b":3,
          "c":3,
          "d":2,
          "e":1,
          "f":4,
          "g":2,
          "h":4,
          "i":1,
          "j":8,
          "k":5,
          "l":1,
          "m":3,
          "n":1,
          "o":1,
          "p":3,
          "q":10,
          "r":1,
          "s":1,
          "t":1,
          "u":1,
          "v":4,
          "w":4,
          "x":8,
          "y":4,
          "z":10}

file = open("words_eng.txt","r")
wordic = {} # will store all word with correrpond value
wordlist = file.read().split()
for i in wordlist:
    sum = 0
    for x in range(len(i)):
        sum += points[i[x]]
    wordic[i] = sum
highest = 0
#max(wordic) work differently
for i in wordic:
    if wordic[i] > highest:
        highest = wordic[i]
        highword = i
print(highword)
file.close()

#####Challenge#####
word = input("Please enter a word")
#word = input("Enter a 7 letter word in lower case")
letterlist = {} #have a list that contain the user input, symbol one by one and their value.
usersum = 0
for i in range(7):
    usersum += points[word[i]]
    letterlist[word[i]] = points[word[i]]
#https://stackoverflow.com/questions/5447494/remove-an-item-from-a-dictionary-when-its-key-is-unknown

def getletternum(word):
    letternum = {}
    for i in word:
        letternum[i] = 0
    for i in word:
        letternum[i] += 1
    return letternum
letternum = getletternum(word)


#https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list
#need to use deep copy without interfare the list
from copy import deepcopy


def reduce(word):
    allletters = "abcdefghijklmnopqrstuvwxyz"
    restletters = []
    for i in allletters:
        restletters.append(i)
    for alphabet in word:
        if alphabet in restletters:
            restletters.remove(alphabet)
    return restletters

letters_not_in = reduce(word)

def cleaning():
    newlist = deepcopy(wordlist)
    #print(letters_not_in)
    for ab in range(20):#each loop reduce the error by a half, by 20 which means 2^20 and is large enough > len(file)
        for aword in newlist:
            for alph in letters_not_in:
                if alph in aword: #we need to delete this word as the alphbat didnt appear in the userinput at all
                    newlist.remove(aword)
                    break
    return newlist

newlist = cleaning()
#print(len(newlist))

def screening(): #lefting word contain letters less or equal to the user input
    newform = []
    leftedword = []
    for i in (newlist): # get remaing words and there letters combo
        newform.append([getletternum(i), i])
    #print(newform)
    for item in newform:
        remain = True
        for x in word: #loop in userinput word,
            if x in item[0]:
                if letternum[x] < item[0][x]:  #0 return the numbers of each letter. x return the correspond num of letter
                    #print("letter:",x)
                    #print(item)
                    #print(item[0][x])
                    remain = False # if the letter num in word is > userinput, the word is out
            elif x not in item[0]:
                pass
        if (item not in leftedword) and remain:
            leftedword.append(item)
    return leftedword

finallist = screening() #final list contain all words which can fit the users input
#we only need to find the largest word in the final list.


def challenge():
    maxx = 0
    biggest = "a"
    for word in finallist:
        sums = 0
        for letters in word[1]: #word[1] will return the "word"
            sums += points[letters]
        if sums > maxx:
            maxx = sums
            biggest = word
    print("The word is", biggest[1], " with points:",maxx) #there might be more than one word have the same value, can create a list to print all of them

challenge()
