from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)



@app.route('/time', methods=['POST'])
def get_current_time():
    email = request.json
    return {
    'pass': email
    }

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response
   
if __name__ =="__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000, debug=True, threaded=True)
