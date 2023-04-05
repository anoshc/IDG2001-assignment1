# Import modules
from flask import Flask, render_template, request, jsonify, send_file, make_response
import json
import html
import os
import bson
import vobject

# Import files
import database
import vcard_to_json_parser
import json_to_vcard_parser

# Imported functions from files
from database import db
from database import collection
from vcard_to_json_parser import vcard_parser
from json_to_vcard_parser import json_parser

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
    json_parser() # Kjører når vi skriver in routen i postman om man vil teste
    vcards_json = json_parser()
    return jsonify(vcards_json) # Pushes the json to the Postman output
    
    # Prøver å laste ned vcard.json filen her (som inneholder vcard stringen)
    # response = make_response(send_file('vcard.json', as_attachment=True, attachment_filename='data.vcf')) 
    # response.headers['Content-Disposition'] = 'attachment; filename=data.vcf'
    # return response

# GET /contacts/id/vcard (vcard) – Parse one contact (based on id) in json back to vcf, and shows that one contact in vcf.
@app.route('/contacts/<id>/vcard', methods=['GET'])
def getVCardId(id):
    print("hi")



app.run(port=3000)
