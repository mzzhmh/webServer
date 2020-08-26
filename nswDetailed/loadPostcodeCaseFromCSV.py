#!/usr/bin/python3.6

#read the .csv file line by line and dump the record into the mysql database
#

from lxml import html
import requests
from lxml import etree
import mysql.connector
import math
import sys
import os


dbuser=""
dbpassword=""
dbhost=""
dbase=""
webhost=""
webport=""
conffile=sys.argv[1]
with open(conffile) as f:
    lines = f.readlines()
    dbuser = lines[0].strip().split('=')[1]
    dbpw = lines[1].strip().split('=')[1]
    dbhost = lines[2].strip().split('=')[1]
    dbase = lines[3].strip().split('=')[1]
    webhost = lines[4].strip().split('=')[1]
    webport = lines[5].strip().split('=')[1]

csvfile=sys.argv[2]

bashCMD = "dos2unix "+csvfile

os.system(bashCMD)

try:
    filecsv = open(csvfile, 'r')
    Lines = filecsv.readlines() 
    
    cnx = mysql.connector.connect(user=dbuser, password=dbpw,host=dbhost,database=dbase)
    csor = cnx.cursor()
    for line in Lines:
        date = line.strip().split(',')[0]
        postcode = line.strip().split(',')[1]
        suburb = line.strip().split(',')[3]
        lpg = line.strip().split(',')[5]

        print(date+"|"+postcode+"|"+suburb+"|"+lpg)

        query = "insert into covid19.nswPostcode (date,postcode,suburb,lpg) values ('%s','%s','%s','%s')" % (date,postcode,suburb,lpg)

        print(query)
        csor.execute(query)
        cnx.commit()

    csor.close()
    cnx.close()

except Exception as e:
    print(str(e))


