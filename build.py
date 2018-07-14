#! usr/bin/python3

from flask import Flask, render_template, request, url_for
from passcha import get_password, change_ssid, read_config

global resultsDict

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")   
 
@app.route('/changepwd', methods = ['POST','GET'])
def changepwd():
  if request.method == 'POST':
    x = request.form['pwd']
    y = request.form['reset_pwd']
    is_successful, newDict = get_password(x, y, resultsDict)
    global resultsDict
    resultsDict = newDict
    if is_successful:
        return render_template("index.html", data_pass = "Password successfully changed")
    else:
        return render_template("index.html", data_pass = "Incorrect Password")
  elif request.method == 'GET':
    return render_template("index.html")

@app.route('/changessid', methods = ['POST','GET'])
def changessid():
  if request.method == 'POST':
    s = request.form['reset_ssid']
    newDict = change_ssid(s, resultsDict)
    global resultsDict
    resultsDict = newDict
    return render_template("index.html", data_ssid="SSID successfully changed")
  elif request.method == 'GET':
    return render_template("index.html")
        
if __name__ == '__main__':
    resultsDict = read_config()
    app.run(debug=True, host='0.0.0.0')
