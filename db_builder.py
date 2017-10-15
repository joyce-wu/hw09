'''
Joyce Wu
Softdev1 pd07
HW09-- no treble
2017-10-16
'''

import sqlite3 #enable control of an sqlite database
import csv #facilitates CSV I/O

f = "peeps-and-courses.db"
db = sqlite3.connect(f) #opens if f exists, otherwise create
c = db.cursor() #facilitates db ops

#open csv files
peeps = csv.DictReader(open("peeps.csv"))
courses = csv.DictReader(open("courses.csv"))

#create table for peeps
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(command)
#print "PEEPS" + command +"\n"
#poplating table for peeps
for row in peeps:
    populate = 'INSERT INTO peeps VALUES ("' + row["name"] + '", ' + row["age"] + ", " + row["id"] + ")"
    #print populate
    c.execute(populate)

#create table for courses
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)
#print "\n\n\n\n\n\n\n COURSES" + command + "\n"
#populating table for courses
for row in courses:
    populate = 'INSERT INTO courses VALUES ("' + row["code"] + '", ' + row["mark"] + ', ' + row["id"] + ")"
    #print populate
    c.execute(populate)

db.commit() #save changes
db.close() #close database
