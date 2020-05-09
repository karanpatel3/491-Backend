from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from Login import Login
from Register import Register
from dynamic import dyn
from TestCallScraper import GetTok, GetLang, IfExists
import random, hashlib, json, os
from models import app, db
from updatetoken import UpToken
from updateemail import UpEmail
from mailing import sendemail
from werkzeug.exceptions import HTTPException

@app.route('/', methods=['GET'])
def Land():

    return "<h1>LANDING PAGE</h1>"




@app.route('/login', methods=['POST'])
def getPost():
#Sets Posted JSON from the front to variable content
    content = request.get_json()

#Decodes posted JSON and sets email and password to local variables


#Checks email and password against Login Function and sets result equal to a Boolean
    res = Login(content)

    res = {
        'res' : res
    }
#Returns result back to front
    return res
    




@app.route('/register', methods=['POST'])
def getReg():
#Sets Posted JSON from the front to variable content
    content = request.get_json()

#Inserts user data into the database using Register Function and sets result equal to a Boolean
    res = Register(content) 
    res = {
        'res' : res
    }
    return res





@app.route('/scraper', methods=['POST'])
def getScrape():
    content = request.get_json()
    username = content['userName']
    
    langs = IfExists(username)
    
    if isinstance(langs, str) is True:
        return "Invalid Username"
    
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



@app.route('/uptoken', methods=['POST'])
def uptoken():
    content = request.get_json()
    
    res = UpToken(content)
    res = {
        'res' : res
    }


@app.route('/upemail', methods=['POST'])
def UpToken():
    content = request.get_json()
    
    res = UpEmail(content)
    res = {
        'res' : res
    }

@app.route('/email', methods=['GET', 'POST'])
def Mailing():
    if request.method == 'GET':
        name = "Karan"
        email = 'kpp86@rutgers.edu'
        sendemail(name, email)
        return "<h1><strong>CHECK YOUR EMAIL</strong></h1>"

    
    return "<h1>TIME TO CODE AGAIN :( :| :) </h1>"
    

# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#         "args": e.args
#     })
#     response.content_type = "application/json"
#     return response



# @app.errorhandler(Exception)
# def handle_exception(e):
#     # pass through HTTP errors
#     if isinstance(e, HTTPException):
#         return e

#     # now you're handling non-HTTP exceptions only
#     return render_template('500_generic.html', e=e), 500



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ =="__main__":
    # app.debug = True
    app.run(host = '0.0.0.0', port = 5000, debug=True, threaded=True)
    print("<h1>WORKING</h1>")