from flask import Flask, request
import json
from flask_restful import Resource, Api
from directory import Directory 
from binaryFile import BinaryFile
from logFile import LogFile
from bufferFile import BufferFile

app = Flask(__name__)
api = Api(app)


class BinaryApi(Resource):
    def init(self):
        pass 
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

class BufferApi(Resource):
    def init(self):
       pass
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass

class DirectoryApi(Resource):
    def init(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

class logTextApi(Resource):
    def init(self):
        pass
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass


if __name__ == 'main':
    app.run(debug=True)