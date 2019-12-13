from flask import Flask
import ibm_boto3
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

    return row[0]+":"+row[1]+":"+row[2]+":"+row[2]+":"+row[3]+":"+row[4]
  
  @application.route("/boto")
  def hello_boto():

    fetchBoto=BotoImages()
    img=fetchBoto.fetchImg()
    return img
  
  class BotoImages():
    def fetchImg():
      cos_credentials={
              "apikey": "_bAzHuCAN1yPz4Rcg5CZY1Tbp0UOpshuMhpoNkIvJAa3",
              "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
              "iam_apikey_description": "Auto-generated for key b766a2b2-aacd-4a78-aaed-1784769a82a6",
              "iam_apikey_name": "gamification-cos-standard-tkq",
              "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
              "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/693fe8ead49b44b192004113d21b15c2::serviceid:ServiceId-f6d85b01-d45a-4d92-831d-3e3efa44bb3c",
              "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/693fe8ead49b44b192004113d21b15c2:fce26086-5b77-42cc-b1aa-d388aa2853d7::"
                      }
      auth_endpoint = 'https://iam.bluemix.net/oidc/token'
      service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

      cos = ibm_boto3.client('s3',
                               ibm_api_key_id=cos_credentials['apikey'],
                               ibm_service_instance_id=cos_credentials['resource_instance_id'],
                               ibm_auth_endpoint=auth_endpoint,
                               config=Config(signature_version='oauth'),
                               endpoint_url=service_endpoint)

      for bucket in cos.list_buckets()['Buckets']:
          print(bucket['Name'])
  
  

if __name__ == "__main__":
    application.run()
