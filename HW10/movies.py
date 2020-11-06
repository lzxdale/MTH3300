#******************************************************************************
# movies.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://docs.python.org/2/library/sqlite3.html
#http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import sqlite3

film_conn = sqlite3.connect("film_permits.db")
film_curs = film_conn.cursor()
typ = ('Shooting Permit', )

Month = input("Enter a Month: ")
Year = input("Enter a Year: ")

film_curs.execute("SELECT Month, Year, EventType, ZipCode FROM Permits WHERE Month=? AND Year=? AND EventType =?;", (Month, Year, 'Shooting Permit', ))
film = film_curs.fetchall()

Zip = {}
for row in film:
    zipcode = row[-1].split()
    for i in zipcode:
        try:
            Zip[i] += 1
        except: #the element is not created, thus assign it to one
            Zip[i] = 1

maxx = 0        
for code in Zip:
    if Zip[code] > maxx:
        maxx = Zip[code]
        bigg = code
        
print("The highest is in",bigg, "with number", Zip[bigg])

film_conn.close()