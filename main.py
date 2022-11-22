from flask import Flask, render_template, request
from replit import db
app = Flask('app')

@app.route('/')
def home():
  return render_template('homepage.html')
  
@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/instructions')
def instructions():
  return render_template("instructions.html")

@app.route('/GAME')
def play_game():
  return render_template("play_game.html")

app.run(host='0.0.0.0', port=81)