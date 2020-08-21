from flask import Flask
from flask import render_template, request, jsonify
import indexHTML
import mysql.connector
import json
import sys

app = Flask(__name__)

dbuser=""
dbpassword=""
dbhost=""
dbase=""
webhost=""
webport=""

@app.route('/')
@app.route('/index')
def index():
    #load db information
    try:
        cnx = mysql.connector.connect(user=dbuser, password=dbpw,
        host=dbhost,
        database=dbase)
        #get the last (latest record)
        csor = cnx.cursor()
        query1='select * from covid19.NSWCase order by id DESC limit 20'
        #query1='select * from covid19.NSWCase'
        csor.execute(query1)
        rows = csor.fetchall()
	#1:idx,2:date,3:newCase,4:newTest,5:totalCase,6:totalTest,7:Death,8:New Infect
        csor.close()
        cnx.close()


        cnx2 = mysql.connector.connect(user=dbuser, password=dbpw,
        host=dbhost,
        database=dbase)
        #get the last (latest record)
        csor2 = cnx2.cursor()
        query2='select * from covid19.AUnewCase order by id DESC limit 20'
        #query1='select * from covid19.NSWCase'
        csor2.execute(query2)
        rows2 = csor2.fetchall()
        csor2.close()
        cnx2.close()

    except Exception as sqlE:
        print(str(sqlE))

    #indexInstance = indexHTML.indexHTML()
    #indexInstance.loadNewCase()
    #indexInstance.loadTotalCase()
    #indexInstance.loadNewTest()
    #indexInstance.loadDeath()
    #print("::"+indexInstance.__str__())
    return render_template('index.html', dataFrame=rows, dataFrame2=rows2)

@app.route('/getNSWDailyData')
def getNSWDailyData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,NewCase from covid19.NSWCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	#listData =  [['Jan 13', 1],['Jan 14', 2],['Jan 15', 4],['Jan 16', 8],['Jan 17', 16],['Jan 18', 32],['Jan 19', 64],['Jan 20', 128],['Jan 21', 256],['Jan 22', 111]]
	return (json.dumps(listData))

@app.route('/getNSWRecoveryData')
def getNSWRecoveryData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,Recovery from covid19.NSWCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	#listData =  [['Jan 13', 1],['Jan 14', 2],['Jan 15', 4],['Jan 16', 8],['Jan 17', 16],['Jan 18', 32],['Jan 19', 64],['Jan 20', 128],['Jan 21', 256],['Jan 22', 111]]
	return (json.dumps(listData))

@app.route('/getNSWactiveData')
def getNSWactiveData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,Active from covid19.NSWCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	#listData =  [['Jan 13', 1],['Jan 14', 2],['Jan 15', 4],['Jan 16', 8],['Jan 17', 16],['Jan 18', 32],['Jan 19', 64],['Jan 20', 128],['Jan 21', 256],['Jan 22', 111]]
	return (json.dumps(listData))


@app.route('/getNSWTotalData')
def getNSWTotalData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,TotalCase from covid19.NSWCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	#listData =  [['Jan 13', 1],['Jan 14', 2],['Jan 15', 4],['Jan 16', 8],['Jan 17', 16],['Jan 18', 32],['Jan 19', 64],['Jan 20', 128],['Jan 21', 256],['Jan 22', 111]]
	return (json.dumps(listData))


@app.route('/getNSWTestData')
def getNSWTestData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,TestedCase from covid19.NSWCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	return (json.dumps(listData))

@app.route('/getNSWDeathData')
def getNSWDeathData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,TotalDeath from covid19.NSWCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	return (json.dumps(listData))


@app.route('/getAUDailyData')
def getAUDailyData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,AU from covid19.AUnewCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	return (json.dumps(listData))


@app.route('/getAUTotalData')
def getAUTotalData():
	# Run code or function for taking photo here
	try:
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		query1='select Date,AUtotal from covid19.AUnewCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	return (json.dumps(listData))

@app.route('/getStateData')
def getStateData():
	# Run code or function for taking photo here
	try:
		stName = request.args.get('state')
		if (stName == 'QLD'):
			query1='select Date,QLD from covid19.AUnewCase order by id ASC limit 365;'
		elif (stName == 'SA'):
			query1='select Date,SA from covid19.AUnewCase order by id ASC limit 365;'
		elif (stName == 'VIC'):
			query1='select Date,VIC from covid19.AUnewCase order by id ASC limit 365;'
		elif (stName == 'NT'):
			query1='select Date,NT from covid19.AUnewCase order by id ASC limit 365;'
		elif (stName == 'ACT'):
			query1='select Date,ACT from covid19.AUnewCase order by id ASC limit 365;'
		elif (stName == 'TAS'):
			query1='select Date,TAS from covid19.AUnewCase order by id ASC limit 365;'
		elif (stName == 'WA'):
			query1='select Date,WA from covid19.AUnewCase order by id ASC limit 365;'
		else:
			query1='select Date,NSW from covid19.AUnewCase order by id ASC limit 365;'

		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		#get the last (latest record)
		csor = cnx.cursor()
		#query1='select Date,AUtotal from covid19.AUnewCase order by id ASC limit 365;'
		#query1='select * from covid19.NSWCase'
		csor.execute(query1)
		rows = csor.fetchall()
		#1:date,2:newCase
		listData = []
		for row in rows:
			listData.append(list(row))
		csor.close()
		cnx.close()
	except Exception as sqlE:
		print(str(sqlE))

	return (json.dumps(listData))

