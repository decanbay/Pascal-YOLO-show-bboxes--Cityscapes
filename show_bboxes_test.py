"""
This little code draws the bounding box on your images. 
A possible scenario is you are coding a parser and want to check it. It first reads your images and 
annotations in PASCAl-VOC format (obj_id x_center y_center box_width box_height   normalized to 0-1 and every object is in a seperate line)
and randomly select an image-annotation pair and draws the boxes on the image.

Feel free to Buy it, use it, break it, fix it, 
Trash it, change it, mail, upgrade it, 
Charge it, point it, zoom it, press it, 
Snap it, work it share it use it crop it copy and paste it.


Istanbul Technical University
Deniz Ekin Canbay
canbay@itu.edu.tr
"""
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import math
import random
import matplotlib.collections as collections
import matplotlib as mpl


IM_PATH="/media/deniz/DATA/CityScapes/leftImg8bit_trainvaltest/leftImg8bit/Cityscapes_all/"
Annot_PATH="/media/deniz/DATA/CityScapes/cityscape2pascal/cityscape/"

w=2048 # image width     size(cv2.imread())   but i am too lazy 
h=1024 # image height


files=os.listdir(IM_PATH)

imname=files[random.randint(0,len(files))]
impath=IM_PATH+imname

lines = [line.rstrip('\n') for line in open(Annot_PATH+imname.split(".")[0]+".txt", 'r')]

im = np.array(Image.open(impath), dtype=np.uint8)

fig, ax = plt.subplots(figsize = (12,6))
ax.set_xlim(0,w)
ax.set_ylim(h,0)
plt.imshow(im)

gt_boxes=[]
for ind in range(len(lines)):
    cx = float(lines[ind].split(" ")[1])
    cy = float(lines[ind].split(" ")[2])
    ww = float(lines[ind].split(" ")[3])
    hh = float(lines[ind].split(" ")[4]) 
    x = math.floor((cx - ww/2)*w)
    y = math.floor((cy - hh/2)*h)
    ww *=w
    hh*= h

# Create a Rectangle patch
    rect = mpl.patches.Rectangle((x,y),ww,hh,linewidth=1,edgecolor='r',fill=False)
    gt_boxes.append(rect)
    ax.add_patch(rect)
    
plt.show()
print(imname)


