from flask import Flask, render_template, request
from replit import db
import leaderboard
app = Flask('app')

db["number1"] = "Dr.A"
db["score1"] = 20
db["number2"] = "Danielle"
db["score2"] = 18
db["number3"] = "Shemaya"
db["score3"] = 17
db["number4"] = "Antonia"
db["score4"] = 10
db["number5"] = "Brandon"
db["score5"] = 3

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

@app.route('/leaderboard')
def display_leaderboard():
  return render_template("leaderboard.html")
app.run(host='0.0.0.0', port=81)