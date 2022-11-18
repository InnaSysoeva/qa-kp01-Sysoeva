from bufferFile import BufferFile
from directory import Directory
import pytest
from array import array

#buffer file tests
def test_bufferFile_init():
    rootDirectory = Directory('rootDirectroty', 5)
    bufferFile = BufferFile('test_buffer_file', rootDirectory, 5)

    assert bufferFile.name == 'test_buffer_file'
    assert bufferFile.head == rootDirectory
    assert bufferFile.max_elem == 5


def test_bufferFile_move():
    rootDirectory = Directory('rootDirectroty', 5)
    bufferFile = BufferFile('test_buffer_file', None, 5)
    bufferFile.move(rootDirectory)
        
    assert bufferFile.head == rootDirectory

def test_bufferFile_delete():
    rootDirectory = Directory('rootDirectroty', 5)
    bufferFile = BufferFile('test_buffer_file', rootDirectory, 5)
    
    del bufferFile
    assert 'bufferFile' not in locals()

def test_bufferFile_addElem():
    rootDirectory = Directory('rootDirectroty', 5)
    bufferFile = BufferFile('test_buffer_file', rootDirectory, 5)

    bufferFile.push('text')

    assert bufferFile.content[0] == 'text'

def test_bufferFile_consumeElem():
    rootDirectory = Directory('rootDirectroty', 5)
    bufferFile = BufferFile('test_buffer_file', rootDirectory, 5)

    bufferFile.push('text')
    bufferFile.push('text2')
    bufferFile.consume()

    assert bufferFile.content[0] == 'text2'
