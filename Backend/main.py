from flask import Flask, render_template, request, jsonify
import json
import html
import os
from pymongo import MongoClient

# Set the flask app
app = Flask(__name__)
#api = Api(app)

client = MongoClient('mongodb+srv://idg2001:mongodbpassword@cluster0.luifcsb.mongodb.net/vCardDB')
db = client.mydatabase


# Test GET

# Hele greia er et Endpoint
# Dette er routen til Endpointet
@app.route('/hei', methods=['GET'])
# Dette er controlleren til Endpointet
def hello_world():
    response = {'message': 'Hello from gruppen!'}
    return jsonify(response)

# Get
# @app.route('/api/users')
# def get_users():
#     user_id = request.args.get('id')
#     # implement code to retrieve and return user data
#     return jsonify(user)


# # Post
# @app.route('/api/users', methods=['POST'])
# def create_user():
#     user_data = request.json
#     # implement code to create and return user data
#     return jsonify(user)

@app.route('/')
def index():
    db = client.mydatabase
    collection = db.mycollection
    data = collection.find_one()
    return f'Hello, {data}!'
# @app.route('/results')
# def results():
#     return render_template('../Frontend/index.html')




# @app.route('/')
# def index():
#     collection = db.vcard
#     result = collection.find_one()
#     return str(result)

# Homepage, find the form
# @app.route('/')
# def home():
#     return render_template('../Frontend/index.html')


# Route when uploading file from form
# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     file.save(file.filename)
#     return 'File uploaded successfully!'


# Source https://stackoverflow.com/questions/62906140/displaying-json-in-the-html-using-flask-and-local-json-file 
# with open ('../Database/vcard.json', r) as vcardfile:
#     data = vcardfile.read()

# Route to see the json vcard file
# @app.route('/results')
# def results():
#     return render_template('index.html', title="page", jsonfile=json.dumps(data))

# @app.route('/results/id')
# def resultUer():
#     return # user





# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(port=4000)
    #app.run(host=os.getenv('HOST', 'localhost'), port=os.getenv('PORT', '5000'))


# Run app
#app.run()