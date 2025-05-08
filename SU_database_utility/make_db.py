#This script is heavily commented to make it easier for a student to use. If you have any problems please contact the professor of one of the TA's for assistance.
#Please read all comments before editing this script and if you do not understand what something does or how to adapt it for your use case please contact the professor or a TA

#import statements lets the program have access to functionality that it doesn't always have.
import sqlite3 as sql #the "as" command in python renames the import so it can be called by whatever name the programer choses
from os import path
from sre_constants import SUCCESS #this path utility might be necessary for the student to make sure their database is saved in the proper location but it is not currently in use
from  util import build_complete 

db_path = r"dataBase.db" #put the path to your database followed by /name-of-database.db in this string for example C:/test-folder/example.db
#the lower case r next to this string turns it into a string literal which means it will ignore escape characters. So, no need for double backslashes or anything of that nature

#creates a connection to the database and creates the database if it does not already exist
connection = sql.Connection(db_path)

#the cursor object is used to send commands to your database
cursor = connection.cursor()

#I'm using a video game ordering service for the example database so the tables will be for the games that I sell, orders placed and my customers
#these are the names of the tables in the database. The words on the right of the equals sign are the name of the variable and the words in quotes on the left of the equals sign are what that variable represents.
TABLE_ONE_NAME = "movies" #name of the table you wish to create
TABLE_TWO_NAME = "customers" #since the names of the tables are constants they are all capitalized and separated by underscores
TABLE_THREE_NAME = "comics"
TABLE_FOUR_NAME = "books" 
table_names = (TABLE_ONE_NAME, TABLE_TWO_NAME, TABLE_THREE_NAME, TABLE_FOUR_NAME) #put the names of all of your tables in this list. 
#You can either type them out in quotes or declare them as constants like I did above. it is considered best practice to declare them as constants


#here you create lists that contain the schema for your tables
#the first word in each element of the schema list is the name of the table element
#the second word in each of the elements of your schema list is the data type held by that field
table_one_schema = ("movieName text", "genre text", "director text", "releaseYear integer") #the naming convention for your table names is that all words are lower case and that words are separated by an underscore.
table_two_schema = ("customerID text", "firstName text", "lastName text")#each table will have its own schema
table_three_schema = ("comicName text", "genre text", "author text", "releaseYear integer")#remember to keep the names of the variables that hold your tables and their corresponding tables consistent
table_four_schema = ("bookName text", "genre text", "author text", "releaseYear integer")

#this is a f-string that will be used to create your database
# the basics of f-strings: https://youtube.com/shorts/rBamvYwO3gg?feature=share
schema_string_table_one = f"create table {TABLE_ONE_NAME} ({table_one_schema[0]} , {table_one_schema[1]} , {table_one_schema[2]}, {table_one_schema[3]})"#each element of your schema should be called here inside brackets and separated by commas. Here there are three elements and we start counting at 0
schema_string_table_two = f"create table {TABLE_TWO_NAME} ({table_two_schema[0]}, {table_two_schema[1]}, {table_two_schema[2]})"#here here are four elements
schema_string_table_three = f"create table {TABLE_THREE_NAME} ({table_three_schema[0]}, {table_three_schema[1]}, {table_three_schema[2]}, {table_three_schema[3]})"#three elements again and remember to start counting at 0
schema_string_table_four = f"create table {TABLE_FOUR_NAME} ({table_four_schema[0]}, {table_four_schema[1]}, {table_four_schema[2]}, {table_four_schema[3]})"
#a list to store all of the schemas
table_schemas = (schema_string_table_one, schema_string_table_two, schema_string_table_three, schema_string_table_four)

#this is where you will set up the data to be stored in your database
table_one = [#this is a tuple, tuples are immutable and can be passed as an argument in sqlite to create or edit a table
    ("Oblivion", "Sci-Fi", "Joseph Kosinski" , 2013),
    ("Valerian and the City of a Thousand Planets", "Sci-Fi", "Luc Besson" , 2017),
    ("The Suicide Squad", "Action", "James Gunn" , 2021)
]

table_two = [#remember to keep track of which table is which and its corresponding name, schema and elements
    ("1234JD", "John", "Doe"),
    ("4321jd", "Jane", "Doe"),
    ("135JB", "Jim", "Bob")
]

table_three = [
    ("Spider-Man", "Sci-Fi", "Stan Lee" , 1962),
    ("Batman", "Sci-Fi", "Bob Kane" , 1939),
    ("Superman", "Sci-Fi", "Jerry Siegel" , 1938)
]

table_four = [
    ("Eragon", "Fantasy Fiction", "Christopher Paolini", 2002),
    ("Harry Potter", "Fantasy Fiction", "J. K. Rowling", 1997),
    ("Ranger's Apprentice", "Sci-Fi", "John Flanagan", 2004)
]

tables = [(table_one), (table_two), (table_three), (table_four)]


if __name__ == '__main__':#this is the code that will execute when you run the program. There is no reason to change anything after this point.

    for i in range(0,len(table_schemas)): #this loops through your schemas and uses them to create new tables in your database
        cursor.execute(table_schemas[i]) #this command creates the individual tables 
    
    for i in range(0,len(table_names)): #this takes the values you put into your tables and adds their values into the database table
        insert = (("?, ")*len(tables[i][0])) #in order to populate the tables with data there needs to be a number of question marks 
        insert = insert[:-2]
        cursor.executemany(f"insert into {table_names[i]} values ({insert})", tables[i])

    build_complete.confirm()
    #saves your database
    connection.commit()