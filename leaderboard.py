from replit import db

#Storing initial values in the database
#Comment out after first run
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

def update_leaderboard(username, score):
  if score > db["score1"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = db["number3"]
    db["score4"] = db["score3"]
    db["number3"] = db["number2"]
    db["score3"] = db["score2"]
    db["number1"] = username
    db["score1"] = score
  elif score > db["score2"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = db["number3"]
    db["score4"] = db["score3"]
    db["number3"] = db["number2"]
    db["score3"] = db["score2"]
    db["number2"] = username
    db["score2"] = score
  elif score > db["score3"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = db["number3"]
    db["score4"] = db["score3"]
    db["number3"] = username
    db["score3"] = score
  elif score > db["score4"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = username
    db["score4"] = score
  elif score > db["score5"]:
    db["number5"] = username
    db["score5"] = score
 
  


