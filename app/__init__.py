from flask import Flask,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
#from app import views, models

app.config['MONGO_DBNAME'] = 'ffe68dbf-7fb4-4bbe-9f72-3cd0b519caea'
app.config['MONGO_URI'] = 'mongodb://9a0c884b-3a06-42ff-972d-db78907d5727:ySIl9NWcehDYlAOxoLGMs3Dqy@42.159.80.108:27017/ffe68dbf-7fb4-4bbe-9f72-3cd0b519caea'

app.url_map.strict_slashes = False
mongo = PyMongo(app)

@app.route("/", methods=['GET'])
def home_page():
    return "<h1>Hello World!</h1>"

@app.route("/rtdata", methods=['GET'])
def rtdata_page():
    #rtdatas = mongo.db.getCollection('ene_rtdata').find({})
    rtdatas = mongo.db.ene_rtdata.find({})
    #rtdatas = mongo.db.ene_rtdata.find_one()
    return render_template('index2.html',rtdatas=rtdatas)