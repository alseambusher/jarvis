import os
import subprocess
import sqlite3
from config import DB

def _exe(command):
    os.system(command+"&")

def pipe(command,kind='str'):
    #TODO this will be executed in some other shell which should not happen. Think of some way to fix this and run in current shell
    if kind=='str':
        return subprocess.Popen(command,shell=False,stdout=subprocess.PIPE).stdout.readlines()[0][1:-2]
    else:
        return subprocess.Popen(command,shell=False,stdout=subprocess.PIPE).stdout.readlines()

def db_connect():
    return sqlite3.connect(DB)

class dummy_object():#this is just a dummy object
    pass

def dummy_func():
    pass

