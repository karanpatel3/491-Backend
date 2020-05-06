from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from Login import Login
from Register import Register
from dynamic import dyn
from TestCallScraper import GetTok, GetLang, IfExists
import psycopg2, random, hashlib, json, os
from models import app, db




@app.route('/login', methods=['POST'])
def getPost():
#Sets Posted JSON from the front to variable content
    content = request.get_json()

#Decodes posted JSON and sets email and password to local variables
    username = content['userName']
    password = content['password']

#Checks email and password against Login Function and sets result equal to a Boolean
    res = Login(username, password)

    res = {
        'res' : res
    }
#Returns result back to front
    return res
    

@app.route('/register', methods=['POST'])
def getReg():
#Sets Posted JSON from the front to variable content
    content = request.get_json()

#Decodes posted JSON and sets relevant data to local variables
    # email = content['email']
    # git_user = content['github_userName']
    # password = content['password']
    # fname = content['firstName']
    # lname = content['lastName']
    # occupation = content['occupation']
    # city = content['city']
    # bio = content['bio']
    # actoken = content['token']

#Inserts user data into the database using Register Function and sets result equal to a Boolean
    # res = Register(fname, lname, actoken, git_user, email, password)
    res = Register(content) 
    res = {
        'res' : res
    }
    return res

@app.route('/scraper', methods=['POST'])
def getScrape():
    content = request.get_json()
    username = content['userName'] #CHANGE 'EMAIL' TO WHATEVER VARIABLE NAME THAT USERNAME IS SENT
    
    langs = IfExists(username)
    
    labels = []
    data = []
    for key in langs:
        labels.append(key)
        data.append(langs[key])

    backgroundColor = []

    for c in langs:
        string = 'rgba({},{},{},0.6)'.format(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
        backgroundColor.append(string)

    res = {
        'labels' : labels,
        'data' : data,
        'backgroundColor' : backgroundColor
    }
    return res
@app.route('/users', methods=['GET'])
def retusers():
    return dyn()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ =="__main__":
    # app.debug = True
    # app.run(host = '0.0.0.0', port = 5000, debug=True, threaded=True)
    langs = IfExists('theokahanda')
    labels = []
    data = []
    for key in langs:
        labels.append(key)
        data.append(langs[key])

    backgroundColor = []

    for c in langs:
        string = 'rgba({},{},{},0.6)'.format(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
        backgroundColor.append(string)

    res = {
        'labels' : labels,
        'data' : data,
        'backgroundColor' : backgroundColor
    }
    print(res)
