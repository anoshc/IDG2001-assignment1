from flask import Flask
from pymongo import MongoClient
from dotenv import dotenv_values

app = Flask(__name__)

config = dotenv_values('.env')
mongo_uri = config['MONGO_URI']
client = MongoClient(mongo_uri)

db = client['vCardDB']
collection = db['vcard']

documents = collection.find({})
for document in documents:
   print(document)
   

if __name__ == '__main__':
   app.run(port=4000)
   #app.run(host=os.getenv('HOST', 'localhost'), port=os.getenv('PORT', '5000'))