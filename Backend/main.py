# Import modules
from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import json
import html
import os

# Import files
import database
import functions
import vcard_parser

# Imported functions from files
from database import collection
from vcard_parser import vcard_parser
# from functions import

# Set the flask app
app = Flask(__name__)

#hei

# POST /contacts endpoint – Lisa, fortsette på den
@app.route('/contacts', methods=['POST'])
def new_contact():
    file = request.files['file']
    # file.save('/' + file.filename)
    file.save(secure_filename(file.filename))
    return 'file uploaded successfully'
    vcard_parser(file)
    with open('data.json') as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)
    return jsonify(file_data)
    
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
        

# GET /contacts endpoint (json) – Alexandra

# GET /contacts/id endpoint (json) - Anosh

# GET /contacts/vcard (vcard)

# GET /contacts/id/vcard (vcard)



# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(port=3000, debug=True)

