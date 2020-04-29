from flask import Flask, jsonify, request, json
from datetime import datetime
# from flask_cors import CORS, cross_origin
import hashlib, psycopg2, os


app = Flask(__name__)

app.route('/')
app.route('/login')

def Login(gituser, password):

    password = hashlib.sha256(password.encode())
    hashedpass= password.hexdigest()

    sql = ""
    sql += "SELECT * FROM acct_logins"
    sql += " WHERE"
    sql += " ("
    sql += " github_name ='" + gituser + "'"
    sql += " AND"
    sql += " pass = '" + hashedpass + "'"
    sql += " )"
#    Uncomment to print out query
#    print(sql)
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        # connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
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
