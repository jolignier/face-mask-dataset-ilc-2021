import glob
import hashlib
import os

# if os.path.exists(os.path.normpath("./JPEGImages/")):
#     print("[ERROR] Path not found: 'JPEGImages'")
#     quit()

path = "JPEGImages"
filenames = glob.glob(os.path.join(path, "*.jpg"))
filenames += glob.glob(os.path.join(path, "*.jpeg"))
filenames += glob.glob(os.path.join(path, "*.JPG"))
filenames += glob.glob(os.path.join(path, "*.JPEG"))

file_old = []
file_new = []

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        file_old.append(os.path.basename(filename))
        file_new.append(hashlib.md5(data).hexdigest() + os.path.splitext(filename)[1])

        print("file_old {}".format(file_old[-1]))
        print("file_new {}".format(file_new[-1]))
    os.rename(os.path.join(path, file_old[-1]), os.path.join(path, file_new[-1]))
