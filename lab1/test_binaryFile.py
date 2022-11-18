from binaryFile import BinaryFile
from directory import Directory
import pytest
from array import array

#binary file tests

def test_binaryFile_init():
    rootDirectory = Directory('rootDirectroty', 5)
    binaryFile = BinaryFile('test_binary_file', rootDirectory, 'text content')

    assert binaryFile.name == 'test_binary_file'
    assert binaryFile.head == rootDirectory
    assert binaryFile.content == 'text content'

def test_binaryFile_delete():
    binaryFile = BinaryFile('test_binary_file', None, 'text content')
    del binaryFile
    assert 'binaryFile' not in locals()

def test_binaryFile_read():
    binaryFile = BinaryFile('test_binary_file', None, 'text content')
    assert binaryFile.readContent() == 'text content'

def test_binaryFile_move():
    rootDirectory = Directory('rootDirectroty', 5)
    binaryFile = BinaryFile('test_binary_file', None, 'text content')
    binaryFile.move(rootDirectory)
    assert binaryFile.head == rootDirectory

