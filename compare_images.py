import cv2
import argparse
import glob
import numpy as np

IMG_PATH = "./JPEGImages/*"
THRESH = 65 


def compare(img1, img2):
    """ 
        Compare two OpenCV images and return the 
        percentage of similarity of the images (0 - 100%)
    """
    # Set img2 to img1 shape to compare
    height = img1.shape[0]
    width = img1.shape[1]
    img2 = cv2.resize(img2, (width, height))
    #--- take the absolute difference of the images ---
    res = cv2.absdiff(img1, img2)
    #--- convert the result to integer type ---
    res = res.astype(np.uint8)
    #--- find percentage difference based on number of pixels that are zero ---
    percentage = 100 - ((np.count_nonzero(res) * 100)/ res.size)
    
    return percentage
    
    
if __name__ == '__main__':
    
    img_list = glob.glob(IMG_PATH)
    print("[INFO] - Comparison started !", len(img_list), "images to compare")
    for i in range (0, len(img_list)):
        for j in range (i+1, len(img_list)):
            img1 = cv2.imread(img_list[i], 0)
            img2 = cv2.imread(img_list[j], 0)
            cmp = compare(img1, img2)
            print(cmp)
            if cmp > THRESH:
                print('[INFO] - Images are very close to each other, >', THRESH,'% : ', img_list[i], ' -----', img_list[2])
                
          
    print("[INFO] - Comparison finished !")
    
    
    
    
    
    
    
    