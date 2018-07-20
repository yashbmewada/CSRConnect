from flask import Flask,jsonify,request
from flask_cors import CORS
import pymongo
import json
from pymongo import MongoClient
from scorepredictor import *

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.CSRConnect


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/allngos')
def get_all_ngos():
    ngos = []
    collection = db.ngos
    cursor = collection.find({},{'_id':0})

    for document in cursor:
        ngos.append(document)
    return jsonify(ngos)

@app.route('/allcompany')
def getAllCompany():
    final = []
    collection = db.company
    cursor = collection.find({},{'_id':0})
    print(cursor)
    for document in cursor:
        final.append(document)
    return jsonify(final)

@app.route('/company/<id>')
def getcompany(id):
    final = []
    collection = db.company
    print(type(id))
    cursor = collection.find({'id':int(id)},{'_id':0})
    for document in cursor:
        final.append(document)
    return jsonify(final)

@app.route('/ngo/<id>')
def getngo(id):
    final = []
    collection = db.ngos
    cursor = collection.find({'id':int(id)},{'_id':0})
    for document in cursor:
        final.append(document)
    return jsonify(final)

@app.route('/donation', methods=['POST'])
def addDonation():
    content = request.get_json(silent=True)
    collection = db.ngos
    print("Content : " + str(content))
    collection.update_one(
        {"id":int(content["id"])},
        {
            "$set":{
                "donation_money":content["amount"]
            }
        }
    )
    print("records updated")
    return "OK"

@app.route('/score', methods=['GET','POST'])
def getNonProfitScore():
    collection = db.ngos
    m1,m2,m3,m4,m5,m6,intercept = predictScore()
    content = request.get_json(silent=True)
    x1 = content["x1"]
    x2 = content["x2"]
    x3 = content["x3"]
    x4 = content["x4"]
    x5 = content["x5"]
    x6 = content["x6"]

    predicted_y = m1 * x1 - m2 * x2 + m3 * x3 - m4 * x4 + m5 * x5 - m6 * x6 + intercept

    return predicted_y


if __name__ == '__main__':
    app.run()


