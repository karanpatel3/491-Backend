from flask import Flask, request
from flask_cors import CORS, cross_origin
from Login import Login
from Register import Register
from CallScraper import GetTok, GetLang
import psycopg2
import hashlib
import json

app = Flask(__name__)



@app.route('/login', methods=['POST'])
def getPost():
#Sets Posted JSON from the front to variable content
    content = request.get_json()

#Decodes posted JSON and sets email and password to local variables
    email = content['email']
    password = content['password']

#Checks email and password against Login Function and sets result equal to a Boolean
    res = Login(email, password)

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
    email = content['email']
    password = content['password']
    fname = content['firstName']
    lname = content['lastName']
    actoken = content['token']

#Inserts user data into the database using Register Function and sets result equal to a Boolean
    res = Register(fname, lname, actoken, email, password)
    res = {
        'res' : res
    }
    return res

@app.route('/scraper', methods=['POST'])
def getScrape():
    content = request.get_json()
    username = content['email'] #CHANGE 'EMAIL' TO WHATEVER VARIABLE NAME THAT USERNAME IS SENT
    token = GetTok(username)
    res = GetLang(token)
    return res

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ =="__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000, debug=True, threaded=True)
