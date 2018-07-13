#! usr/bin/python3

from flask import Flask, render_template, request
from passcha import get_password

global resultsDict
resultsDict = {}

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")   
 
@app.route('/changepwd', methods = ['POST'])
def changepwd():
  if request.method == 'POST':
    x = request.form['pwd']
    y = request.form['reset_pwd']
    outcome, results = get_password(x,y, resultsDict)
    global resultsDict
    resultsDict = results
    if outcome == True:
      # return "Ok"
      return render_template("index1.html", data=x, password_message="ok") 
    else:
      return render_template('index.html', password_message = "Wrong password, try Again")
 
if __name__ == '__main__':
  with open('/etc/hostapd/hostapd.conf', "r") as f:
    f_contents = f.readlines()
    resultsDict = {}
    for line in f_contents:
      key,value = line.split("=")
      resultsDict[key] = value.strip()
  f.close()
  app.run(debug=True, host='0.0.0.0')
