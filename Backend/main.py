# Import modules
from flask import Flask, render_template, request, jsonify
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



# Render the HTML form to the page
@app.route('/')
def upload_file():
   return render_template('index.html')
   
# POST/contacts endpoint - Get the uploaded vcf-file, parse it to JSON, and push it to the database. 
@app.route('/contacts', methods=['POST'])
def new_contact():
    # Hente filen fra html formet
    if request.method == 'POST':
        uploaded_file = request.files['file']
        # Om filen ikke er tom, gjør dette:
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename) # Saver filen
            vcard_parser(uploaded_file.filename) # Parse filen til JSON
            os.remove(uploaded_file.filename) # Fjerne vcf filen lokalt 
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
        

# GET/contacts - Show all contacts 
@app.route('/contacts', methods=['GET'])
def getAllContacts():
 result = collection.find()
 return f' {(list(result))}'
  


# GET/contacts/<id> - Shows one contact based on id
@app.route('/contacts/<id>', methods=['GET'])
def getContacts(id):
  from bson.objectid import ObjectId
  #Kan displaye dokument basert på id, men hvis man går på routen (/:id) så finner den ikke id.
  result = collection.find_one({"_id": ObjectId(id)})
  return f'{result}'



# GET /contacts/vcard (vcard) – Parse the contacts in json back to vcf, and shows all contacts in vcf. 
@app.route('/contacts/vcard', methods=['GET'])
def getVCard():
 print("hi")



# GET /contacts/id/vcard (vcard) – Parse one contact (based on id) in json back to vcf, and shows that one contact in vcf.
@app.route('/contacts/<id>/vcard', methods=['GET'])
def getVCardID(id):
   print("hi")



app.run()
