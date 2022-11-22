from flask import Flask, render_template, request
from replit import db
app = Flask('app')

@app.route('/')
def homepage():
  return render_template('instructions.html')

@app.route('/login_or_signup',methods=["POST", "GET"])
def login_or_signup():
  return render_template("login_or_signup.html")

@app.route('/signin')
def login():
  return render_template('login_or_signup.html')
  
app.run(host='0.0.0.0', port=81)