from flask import Flask, request
import json
from flask_restful import Resource, Api
from directory import Directory
from binaryFile import BinaryFile
from logFile import LogFile
from bufferFile import BufferFile

app = Flask(__name__)
api = Api(app)

root = Directory('root', 100)
content = 'binary content'
binary = BinaryFile('binary file', root, content)
size = 100
buffer = BufferFile('buffer file', root, size)
maxElements = 100
directory = Directory('dirname', maxElements)
log = LogFile('log file', root)

class DirectoryApi(Resource):
    def init(self):
        self.directory = directory
    def post(self):
        data = request.get_json()
        self.directory = Directory(data["name"], data["maxElements"])
        return {'message': 'Directory is created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.directory.move(fatherDir)
    def delete(self):
        return self.directory.delete()

class BinaryApi(Resource):
    def init(self):
        self.binary = binary
    def get(self):
        return self.binary.read()
    def post(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        self.binary = BinaryFile(data["fileName"], data["content"], fatherDir)
        return {'message': 'BinaryFile is successfully created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.binary.move(fatherDir)
    def delete(self):
        return self.binary.delete()

class BufferApi(Resource):
    def init(self):
        self.buffer = buffer
    def get(self):
        return self.buffer.consume()
    def post(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        self.buffer = BufferFile(data["fileName"], data["maxSize"], fatherDir)
        return {'message': 'BufferFile is created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.buffer.move(fatherDir)
    def patch(self):
        data = json.loads(request.data)
        return self.buffer.push(data["element"])
    def delete(self):
        return self.buffer.delete()


class logTextApi(Resource):
    def init(self):
        self.logText = LogFile
    def get(self):
        return self.logText.read()
    def post(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        self.logText = LogFile(data["fileName"], fatherDir)
        return {'message': 'LogFile is created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.logText.move(fatherDir)
    def patch(self):
        data = request.get_json()
        return self.logText.log(data["line"])
    def delete(self):
        return self.logText.delete()

api.add_resource(BinaryApi, '/binaryfile')
api.add_resource(BufferApi, '/bufferfile')
api.add_resource(DirectoryApi, '/directory')
api.add_resource(logTextApi, '/logtextfile')

if __name__ == '__main__':
    app.run(debug=True)