from flask import Flask, jsonify, request, json
from datetime import datetime
from flask_cors import CORS, cross_origin
import hashlib, psycopg2, os
from models import Acct, Skills, db

def Login(content):
    
#Unpackages JSON
    content = request.get_json()
    username = content['userName']
    password = content['password']

#Hashes Password
    password = hashlib.sha256(password.encode())
    password = password.hexdigest()

#Tries to log in
    try:
        result = Acct.query.filter_by(github_name=username, passw=password).scalar() is not None
        return result

#If Fails, returns error
    except Exception as error:
        print(error.orig.args)
        return error.orig.args
       
           
   
       
if __name__ =="__main__":
    passw='yes'
    email = 'jrs487@rutgers.edu'
    print(Login(email, passw))
