import glob
import hashlib
from pathlib import Path
import os


# Check if path exist
path = "JPEGImages"
if Path(path).is_file():
    print("[ERROR] Path not found: 'JPEGImages'")
    quit()

# Append pictures
file_names = glob.glob(os.path.join(path, "*.jpg"))
file_names += glob.glob(os.path.join(path, "*.jpeg"))
file_names += glob.glob(os.path.join(path, "*.JPG"))
file_names += glob.glob(os.path.join(path, "*.JPEG"))
file_names += glob.glob(os.path.join(path, "*.png"))

# Iterate on all picture for get md5sum
file_old = []
file_new = []
for filename in file_names:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        file_old.append(os.path.basename(filename))
        file_new.append(hashlib.md5(data).hexdigest() + os.path.splitext(filename)[1])
        print("file_old {}".format(file_old[-1]))
        print("file_new {}".format(file_new[-1]))

    # Move original name to md5sum name
    os.rename(os.path.join(path, file_old[-1]), os.path.join(path, file_new[-1]))
