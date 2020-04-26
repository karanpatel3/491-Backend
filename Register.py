from flask import Flask, jsonify, request, json
import psycopg2, hashlib
from CallScraper import GetLang

app = Flask(__name__)
@app.route('/')
#Variables below to put into query, convert these to be POSTED later
@app.route('/register')
def Register(c):
    content = c
    email = content['email']
    gituser = content['github_userName']
    password = content['password']
    fname = content['firstName']
    lname = content['lastName']
    occupation = content['occupation']
    city = content['city']
    bio = content['bio']
    actoken = content['token']
    password = hashlib.sha256(password.encode())
    hashedpass= password.hexdigest()

    #sql query, do not touch
    sql = "INSERT INTO acct_logins "
    sql += "("
    sql += "  first_name"
    sql += ", last_name"
    sql += ",  access_token"
    sql += ", github_name"
    sql += ", email"
    sql += ", pass"
    sql += ", city"
    sql += ", bio"
    sql += ", occupation"
    sql += ") VALUES ("
    sql += " '" + fname + "'"
    sql += ",'" + lname + "'"
    sql += ",'" + actoken + "'"
    sql += ",'" + gituser + "'"
    sql += ",'" + email + "'"
    sql += ",'" + hashedpass + "'"
    sql += ",'" + city + "'"
    sql += ",'" + bio + "'"
    sql += ",'" + occupation + "'"
    sql += ")"

    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")
   
    try:
        cur.execute(sql)


    except psycopg2.Error as e:
        message = "Database error: " + e + "/n SQL: " + sql
        result = 'false'
        cur.close()
        return result
       
           
    result = 'true'
    message = "Your user account has been added."
    print(message)
    GetLang(gituser, actoken)
    cur.close()
    return result
   

if __name__ =="__main__":
    # app.debug = True
    # app.run(host = '0.0.0.0', port = 5000)
