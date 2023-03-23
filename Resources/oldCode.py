# @app.route('/')
# def index():
#     db = client.mydatabase
#     collection = db.mycollection
#     data = collection.find_one()
#     return f'Hello, {data}!'
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


# Get
# @app.route('/api/users')
# def get_users():
#     user_id = request.args.get('id')
#     # implement code to retrieve and return user data
#     return jsonify(user)