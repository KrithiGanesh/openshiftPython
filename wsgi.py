from flask import Flask
import MySQLdb
import os
import cgi
application = Flask(__name__)
@application.route("/home")
def home():
  greeting = Greeting()
  greet=greeting.post()
  return greet
  
class Greeting():
    def post(self):
        username = "krithiga"
        print("Content-type: text/html")
        welcome_string = """<html><head><title>GenZ Inc.</title></head><body><div class="heading"><h1 style="color:white;background-color:#000066">Welcome to GenZ Inc <img src="pic_trulli.jpg" alt="Trulli" width="38"height="38" style="float:right;"></h1></div> <div class="main"><p style="color:white;background-color:black"><b>IKEA_D-O-D : WEBSITE UNDER CONSTRUCTION</b></p></div> </body> </html>""".format(username)
        return welcome_string

@application.route("/")
def hello_world():

  storage = Storage()

  #storage.populate()

  score = storage.score()

  return score



class Storage():

  def __init__(self):

    self.db = MySQLdb.connect(

      user   = "xxuser",

      passwd = "welcome1",

      db     ="sampledb",

      host   = "custom-mysql.gamification.svc.cluster.local",

      port   = int('3306')

    )



    cur = self.db.cursor()

   # cur.execute("CREATE TABLE IF NOT EXISTS scores(score INT)")



  def populate(self):

    cur = self.db.cursor()

    cur.execute("INSERT INTO scores(score) VALUES(1234)")



  def score(self):

    cur = self.db.cursor()

    cur.execute("SELECT * FROM XXIBM_PRODUCT_STYLE")

    row = cur.fetchone()

    return row[0]

if __name__ == "__main__":
    application.run()
