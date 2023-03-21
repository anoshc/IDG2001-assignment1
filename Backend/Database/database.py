from flask import Flask
from pymongo import MongoClient
#import os

#DB_URI = "mongodb+srv://lisamarimyrene:mongodbpassword@cluster0.mub535i.mongodb.net/vCardDB?retryWrites=true&w=majority"

app = Flask(__name__)


client = MongoClient('mongodb+srv://idg2001:mongodbpassword@cluster0.luifcsb.mongodb.net/vCardDB')
db = client.mydatabase


if __name__ == '__main__':
   app.run(port=4000)
   #app.run(host=os.getenv('HOST', 'localhost'), port=os.getenv('PORT', '5000'))