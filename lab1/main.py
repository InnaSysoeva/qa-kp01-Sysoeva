from directory import Directory
from binaryFile import BinaryFile
from logFile import LogFile
from bufferFile import BufferFile
from fileSystem import FileSystem


#creating file system
fileSystem = FileSystem('File system', 100)

#creating directory and move it into file system
dir1 = Directory('dir1', 5)
fileSystem.addFile(dir1)

#adding nested directory into dir1
dir2 = Directory('dir2', 3)
dir3 = Directory('dir3', 10)
dir2.move(dir1)
dir3.move(dir1)

#checking directory in dir1
print('List of files in `dir1`')
dir1.read()

#adding more files into dir1
buffer1 = BufferFile('buffer1', dir1, 3)
binary1 = BinaryFile('binary1', dir1, 'some text')
log1 = LogFile('log1', dir1)

#checking files in dir1
print('List of files in `dir1`')
dir1.read()

#adding content into files in dir1
buffer1.push('some buffer text')
buffer1.push('another buffer text')
log1.addLog('first log')
log1.addLog('second log')
log1.addLog('third log')

#checking content of files in dir1
print('Content in `log`')
print(log1.read())

#moving file 'binary1' from dir1 to dir3
binary1.move(dir3)
print('Files in dir1')
dir1.read()
print('Files in dir3')
dir3.read()

#add several files into dir3
binary2 = BinaryFile('binary2', dir3, '1234567890')
log2 = LogFile('log2', dir3)
log3 = LogFile('log3', dir3)
print('Files in dir3')
dir3.read()