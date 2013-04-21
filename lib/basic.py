import os
import subprocess
import sqlite3
from config import DB

def _exe(command):
    os.system("bash -c '"+command+"&'")

def pipe(command,kind='str'):
    if kind=='str':
        return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()[0][1:-2]
    else:
        return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()

def db_connect():
    return sqlite3.connect(DB)

class dummy_object():#this is just a dummy object
    pass

def dummy_func():
    pass

