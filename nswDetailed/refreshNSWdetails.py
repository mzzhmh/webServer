#!/usr/bin/python3.6

#call nsw covid statistical data api to get the latest records and put them into the database

from lxml import html
import requests
from lxml import etree
import mysql.connector
import math
import sys
import os
import json


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


print("\n===============================================================")
#get local db num
try:
    cnx = mysql.connector.connect(user=dbuser, password=dbpw,host=dbhost,database=dbase)
    csor = cnx.cursor()
    query = 'select count(*) from nswPostcode;'
    csor.execute(query)
    rows = csor.fetchall()
    dbNum = int(rows[0][0])
    print("[DB]:"+str(dbNum))
except Exception as sqlE:
    print(str(sqlE))

#get nsw stat number from web
totURL='https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=21304414-1ff1-4243-a5d2-f52778048b29&limit=0'
JSONtotNum = requests.get(totURL,verify=False,timeout=30)
if (JSONtotNum.status_code == 200):
    jsonData = json.loads(JSONtotNum.text)
    webNum = jsonData["result"]["total"]
    print("[RES]:"+str(webNum))
else:
    print("[ERR]:"+JSONtotNum.text)

#how many to get
offset = webNum - dbNum
if offset <= 0:
    print("DB ahead, wait.....")
    sys.exit(1)
else:
    newCasesURL='https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=21304414-1ff1-4243-a5d2-f52778048b29&offset=3780&limit='+str(offset)
    print("[OFFSET]:"+str(offset))
    JSONoffset = requests.get(newCasesURL,verify=False,timeout=30)
    if (JSONoffset.status_code == 200):
        OffsetJSONdata = json.loads(JSONoffset.text)
        records = OffsetJSONdata['result']['records']
        #print(json.dumps(records, indent=4, sort_keys=True))
        
        #put each record into local db
        for entry in records:
            print(entry)
    else:
        print("[ERR]:"+JSONoffset.text)





print("==================================================================")
