from flask import Flask, render_template, request, jsonify
import json
import html
import os
# Imported database.py file
import database
# Imported varables from database.py file
from database import collection 

import functions
from functions import 



# Set the flask app
app = Flask(__name__)




# Test GET

# Hele greia er et Endpoint
# Dette er routen til Endpointet
@app.route('/', methods=['GET'])
# Dette er controlleren til Endpointet
def hello_world():
    response = {'message': 'Hello from gruppen!'}
    return jsonify(response)

@app.route('/railway', methods=['GET'])
# Dette er controlleren til Endpointet
def hello_railway():
    data = collection.find()
    return f'Hello, {data}!'



# # Post
@app.route('', methods=['POST'])
def create_user():
    user_data = export.json
    # implement code to create and return user data
    return jsonify(user)






# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(port=4000)
    #app.run(host=os.getenv('HOST', 'localhost'), port=os.getenv('PORT', '5000'))


# Run app
app.run()