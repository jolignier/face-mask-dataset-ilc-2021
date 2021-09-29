import glob
import hashlib
import os

filenames = glob.glob("./JPEGImages/*.jpg")
filenames += glob.glob("./JPEGImages/*.jpeg")
filenames += glob.glob("./JPEGImages/*.JPG")
filenames += glob.glob("./JPEGImages/*.JPEG")

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        os.rename(filename, "./JPEGImages/" + hashlib.md5(data).hexdigest() + ".jpg")
