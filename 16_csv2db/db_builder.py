#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
debug = False
#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

#code to read in roster info

def readFile(file):
    # returns file as a dictionary seperated by rows
    return csv.DictReader(open(file))

#all dicts will have the same headers since both csv files have the same headers
def dict2SQ(dict, dict_name):
    dict_headers = " (name TEXT, num0 INTEGER, num1 INTEGER)"
    c.execute("CREATE TABLE IF NOT EXISTS " + dict_name + dict_headers)

    dict_loop = dict.fieldnames
    for item in dict:
        item_string = "('" + item[dict_loop[0]] + "'," + \
            item[dict_loop[1]] + "," + item[dict_loop[2]] + ")"
        c.execute("INSERT INTO roster VALUES "+item_string+";")
        if debug:
            print(item_string)
    
    db.commit()

    
    # for item in dict:
    #     item_string = "('" + dict[item][dict_loop[0]] + "', " 
    #     + dict[item][dict_loop][1]+ "," + dict[item][dict_loop][2] +")"
    #     if debug:
    #         print(item_string)
        #c.execute("INSERT INTO roster VALUES ('whose-it', 2);")
        
    #c.execute("CREATE TABLE [IF NOT EXISTS] " + dict_name + dict_headers)
    db.commit()

def printDictioanry(dic):
    for row in dic:
        print(", ".join(row))




command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

if __name__ == "__main__":
    rosterDict = readFile('students.csv')
    dict2SQ(rosterDict, "roster")
    db.commit()  # save changes
    rows = c.fetchall()
    for i in range(len(rows)):
        print(rows[i])
    db.close()  # close database
    
    



