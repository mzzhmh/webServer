#!/usr/bin/python3.6

from lxml import html
import requests
from lxml import etree
import mysql.connector
import math
import sys

def changeToDBdate(webDate):
    #print(webDate)
    month=webDate.split(' ')[1]
    if month == 'Jan':  
         monthString = "01"
    elif month == 'Feb':  
         monthString = "02"
    elif month == 'Mar':  
         monthString = "03"
    elif month == 'Apr':  
         monthString = "04"
    elif month == 'May':  
         monthString = "05"
    elif month == 'Jun':  
         monthString = "06"
    elif month == 'Jul':  
         monthString = "07"
    elif month == 'Aug':  
         monthString = "08"
    elif month == 'Sept': 
         monthString = "09"
    elif month == 'Oct': 
         monthString = "10"
    elif month == 'Nov': 
         monthString = "11"
    elif month == 'Dec': 
         monthString = "12"
    else:
         monthString = "00"
    return webDate.split(' ')[0]+"/"+monthString

def scrapNewCase(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    #print(tree)
    node = tree.find('.//*[@id="content"]/div/div/section/table')
    latest = node[1]
    strList = list(latest.itertext())
    print(strList)
    date = changeToDBdate(strList[0])
    new = strList[-1].replace(',','')
    total = strList[1].replace(',','')
    if (new == '-'):
	    new = 'NULL'
    if (total == '-'):
	    total = 'NULL'
    return (date,new,total)

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


#scrap the nsw new and total cases
try:
    page = requests.get('http://covidlive.com.au/report/daily-cases/nsw')
    tree = html.fromstring(page.content)
    #print(tree)
    node = tree.find('.//*[@id="content"]/div/div/section/table')
    #print(etree.tostring(node,pretty_print=True))
    #print(etree.tostring(node[-1]))
    #for a in node:
    #    print(a)
    #get the latest data
    latest = node[1]
    strList = list(latest.itertext())
    #print(strList)
    #1:date,2:total case,3:increase/decrease,4:dailyNewCase,5:rate
    date = changeToDBdate(strList[0])
    totalCase = strList[1].replace(',','')
    if ((totalCase)=='-'):
	    totalCase = 'NULL'
    newCase = strList[-1].replace(',','')
    if ((newCase)=='-'):
            newCase = 'NULL'

    print("======New Case=====")
    print(date)
    print(totalCase)
    print(newCase)
    print("===================")
except Exception as e:
    print(str(e))


#scrap the nsw tested case totol and daily
try:
    page2 = requests.get('http://covidlive.com.au/report/daily-tests/nsw')
    tree2 = html.fromstring(page2.content)
    #print(tree)
    node2 = tree2.find('.//*[@id="content"]/div/div/section/table')
    #print(etree.tostring(node2,pretty_print=True))
    #print(etree.tostring(node2[-1]))
    #for a in node2:
    #    print(a)
    #get the latest data
    latest2 = node2[1]
    strList2 = list(latest2.itertext())
    #print(strList2)
    date2 = changeToDBdate(strList2[0])
    #a.replace(',', '')
    totalTestCase = strList2[1].replace(',','')
    if ((totalTestCase)=='-'):
	    totalTestCase = 'NULL'
    newTestCase = strList2[-1].replace(',','')
    if ((newTestCase)=='-'):
	    newTestCase = 'NULL'
    print("=====Tested========")
    print(date2)
    print(totalTestCase)
    print(newTestCase)
    print("===================")
except Exception as e2:
    print(str(e2))

#scrap total death
try:
    page3 = requests.get('http://covidlive.com.au/report/daily-deaths/nsw')
    tree3 = html.fromstring(page3.content)
    #print(tree)
    node3 = tree3.find('.//*[@id="content"]/div/div/section/table')
    #get the latest data
    latest3 = node3[1]
    strList3 = list(latest3.itertext())
    #print(strList3)
    date3 = changeToDBdate(strList3[0])
    newDeath = strList3[1].replace(',','')
    if ((newDeath)=='-'):
	    newDeath = 'NULL'
    print("=======Death=======")
    print(date3)
    print(newDeath)
    print("===================")
except Exception as e3:
    print(str(e3))

#scrap community infect
try:
    page4 = requests.get('http://covidlive.com.au/report/daily-community-transmission/nsw')
    tree4 = html.fromstring(page4.content)
    #print(tree4)
    node4 = tree4.find('.//*[@id="content"]/div/div/section/table')
    #get the latest data
    latest4 = node4[1]
    strList4 = list(latest4.itertext())
    #print(strList4)
    date4 = changeToDBdate(strList4[0])
    newInfect = strList4[-1].replace(',','')
    if ((newInfect)=='-'):
        newInfect = 'NULL'
    print("=======newInfect=======")
    print(date4)
    print(newInfect)
    print("===================")
except Exception as e4:
    print(str(e4))
   
NSWrecovery = scrapNewCase('http://covidlive.com.au/report/daily-recoveries/nsw')
NSWrec = NSWrecovery[2]
print("=======NSW Recovery=======")
print(NSWrec)
print("===================")

NSWactive = scrapNewCase('http://covidlive.com.au/report/daily-active-cases/nsw')
NSWact = NSWactive[2]
print("=======NSW Active Case=======")
print(NSWact)
print("===================")


#insert of update the db records
if (date != date2) or (date != date3) or (date2 != date3):
    print("Record Date not equal, so wait until next schedule.")
    sys.exit(1)

try:
    cnx = mysql.connector.connect(user=dbuser, password=dbpw,
                              host=dbhost,
                              database=dbase)
    #get the last (latest record)
    csor = cnx.cursor()
    query1='select * from covid19.NSWCase order by id desc limit 1'
    #query1='select * from covid19.NSWCase'
    csor.execute(query1)
    rows = csor.fetchall()
    #1:idx,2:date,3:newCase,4:newTest,5:totalCase,6:totalTest,7:Death
    dbDate = rows[0][1]
    dbId = int(rows[0][0])
    print("DB latest:"+dbDate)
    print("DB Id:"+str(dbId))

    #insert new data if there is a new date than dbDate
    if (dbDate != date):
        print("Inserting new records........")
        insertQ="insert into covid19.NSWCase (Id,Date,NewCase,TestedCase,TotalCase,TotalTestedCase,TotalDeath,CommunityInfect,Recovery,Active) values (%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s)" % (str(dbId+1),date,newCase,newTestCase,totalCase,totalTestCase,newDeath,newInfect,NSWrec,NSWact)
        print(insertQ)
        csor.execute(insertQ)
        cnx.commit()
        csor.close()
        cnx.close()
    else:
        print("Updating latest DB record........")
        updateQ="update covid19.NSWCase set NewCase=%s,TestedCase=%s,TotalCase=%s,TotalTestedCase=%s,TotalDeath=%s,CommunityInfect=%s,Recovery=%s,Active=%s where Date='%s'" % (newCase,newTestCase,totalCase,totalTestCase,newDeath,newInfect,NSWrec,NSWact,date)
        print(updateQ)
        csor.execute(updateQ)
        cnx.commit()
        csor.close()
        cnx.close()
except Exception as sqlE:
    print(str(sqlE))



#scraping other States and National data
try:
    #QLD
    QLD = scrapNewCase('http://covidlive.com.au/report/daily-cases/qld')
    QLDdate = QLD[0]
    QLDnew = QLD[1]
    #SA
    SA = scrapNewCase('http://covidlive.com.au/report/daily-cases/sa')
    SAdate = SA[0]
    SAnew = SA[1]
    #VIC
    VIC = scrapNewCase('http://covidlive.com.au/report/daily-cases/vic')
    VICdate = VIC[0]
    VICnew = VIC[1]
    #WA
    WA = scrapNewCase('http://covidlive.com.au/report/daily-cases/wa')
    WAdate = WA[0]
    WAnew = WA[1]
    #TAS
    TAS = scrapNewCase('http://covidlive.com.au/report/daily-cases/tas')
    TASdate = TAS[0]
    TASnew = TAS[1]
    #NT
    NT = scrapNewCase('http://covidlive.com.au/report/daily-cases/nt')
    NTdate = NT[0]
    NTnew = NT[1]
    #ACT
    ACT = scrapNewCase('http://covidlive.com.au/report/daily-cases/act')
    ACTdate = ACT[0]
    ACTnew = ACT[1]
    #AU
    AUS = scrapNewCase('http://covidlive.com.au/report/daily-cases/aus')
    AUSdate = AUS[0]
    AUSnew = AUS[1]
    #AUtotal
    AUStotal = AUS[2]
    if((QLDdate == date) and (QLDdate == SAdate) and (SAdate == VICdate) and (VICdate == WAdate) and (WAdate == TASdate) and (TASdate == NTdate) and (NTdate == ACTdate) and (ACTdate == AUSdate)):
        print('===============State Cases %s ============='% (QLDdate))
        print('NSW:%s' % (newCase))
        print('NSW Recovery:%s' % (NSWrec))
        print('QLD:%s' % (QLDnew))
        print('SA:%s' % (SAnew))
        print('VIC:%s' % (VICnew))
        print('WA:%s' % (WAnew))
        print('TAS:%s' % (TASnew))
        print('NT:%s' % (NTnew))
        print('ACT:%s' % (ACTnew))
        print('AUS:%s' % (AUSnew))
        print('AUS TOTAL:%s' % (AUStotal))
        print('============================================')

        #add or update the AUnewCase table
        cnx2 = mysql.connector.connect(user=dbuser, password=dbpw,
                              host=dbhost,
                              database=dbase)
        #get the last (latest record)
        csor2 = cnx2.cursor()
        query21='select * from covid19.AUnewCase order by id desc limit 1'
        #query21='select * from covid19.NSWCase'
        csor2.execute(query21)
        rows2 = csor2.fetchall()
        #1:idx,2:date,3:newCase,4:newTest,5:totalCase,6:totalTest,7:Death
        dbDate2 = rows2[0][1]
        dbId2 = int(rows2[0][0])
        print("DB2 latest:"+dbDate2)
        print("DB2 Id:"+str(dbId2))

        #insert new data if there is a new date than dbDate
        if (dbDate2 != date):
            print("Inserting new records........")
            insertQ2="insert into covid19.AUnewCase (Id,Date,NSW,QLD,SA,VIC,WA,TAS,NT,ACT,AU,AUtotal) values (%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (str(dbId2+1),date,newCase,QLDnew,SAnew,VICnew,WAnew,TASnew,NTnew,ACTnew,AUSnew,AUStotal)
            print(insertQ2)
            csor2.execute(insertQ2)
            cnx2.commit()
            csor2.close()
            cnx2.close()
        else:
            print("Updating latest DB record........")
            updateQ2="update covid19.AUnewCase set NSW=%s,QLD=%s,SA=%s,VIC=%s,WA=%s,TAS=%s,NT=%s,ACT=%s,AU=%s,AUtotal=%s where Date='%s'" % (newCase,QLDnew,SAnew,VICnew,WAnew,TASnew,NTnew,ACTnew,AUSnew,AUStotal,date)
            print(updateQ2)
            csor2.execute(updateQ2)
            cnx2.commit()
            csor2.close()
            cnx2.close()
    else:
        print('Date of each State are NOT the same! so quit game!')
        sys.exit(1)
except Exception as scrapE:
    print(str(scrapE))







