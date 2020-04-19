from flask import Flask, jsonify, request, json
import psycopg2
import hashlib
import logging

logging.info("my app has started")

app = Flask(__name__)
@app.route('/')
#Variables below to put into query, convert these to be POSTED later
@app.route('/register')
def Register(f, l, a, e, p):

    fname = f
    lname = l
    actoken = a
    email = e
    password = hashlib.sha256(p.encode())
    hashedpass= password.hexdigest()

    #sql query, do not touch
    sql = "INSERT INTO acct_logins "
    sql += "("
    sql += "  first_name"
    sql += ", last_name"
    sql += ",  access_token"
    sql += ", email"
    sql += ", pass"
    sql += ") VALUES ("
    sql += " '" + fname + "'"
    sql += ",'" + lname + "'"
    sql += ",'" + actoken + "'"
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
##        cur.execute("SELECT * from acct_logins")


##    #Uncomment this block to see what's in the acct_logins
##        db=cur.fetchall()
##        print(db)
##        connection.commit()

    except psycopg2.Error as e:
        message = "Database error: " + e + "/n SQL: " + sql
        result = 'false'
        cur.close()
        return result
       
           
    result = 'true'
    message = "Your user account has been added."
    print(message)
    cur.close()
    return result
   

if __name__ =="__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
    f = 'Ashish'
    l = 'Gare'
    a = 'WORKING'
    e = 'avg53@rutgers.edu'
    p = 'yes'
    print(Register(f, l, a, e, p))
