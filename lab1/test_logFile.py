from logFile import LogFile
from directory import Directory
import pytest
from array import array

#log file tests
def test_init_logFile():
    rootDirectory = Directory('rootDirectroty', 5)
    logFile = LogFile('test_log_file', rootDirectory)
    
    assert logFile.name == 'test_log_file'
    assert logFile.head == rootDirectory

def test_delete_logFile():
    rootDirectory = Directory('rootDirectroty', 5)
    logFile = LogFile('test_log_file', rootDirectory)
    
    del logFile
    assert 'logFile' not in locals()

def test_move_logFile():
    rootDirectory = Directory('rootDirectroty', 5)
    logFile = LogFile('test_log_file', None)
    logFile.move(rootDirectory)
    assert logFile.head == rootDirectory
    assert rootDirectory.files[0] == logFile

def test_addLog():
    logFile = LogFile('test_log_file', None)
    logFile.addLog('log1')
    logFile.addLog('log2')
    logFile.addLog('log3')
    assert logFile.content == 'log1' + '\n' + 'log2' + '\n' + 'log3' + '\n'





