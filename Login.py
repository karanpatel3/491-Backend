from flask import Flask, jsonify, request, json
from datetime import datetime
from flask_cors import CORS, cross_origin
import hashlib, psycopg2, os
from models import Acct, Skills, db



app = Flask(__name__)

app.route('/')
app.route('/login')

def Login(gituser, password):

    password = hashlib.sha256(password.encode())
    hashedpass= password.hexdigest()


    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        
    except:
        print ("I am unable to connect to the database.")

    try:
        result = Acct.query.filter_by(github_name=gituser, passw=hashedpass).scalar() is not None
        return result


    except:
        message = "Database error "
        result = 'false'
        return result
       
           
   
       
if __name__ =="__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
    passw='yes'
    email = 'jrs487@rutgers.edu'
    print(Login(email, passw))
