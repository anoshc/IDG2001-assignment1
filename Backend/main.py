# Import modules
from flask import Flask, render_template, request, jsonify
import json
import html
import os

# Import files
import database
import functions

# Imported functions from files
from database import collection 
from functions import 

# Set the flask app
app = Flask(__name__)


# POST /contacts endpoint
@app.route('/contacts', methods=['POST'])
def newContact():
    user_data = export.json
    # implement code to create and return user data
    return jsonify(user)


# GET /contacts endpoint (json)


# GET /contacts/id endpoint (json)


# GET /contacts/vcard (vcard)


# GET /contacts/id/vcard (vcard)







''' TEST API FOR Å SJEKKE OM DET FUNKA BERRE'''
@app.route('/railway', methods=['GET'])
# Dette er controlleren til Endpointet
def hello_railway():
    data = collection.find()
    return f'Hello, {data}!'

# Hele greia er et Endpoint
# Dette er routen til Endpointet
@app.route('/', methods=['GET'])
# Dette er controlleren til Endpointet
def hello_world():
    response = {'message': 'Hello from gruppen!'}
    return jsonify(response)


# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(port=4000)
    #app.run(host=os.getenv('HOST', 'localhost'), port=os.getenv('PORT', '5000'))


# Run app
app.run()