import glob
import hashlib
import os

filenames = glob.glob("./*.jpg")
filenames += glob.glob("./*.jpeg")

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        os.rename(filename, hashlib.md5(data).hexdigest() + ".jpg")
