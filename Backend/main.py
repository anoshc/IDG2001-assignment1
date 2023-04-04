# Import modules
from flask import Flask, render_template, request, redirect, url_for, jsonify
#from werkzeug import secure_filename
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
app.config['UPLOAD_FOLDER'] = '/vcard_files'



# Rendre HTML formet
@app.route('/')
def upload_file():
   return render_template('index.html')
   

# POST /contacts endpoint – Lisa, fortsette på den
@app.route('/contacts', methods=['POST'])
def new_contact():
def new_contact():
    # Hente filen fra html formet
    if request.method == 'POST':
        uploaded_file = request.files['file']
        # Om filen ikke er tom, gjør dette:
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename) # Saver filen
            vcard_parser(uploaded_file.filename) # Parse filen til JSON
            return 'File read successfully and uploaded to database!'
        else:
            return 'Could not read file, try again.'
    
    # Pushe filen til databasen
    with open('data.json') as data:
        file_data = json.load(data)
        if isinstance(file_data, list):
            collection.insert_many(file_data)
        else:
            collection.insert_one(file_data)
        return jsonify(file_data)
        


#GET/contacts -  Finds all contacts 
@app.route('/contacts', methods=['GET'])
def getAllContacts():
 result = collection.find()
 return f' {(list(result))}'
  


#GET/contacts/<id> - Shows one contact based off id
@app.route('/contacts/<id>', methods=['GET'])
def getContacts(id):
  from bson.objectid import ObjectId
  #Kan displaye dokument basert på id, men hvis man går på routen (/:id) så finner den ikke id.
  result = collection.find_one({"_id": ObjectId(id)})
  return f'{result}'



# GET /contacts/vcard (vcard)
@app.route('/contacts/vcard', methods=['GET'])
def getVCard():
 print("hi")



# GET /contacts/id/vcard (vcard)
@app.route('/contacts/<id>/vcard', methods=['GET'])
def getVCardID(id):
   print("hi")



# user_data = export.json
  # implement code to create and return user data
  # return jsonify(user)

 # return jsonify(file_data)


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


