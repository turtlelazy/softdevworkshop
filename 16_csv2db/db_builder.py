#The Onions - Tomas Acuna, Lucas Tom-Wong, Ishraq Mahid
#SoftDev
#k16 -- SQLiters and Database Agony
#2021 - 10 - 25
#2.5 hours

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O

#debug statements will print
debug = True
#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

#code to read in roster info

def list_to_string(lst):
    return "(" + ", ".join(lst) + ")"


def append(a, b):
    return a + " " + b


def add_format(value, field_type):
    if field_type == "TEXT":
        return "'" + value + "'"
    return value


def dict2SQ(dict_reader, db, table_name, field_types):
    '''
    converts a CSV dictinoary to an sqlite table
    dict_reader is dictionary
    db is sqlite connection
    table_name is desired name
    field_types are inputted as a parameter
    '''
    c = db.cursor()
    field_names = dict_reader.fieldnames

    headers = map(append, field_names, field_types)
    header_string = list_to_string(headers)
    c.execute("CREATE TABLE IF NOT EXISTS " + table_name + " " + header_string)

    for dic in dict_reader:
        values = map(dic.get, field_names)
        formatted_values = map(add_format, values, field_types)
        value_string = list_to_string(formatted_values)
        c.execute("INSERT INTO " + table_name + " VALUES " + value_string)

    db.commit()

    # for value in dict:
    #     value_string = "('" + dict[value][dict_loop[0]] + "', "
    #     + dict[value][dict_loop][1]+ "," + dict[value][dict_loop][2] +")"
    #     if debug:
    #         print(value_string)
    #c.execute("INSERT INTO roster VALUES ('whose-it', 2);")

    #c.execute("CREATE TABLE [IF NOT EXISTS] " + table_name + table_headers)g


def printDB(db, table_name):
    '''
    prints the sqliteDB given tablename to select it
    db is sqlite connection
    table_name is name of target table
    '''
    if dbExistence(db, table_name):
        c = db.cursor()
        c.execute("SELECT * FROM " + table_name)
        rows = c.fetchall()
        for row in rows:
            print(row)
    else:
        print("table '" + table_name + "' does not exist")


def dbExistence(db, table_name):
    '''
    returns boolean based on whether or not the given tableName exists
    '''
    c = db.cursor()
    c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='" + table_name + "'")
    return(bool(c.fetchone()))
#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

#runs if not imported
if __name__ == "__main__":
    # open if file exists, otherwise create
    discobandit = sqlite3.connect("discobandit.db")

    #opens using target file and runs dict2SQ with chosen parameters
    with open("students.csv") as students:
        roster_reader = csv.DictReader(students)
        dict2SQ(roster_reader, discobandit, "roster",
                ["TEXT", "INTEGER", "INTEGER"])
    with open("courses.csv") as courses:
        gradebook_reader = csv.DictReader(courses)
        dict2SQ(gradebook_reader, discobandit, "gradebook",
                ["TEXT", "INTEGER", "INTEGER"])

    #test statements
    if debug:
        print("roster:")
        printDB(discobandit, "roster")
        print("gradebook:")
        printDB(discobandit, "gradebook")

        print("cheese:")
        printDB(discobandit, "cheese") #should not exist

    discobandit.close()  # close database
