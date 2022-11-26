from flask import Flask, render_template, request
from replit import db
import leaderboard
app = Flask('app')

# db["number1"] = "Dr.A"
# db["score1"] = 20
# db["number2"] = "Danielle"
# db["score2"] = 18
# db["number3"] = "Shemaya"
# db["score3"] = 17
# db["number4"] = "Antonia"
# db["score4"] = 10
# db["number5"] = "Brandon"
# db["score5"] = 3

@app.route('/')
def home():
  return render_template('homepage.html')
  
@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/instructions')
def instructions():
  return render_template("instructions.html")

@app.route("/PlayGame")
def get_result():
  result = request.form.to_dict()
  username = result["username"]
  score = result["score"]
  return render_template("play_game.html")

@app.route('/leaderboard')
def display_leaderboard():
  number1 = db["number1"] + ": " + str(db["score1"])
  number2 = db["number2"] + ": " + str(db["score2"])
  number3 = db["number3"] + ": " + str(db["score3"])
  number4 = db["number4"] + ": " + str(db["score4"])
  number5 = db["number5"] + ": " + str(db["score5"])
  return render_template('leaderboard.html', number1=number1, number2=number2, number3=number3, number4=number4, number5=number5)



  
app.run(host='0.0.0.0', port=81)