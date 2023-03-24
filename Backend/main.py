# Import modules
from flask import Flask, render_template, request, jsonify
import json
import html
import os
import bson

# Import files
import database
import functions
import vcard_parser

# Imported functions from files
from database import db
from database import collection
from vcard_parser import vcard_parser
# from functions import

# Set the flask app
app = Flask(__name__)


# POST /contacts endpoint – Lisa, fortsette på den
@app.route('/contacts', methods=['POST'])
def new_contact():
    vcard_parser()
    with open('export.json') as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        collection.insert_many(file_data)
        response = {'message': 'Inserted many'}
        return jsonify(response)
        
    else:
        collection.insert_one(file_data)
         response = {'message': 'Inserted one'}
        return jsonify(response)



#GET/contacts - Alexandra:  Finds all contacts 
@app.route('/contacts', methods=['GET'])
def getAllContacts():
 result = collection.find()
 return f' {(list(result))}'
  


#GET/contacts/:id - Anosh: Shows one contact based off id
@app.route('/contacts/:id', methods=['GET'])
def getContacts():
  from bson.objectid import ObjectId
  #Kan displaye dokument basert på id, men hvis man går på routen (/:id) så finner den ikke id.
  result = collection.find_one({"_id": ObjectId("641c63f64b212cebf543eb01")})
  return f'{result}'



 # user_data = export.json
    # implement code to create and return user data
    # return jsonify(user)

   # return jsonify(file_data)

# GET /contacts/id endpoint (json) - Anosh

# GET /contacts/vcard (vcard)

# GET /contacts/id/vcard (vcard)


''' 
    The POST api endpoint does this:
    
    1. Calls a vcard_parser() function (not shown in this code) to parse vCard data.

    2. Reads the contents of a file named export.json into a variable called file_data, 
    using the json.load() function to parse the JSON-formatted data in the file.

    3. Checks if the file_data variable is a list. If it is, it assumes that the data contains 
    multiple records and inserts them all into a MongoDB collection using the insert_many() method. 
    If it is not a list, it assumes that the data contains a single record and inserts it into 
    the MongoDB collection using the insert_one() method.

    4. !Returning the json object as output (doesn't work)
'''





# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(port=3000, debug=True)


