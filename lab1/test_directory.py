from directory import Directory
import pytest
from array import array

#directory tests
def test_init_dir():
    name = 'test_directory'
    maxElem = 5
    directory = Directory('test_directory', 5)

    assert directory.name == name
    assert directory.elementsCount == 0
    assert directory.dir_max_elem  == maxElem

def test_delete_dir():
    directory = Directory('test_directory', 5)
    del directory
    assert 'directory' not in locals()

def test_move_dir():
    rootDirectory = Directory('rootDirectroty', 5)
    directory = Directory('test_directory', 5)
    directory.move(rootDirectory)
    assert directory.head == rootDirectory
    assert rootDirectory.files[0] == directory