@app.route('/NSWcrossRF')
def NSWcrossRF():
	try:
		listData = []
		jsDict = json.loads(((request.args).to_dict())['data'])
		
		#print(jsDict)
		#print(type(jsDict))

		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)

		for key in jsDict:
			if ((key == 'NSWdaily') and (jsDict[key] == 1)):
				query='select Date,NewCase from covid19.NSWCase order by id ASC limit 365;'
				csor = cnx.cursor()
				csor.execute(query)
				rows = csor.fetchall()
				#1:date,2:newCase
				if(len(listData) == 0):
					for row in rows:
						listData.append(list(row))
				else:
					for i in range(len(listData)):
						listData[i].append((rows[i])[1])
				csor.close()
				query=''
			if ((key == 'NSWtotal') and (jsDict[key] == 1)):
				query='select Date,TotalCase from covid19.NSWCase order by id ASC limit 365;'
				csor = cnx.cursor()
				csor.execute(query)
				rows = csor.fetchall()
				if(len(listData) == 0):
					for row in rows:
						listData.append(list(row))
				else:
					for i in range(len(listData)):
						listData[i].append((rows[i])[1])
				csor.close()
				query=''
			if ((key == 'NSWRec') and (jsDict[key] == 1)):
				query='select Date,Recovery from covid19.NSWCase order by id ASC limit 365;'
				csor = cnx.cursor()
				csor.execute(query)
				rows = csor.fetchall()
				if(len(listData) == 0):
					for row in rows:
						listData.append(list(row))
				else:
					for i in range(len(listData)):
						listData[i].append((rows[i])[1])

				csor.close()
				query=''
			if ((key == 'NSWact') and (jsDict[key] == 1)):
				query='select Date,Active from covid19.NSWCase order by id ASC limit 365;'
				csor = cnx.cursor()
				csor.execute(query)
				rows = csor.fetchall()
				if(len(listData) == 0):
					for row in rows:
						listData.append(list(row))
				else:
					for i in range(len(listData)):
						listData[i].append((rows[i])[1])
				csor.close()
				query=''
			if ((key == 'NSWtest') and (jsDict[key] == 1)):
				query='select Date,TestedCase from covid19.NSWCase order by id ASC limit 365;'
				csor = cnx.cursor()
				csor.execute(query)
				rows = csor.fetchall()
				if(len(listData) == 0):
					for row in rows:
						listData.append(list(row))
				else:
					for i in range(len(listData)):
						listData[i].append((rows[i])[1])
				csor.close()
				query=''
			if ((key == 'NSWdeath') and (jsDict[key] == 1)):
				query='select Date,TotalDeath from covid19.NSWCase order by id ASC limit 365;'
				csor = cnx.cursor()
				csor.execute(query)
				rows = csor.fetchall()
				if(len(listData) == 0):
					for row in rows:
						listData.append(list(row))
				else:
					for i in range(len(listData)):
						listData[i].append((rows[i])[1])
				csor.close()
				query=''

	except Exception as sqlE:
		print(str(sqlE))
	#print(listData)
	return(json.dumps(listData))

def switch_query(argument):
	switcher = {
			0: ",AU",
			1: ",AUtotal",
			2: ",NSW",
			3: ",QLD",
			4: ",SA",
			5: ",VIC",
			6: ",WA",
			7: ",TAS",
			8: ",NT",
			9: ",ACT"
			}
	return switcher.get(argument, "")

@app.route('/AUcrossRF')
def AUcrossRF():
	try:
		listData = []
		jsDict = ""
		#print(request.args)
		#jsDict = str(json.loads(((request.args).to_dict())['data']))
		jsDict = ((request.args).to_dict())['data']
		query = ""
		#print(jsDict)
		#print(type(jsDict))

		#build mysql query
		cnx = mysql.connector.connect(user=dbuser, password=dbpw,
				host=dbhost,
				database=dbase)
		
		query1 = "select Date"
		query3 = " from covid19.AUnewCase order by id ASC limit 365;"
		query2 = ""
		for i in range(10):
			if jsDict[i] == '1':
				#0 national increase daily 1 national total 2 nsw 3 qld 4 sa 5 vic 6 wa 7 tas 8 nt 9 act
				query2 = query2 + switch_query(i)

		query = query1+query2+query3
		#print(query)
		csor = cnx.cursor()
		csor.execute(query)
		rows = csor.fetchall()
		for row in rows:
			listData.append(list(row))
		csor.close()
		query=''

	except Exception as sqlE:
		print(str(sqlE))
	#print(listData)
	return(json.dumps(listData))



if __name__ == "__main__":
    conffile=sys.argv[1]
    with open(conffile) as f:
        lines = f.readlines()
        dbuser = lines[0].strip().split('=')[1]
        dbpw = lines[1].strip().split('=')[1]
        dbhost = lines[2].strip().split('=')[1]
        dbase = lines[3].strip().split('=')[1]
        webhost = lines[4].strip().split('=')[1]
        webport = lines[5].strip().split('=')[1]
    #print(dbuser)
    #print(dbpw)
    #print(dbhost)
    #print(dbase)
    #print(webhost)
    #print(webport)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host=webhost, port=webport)
