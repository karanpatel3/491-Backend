from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2, random
from GitHubScraper import GetRepo as gr
import numpy as np

def IfExists(username):
    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")
    
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (username,))
    exists = cur.fetchone()[0]
    print(exists)
    if exists is True:
        cur.execute("select * from "+username+"")
        rows = cur.fetchall()

        di = {}

        for a, b in rows: 
            di.setdefault(a, []).append(b) 
        return di 

    else:
        return GetTok(username)


def GetTok(username):
    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")
    
    sql = ""
    sql += "SELECT access_token FROM acct_logins"
    sql += " WHERE"
    sql += " ("
    sql += "  github_name ='" + username + "'"
    sql += " )"
    cur.execute(sql)
    token = cur.fetchone()
    token = token[0]
    return GetLang(username, token)
    
def GetLang(username, access_token):
    
    gi = gr(access_token)
    gi.repo_getter() # Update empty Dictionary
    gi.get_keyval() # Sum up all the respective dictionary key values
    print(gi.emp_dict) # Print final dictionary
    test = gi.emp_dict
    languages=""
    byte_num=""
    
    #send access token to github scraper and get output, dictionary variable equal to output

    tablename = username
   
    sql = ""
    sql += "CREATE TABLE IF NOT EXISTS "
    sql += "" + tablename + ""
    sql += " ("
    sql += "languages varchar(255)"
    sql += ", bytes int"
    sql += ")"

    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")
   
    try:
        cur.execute(sql)
        result = True
        return result   
    except psycopg2.Error as e:
        message = "Database error: " + e + "/n SQL: " + sql
        result = False
        cur.close()
        return result


    languages=""
    byte_num=""
    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")

    for key in test.keys():
        val = test[key]
        sql = "INSERT INTO "+tablename+" (languages, bytes ) VALUES ('"+key+"', "+str(val)+");"
        cur.execute(sql)
    
    test = json.dumps(test)
    res = json.loads(test)
    cur.close()
    return res

if __name__ =="__main__":
    user = 'ashish'
    print(IfExists(user))
