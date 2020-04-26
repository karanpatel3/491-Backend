from flask import Flask, jsonify, request, json
import psycopg2, hashlib
from CallScraper import GetLang

app = Flask(__name__)
@app.route('/')
#Variables below to put into query, convert these to be POSTED later
@app.route('/register')
def Register(f, l, a, g, e, p):
    
    fname = f
    lname = l
    actoken = a
    gituser = g
    email = e
    password = hashlib.sha256(p.encode())
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
    sql += ") VALUES ("
    sql += " '" + fname + "'"
    sql += ",'" + lname + "'"
    sql += ",'" + actoken + "'"
    sql += ",'" + gituser + "'"
    sql += ",'" + email + "'"
    sql += ",'" + hashedpass + "'"
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
    f = 'Ashis'
    l = 'Gare'
    a = '944a69adfc88a90271f1c5c3b47dc1d577db4c58'
    g = 'ashish'
    e = 'avg53@rutgers.edu'
    p = 'yes'
    print(Register(f, l, a, g, e, p))
