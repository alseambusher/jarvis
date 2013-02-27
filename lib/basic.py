import os
import subprocess

def _exe(command):
    os.system(command)

def pipe(command,kind='str'):
    #TODO this will be executed in some other shell which should not happen. Think of some way to fix this and run in current shell
    if kind=='str':
        return subprocess.Popen(command,shell=False,stdout=subprocess.PIPE).stdout.readlines()[0][1:-2]
    else:
        return subprocess.Popen(command,shell=False,stdout=subprocess.PIPE).stdout.readlines()

class dummy_object():#this is just a dummy object
    pass

