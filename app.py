from flask import Flask, jsonify, request, json
from datetime import datetime
from flask_cors import CORS, cross_origin
import psycopg2
import hashlib

app = Flask(__name__)

CORS(app, support_credentials=True)
@app.route('/')
#Variables below to put into query, convert these to be POSTED later
@app.route('/login', methods=['POST'])

@cross_origin(supports_credentials=True)
# @app.route('/query', methods = ['POST'])


@app.after_request
def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', 'r')
#   response.headers.add('Access-Control-Allow-Credentials', 'true')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#   response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
  return response


def parse_request():
    data = request.get_json()
    email = request.get('email')
    password = request.get('password')
    print(data)
    return data


def Login(email, password):

    password = hashlib.sha256(password.encode())
    hashedpass= password.hexdigest()

    sql = ""
    sql += "SELECT * FROM acct_logins"
    sql += " WHERE"
    sql += " ("
    sql += " email ='" + email + "'"
    sql += " AND"
    sql += " pass = '" + hashedpass + "'"
    sql += " )"
#    Uncomment to print out query
#    print(sql)
    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print ("I am unable to connect to the database.")

    try:
       
        cur.execute(sql)
        if cur.rowcount == 0:
            result = False
            print('NOTHING FOUND')
            return result
        else:
            result = True
            message = "User information found!"
            print(message)
            cur.close()
            return result
       
#uncomment to view all rows in the table        
#        cur.execute("SELECT * from acct_logins")
#        rows = cur.fetchall()
#        print ("\nRows: \n")
#        for row in rows:
#            print (row[1],"   ", row[0])


           

    except psycopg2.Error as e:
        message = "Database error: " + e + "/n SQL: " + sql
        result = 'false'
        cur.close()
        return result
       
           
   
       
if __name__ =="__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
    passw='yes'
    email = 'jrs487@rutgers.edu'
    print(Login(email, passw))
