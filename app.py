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
    print("---------")
    print(type(id))
    cursor = collection.find({'id':int(id)},{'_id':0})
    for document in cursor:
        final.append(document)
    return jsonify(final)




if __name__ == '__main__':
    app.run()
