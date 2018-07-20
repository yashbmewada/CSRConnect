from flask import Flask,jsonify

import pymongo
import json
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.CSRConnect


app = Flask(__name__)


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
    print(final)
    return jsonify(final)



if __name__ == '__main__':
    app.run()


