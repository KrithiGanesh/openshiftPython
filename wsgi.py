from flask import Flask
import MySQLdb
import os
application = Flask(__name__)
@application.route("/home")
def home():
  greeting = Greeting()
 
  
class Greeting():
    def __init__(self):
        username = "krithiga"
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)

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
