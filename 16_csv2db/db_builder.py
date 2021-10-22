#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#print statements trigger based on debug
debug = False
#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

#code to read in roster info

def readFile(file):
    '''
    returns file as a dictionary seperated by rows
    '''
    return csv.DictReader(open(file))

#all dicts will have the same headers since both csv files have the same headers
def dict2SQ(dict, dict_name):
    '''
    converts a CSV dictinoary to an sqlite table
    '''

    #headers variable types are the same for both csv files
    dict_headers = " (name TEXT, num0 INTEGER, num1 INTEGER)"
    c.execute("CREATE TABLE IF NOT EXISTS " + dict_name + dict_headers)

    #csv header returned by .fieldnames
    dict_loop = dict.fieldnames

    #loop through items and add them to the table; set debug to true to view the string of items added
    for item in dict:
        item_string = "('" + item[dict_loop[0]] + "'," + \
            item[dict_loop[1]] + "," + item[dict_loop[2]] + ")"
        c.execute("INSERT INTO "+ dict_name +" VALUES "+item_string+";")
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

def printDictioanry(dic):
    '''
    prints header of each item in dictionary - turned out to be less useful than intended
    '''
    for row in dic:
        print(", ".join(row))


def printDB(tableName):
    '''
    prints the sqliteDB given tablename to select it
    '''

    #holds the info from SELECT in the curson and then fetches it, placing it into rows
    c.execute("SELECT * FROM " + tableName)
    rows = c.fetchall()

    #print each item in rows
    for item in rows:
        print(item)


#source: https://www.sqlitetutorial.net/sqlite-exists/
def dbExistence(tableName):
    '''
    returns boolean based on whether or not the given tableName exists
    '''

    #holds data on existence of tableName
    c.execute("SELECT EXISTS(SELECT * FROM '"+tableName+"')")

    #output of EXISTS is 0 or 1; converts value of exists output into bool
    exists = c.fetchone()[0]
    exists = exists == 1
    return(exists)

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

if __name__ == "__main__":
    #runs if not imported

    rosterDict = readFile('students.csv')
    #dict2SQ(rosterDict, "roster")
    #db.commit()  # save changes
    printDB("roster")
    print(dbExistence('roster'))
    # coursesDict = readFile('courses.csv')
    # dict2SQ(coursesDict, "courses")
    # db.commit()  # save changes
    # printDB("courses")
    db.close()  # close database
    
    



