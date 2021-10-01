import glob
import os

"""
    Let's you see what images are left to annotate
    works only on windows (I guess)
"""
if __name__ == '__main__':
    path = "JPEGImages"
    filenames = glob.glob(os.path.join(path, "*"))
    ann_path = "annotations"
    img_count = 0
    
    for filename in filenames:
        ann_name = filename.split("\\")[-1].split(".")[0]+".xml"
        found = len(glob.glob(os.path.join(ann_path, ann_name)))>0
        if not found:
            print(filename)
            img_count += 1
        
    print(len(filenames)- (img_count),"/",len(filenames), "annotated images")
    print(img_count, "images left")
