import os
import subprocess

def _exe(command):
    os.system(command)

def pipe(command):
    #TODO this will be executed in some other shell which should not happen. Think of some way to fix this
    return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).stdout.readlines()[0][1:-2]

