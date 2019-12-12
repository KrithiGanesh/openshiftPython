from flask import Flask
import MySQLdb
import os
application = Flask(__name__)

@application.route("/")
def hello_world():

  storage = Storage()

  #storage.populate()

  score = storage.score()

  return "Hello pythonapp 123, %d!" % score



class Storage():

  def __init__(self):

    self.db = MySQLdb.connect(

      user   = os.getenv('xxuser'),

      passwd = os.getenv('welcome1'),

      db     = os.getenv('sampledb'),

      host   = os.getenv('mysql-gamification.inmbzp8022.in.dst.ibm.com'),

      port   = int(os.getenv('3306'))

    )



    cur = self.db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS scores(score INT)")



  def populate(self):

    cur = self.db.cursor()

    cur.execute("INSERT INTO scores(score) VALUES(1234)")



  def score(self):

    cur = self.db.cursor()

    cur.execute("SELECT * FROM scores")

    row = cur.fetchone()

    return row[0]

if __name__ == "__main__":
    application.run()
