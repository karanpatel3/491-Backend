from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Login import Login
from Register import Register
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
    result = Login(email, password)

#Returns result back to front
    return json.dumps(result)


@app.route('/register', methods=['POST'])
def getReg():
#Sets Posted JSON from the front to variable content
    content = request.get_json()

#Decodes posted JSON and sets relevant data to local variables
    email = content['email']
    password = content['password']
    fname = content['firstname']
    lname = content['lastname']
    actoken = content['access_token']

#Inserts user data into the database using Register Function and sets result equal to a Boolean
    result = Register(fname, lname, actoken, email, password)
    return json.dumps(result)

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
