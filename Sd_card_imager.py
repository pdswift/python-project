import os
import sys
import copy
import shutil, errno
path = 'S:/'
os.chdir('S:/')
print: os.getcwd()
dirpath = os.getcwd()
print("current directory is : " + dirpath)
cp = copy.deepcopy('S:/')
sys.stdout = open('boot.img', 'w')
