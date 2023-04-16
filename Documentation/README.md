# IDG2001 Assignment 1 – Lisa Mari, Anosh, and Alexandra
09.04.2023

## GitHub link to repo

https://github.com/anoshc/IDG2001-assignment1

## About the project 

In this project we have creates a Flask application that is running in the Railway Cloud server.
The application have several REST API endpoints that connects to both the cloud and the MongoDB database. 
These endpoints/routes have different functionalities, that we will further explain:

    1. @app.route('/')
        This set the home route for the application. When the user is in the home path,
        they will see the form rendered. 

    2. @app.route('/contacts', methods=['POST'])
        This route takes in the uploaded file from the user, parses it from vcf to json,
        and then pushes the result to the database. 

    3. @app.route('/contacts', methods=['GET'])
        This route finds all contacts in the database and displays it to the user. 

    4. @app.route('/contacts/<id>', methods=['GET'])
        This route find a certain contact in the database based on id, and displays it to the user. 

    5. @app.route('/contacts/vcard', methods=['GET'])
        This route get all the contacts in the database, parses it from json back to vcf (in json format), 
        and then dislays it to the user.

    6. @app.route('/contacts/<id>/vcard', methods=['GET'])
        This route get one specific contact in the database based on id, parses it 
        from json back to vcf (in json format), and then dislays it to the user.


## Modules needed for this project:
If you are running the project locally from your computer, you'll need to download 
these modules to make sure the project renders perfectly:

    - flask : render_template, request, jsonify, send_file, make_response
    - json
    - html
    - os
    - bson
    - vobject
    - pymongo : MongoClient
    - dotenv : dotenv_values

## Database
The project needs to be able to connect to the database and its collections. To make this possible, we needed to use the pymongo and dotenv modules. We put the MONGO_URI inside an ```.env``` file, to make the connection more secure. 

## Templates
The HTML form that are displaying in the homepage, are called a 'template' in Python. Thats why the index.html is placed inside the templates folder. This is so that Python is able to find the index form. 

We have also chosen to add a little bit of styling to the application, for a better experience. 