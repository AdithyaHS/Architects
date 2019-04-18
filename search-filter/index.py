from flask import Flask, jsonify, request, url_for
import json
import pprint
from flask import render_template
from flask_cors import CORS
#from flask_pymongo import PyMongo
from bson.json_util import dumps
import pymongo
import ssl
#from ZooKeeperHandler import ZookeeperHandler

#create an instance of the Flask class for our web app
app=Flask(__name__)
CORS(app)

#Configurations for MongoDB
projectsTableURI = 'mongodb://DHANUMAN:Target2018atiub@ds113855.mlab.com:13855/project_add'
UsermanagementURI= 'mongodb+srv://hsadi:adash569@cluster0-5zv82.mongodb.net/test?retryWrites=true'




client = pymongo.MongoClient("mongodb://hsadi:adash569@cluster0-shard-00-00-5zv82.mongodb.net:27017,cluster0-shard-00-01-5zv82.mongodb.net:27017,cluster0-shard-00-02-5zv82.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

#client = MongoClient(projectsTableURI)
#client1= MongoClient(UsermanagementURI)

#connecting to databases
#db = client.project_add
db1=client["user_management"]
print(db1)
#creation of indexes
#db.project.create_index([('$**', 'text')])
#db1.users.create_index([('$**', 'text')])

#Create Routes
if __name__ == '__main__':
    # zk=ZookeeperHandler();
    # zk.registerAuthService('149.165.171.39','5000');

    app.run(debug=True,host='0.0.0.0')
