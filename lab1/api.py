from flask import Flask, request, jsonify
from directory import Directory
from binaryFile import BinaryFile
from logFile import LogFile
from bufferFile import BufferFile
import json

app = Flask(__name__)
root = Directory('root', 100)
content = 'binary content'
binary = BinaryFile('binary file', root, content)
size = 100
buffer = BufferFile('buffer file', root, size)
maxElements = 100
directory = Directory('dirname', maxElements)
directory.move(root)
log = LogFile('log file', root)
another_dir = Directory('d', maxElements, root)
dir_for_delete = Directory('dir5', 100)
dir_for_delete.move(another_dir)
dir1  = Directory('dir1', 100, root)
dir2 = Directory('dir2', 100)
dir2.move(dir1)
#directory
#create
@app.route('/directory', methods=['POST'])
def createDir():
    if request.method == 'POST':
        name = str(request.args.get('name'))
        size = int(request.args.get('max_elems'))
        new_dir = Directory(name, size)
        new_dir.move(root)
    return jsonify({
         "message": "Directory created.",
         "dir_name": new_dir.name,
         "max_elems": new_dir.dir_max_elem})

#move
@app.route('/directory', methods=['PATCH'])
def moveDir():
    if request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.files):
        if any(dir.name == request.args.get('path') for dir in root.files):
            path = next(x for x in root.files if x.name == request.args.get('path'))
            dir = next(x for x in root.files if x.name == request.args.get('name'))
            dir.move(path)
            return jsonify({
         "message": "Directory moved.",
         "directory": {
            "head": str(dir.head.name),
            "name": str(dir.name)  
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400

#read
@app.route('/directory', methods=['GET'])
def readDir():
    if any(dir.name == request.args.get('name') for dir in root.files) or request.args.get('name') == 'root':
        if request.args.get('name') == 'root':
            dir = root
        else:
            dir = next(x for x in root.files if x.name == request.args.get('name'))
        return jsonify({
         "message": "Directory read",
         "directory": {
            "head": str(dir.head.name),
            "name": str(dir.name),
            "max_elems": int(dir.dir_max_elem),            
            "files": str(dir.files)  
         }
        }), 200
    return jsonify({
         "message": "Directory doesn't exist.",
         }), 400

#delete
@app.route('/directory', methods =['DELETE'])
def delDir():
    if request.method == 'DELETE':
        name = str(request.args.get('name'))
        i = 0
        while(i < root.elementsCount):
            if name == root.files[i].name:
                root.files[i].delete()
            i += 1
    return jsonify({
        "message": 'Directory deleted.',
    })

#binary file
#create
@app.route('/binaryfile', methods=['POST'])
def createBinary():
    if request.method == 'POST':
        name = str(request.args.get('name'))
        new_file = BinaryFile(name, root, request.args.get('content'))
        new_file.move(root)
    return jsonify({
         "message": "Binary file created.",
         "name": new_file.name})
#move
@app.route('/binaryfile', methods=['PATCH'])
def moveBinary():
    if request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.files):
        if any(dir.name == request.args.get('path') for dir in root.files):
            path = next(x for x in root.files if x.name == request.args.get('path'))
            dir = next(x for x in root.files if x.name == request.args.get('name'))
            dir.move(path)
            return jsonify({
         "message": "Binary moved.",
         "directory": {
            "head": str(dir.head.name),
            "name": str(dir.name)  
         }
      }), 200
      return jsonify({
         "message": "Binary doesn't exist.",
         }), 400
#delete
@app.route('/binaryfile', methods =['DELETE'])
def deleteBinary():
    if request.method == 'DELETE':
        name = str(request.args.get('name'))
        i = 0
        while(i < root.elementsCount):
            if name == root.files[i].name:
                root.files[i].delete()
            i += 1
    return jsonify({
        "message": 'Binary is deleted.',
    })
#read
@app.route('/binaryfile', methods=['GET'])
def readBinary():
    if any(dir.name == request.args.get('name') for dir in root.files) or request.args.get('name') == 'root':
        if request.args.get('name') == 'root':
            dir = root
        else:
            dir = next(x for x in root.files if x.name == request.args.get('name'))
        return jsonify({
         "message": "Binary read",
         "directory": {
            "head": str(dir.head.name),
            "name": str(dir.name),
            "content": str(dir.content)
         }
        }), 200
    return jsonify({
         "message": "Binary doesn't exist.",
         }), 400

#buffer file
#create
@app.route('/bufferfile', methods=['POST'])
def createBuffer():
    if request.method == 'POST':
        name = str(request.args.get('name'))
        new_file = BufferFile(name, root, int(request.args.get('size')))
        new_file.move(root)
    return jsonify({
         "message": "Buffer file created.",
         "name": new_file.name,
         "size": new_file.max_elem})
#move
@app.route('/bufferfile', methods=['PATCH'])
def moveBuffer():
    if request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.files):
        if any(dir.name == request.args.get('path') for dir in root.files):
            path = next(x for x in root.files if x.name == request.args.get('path'))
            dir = next(x for x in root.files if x.name == request.args.get('name'))
            dir.move(path)
            return jsonify({
         "message": "Buffer moved.",
         "buffer": {
            "head": str(dir.head.name),
            "name": str(dir.name)  
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400
#delete
@app.route('/bufferfile', methods =['DELETE'])
def deleteBuffer():
    if request.method == 'DELETE':
        name = str(request.args.get('name'))
        i = 0
        while(i < root.elementsCount):
            if name == root.files[i].name:
                root.files[i].delete()
            i += 1
    return jsonify({
        "message": 'Buffer is deleted.',
    })
#read
@app.route('/bufferfile', methods=['GET'])
def readBuffer():
    if any(dir.name == request.args.get('name') for dir in root.files) or request.args.get('name') == 'root':
        if request.args.get('name') == 'root':
            dir = root
        else:
            dir = next(x for x in root.files if x.name == request.args.get('name'))
        return jsonify({
         "message": "Buffer read",
         "buffer": {
            "head": str(dir.head.name),
            "name": str(dir.name),
            "content": dir.content
         }
        }), 200
    return jsonify({
         "message": "Buffer doesn't exist.",
         }), 400
#logdile
#create
@app.route('/logfile', methods=['POST'])
def createLogFile():
    if request.method == 'POST':
        name = str(request.args.get('name'))
        new_file = LogFile(name, root)
        new_file.move(root)
    return jsonify({
         "message": "Log file created successfully.",
         "name": new_file.name})

#move
@app.route('/logfile', methods=['PATCH'])
def logfileMove():
    if request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.files):
        if any(dir.name == request.args.get('path') for dir in root.files):
            path = next(x for x in root.files if x.name == request.args.get('path'))
            dir = next(x for x in root.files if x.name == request.args.get('name'))
            dir.move(path)
            return jsonify({
         "message": "Log file moved.",
         "log file": {
            "head": str(dir.head.name),
            "name": str(dir.name)  
         }
      }), 200
      return jsonify({
         "message": "Log file doesn't exist.",
         }), 400
#delete
@app.route('/logfile', methods =['DELETE'])
def logfiledelete():
    if request.method == 'DELETE':
        name = str(request.args.get('name'))
        i = 0
        while(i < root.elementsCount):
            if name == root.files[i].name:
                root.files[i].delete()
            i += 1
    return jsonify({
        "message": 'Log file is deleted.',
    })
#read
@app.route('/logfile', methods=['GET'])
def logfileread():
    if any(dir.name == request.args.get('name') for dir in root.files) or request.args.get('name') == 'root':
        if request.args.get('name') == 'root':
            dir = root
        else:
            dir = next(x for x in root.files if x.name == request.args.get('name'))
        return jsonify({
         "message": "Log file read",
         "buffer": {
            "head": str(dir.head.name),
            "name": str(dir.name),
            "content": dir.content
         }
        }), 200
    return jsonify({
         "message": "Log file doesn't exist.",
         }), 400

if __name__ == '__main__':
    app.run(debug=True)