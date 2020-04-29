from flask import Flask, jsonify, request, json, jsonify
import psycopg2, json

def Update(c):
    content = c
    gituser = content['userName']
    actoken = content['github_token']

    # gituser = user
    # actoken = tok
    sql = "UPDATE public.acct_logins SET access_token='"+actoken+"' WHERE github_name = '"+gituser+"';"

    print(sql)
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
    message = "Your token has been updated."
    print(message)
    return message