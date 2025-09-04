#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('/home/rowan/Downloads/test.jpg')  #change path
out = img.copy()
#color detection

HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_black=np.array([0,0,0])
upper_black=np.array([180,255,50])

lower_blue = np.array([100,50,50])
upper_blue = np.array([130,255,255])

lower_red1 = np.array([0, 120, 70])   
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])



# Make a mask for each color (red, blue, black)
mask_blue = cv2.inRange(HSV_img, lower_blue, upper_blue)
mask_red = cv2.inRange(HSV_img, lower_red1, upper_red1) | cv2.inRange(HSV_img, lower_red2, upper_red2)
mask_black = cv2.inRange(HSV_img, lower_black, upper_black)


# Blue ->black
out[mask_blue > 0] = [0, 0, 0]

# Red ->Blue
out[mask_red > 0] = [255, 0, 0]

# Black ->red
out[mask_black > 0] = [0, 0, 255]
#BGR->RGB 
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out=cv2.cvtColor(out, cv2.COLOR_BGR2RGB)


fig, axes = plt.subplots(1, 2)
axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(out)
axes[1].set_title('Processed Image')
axes[1].axis('off')

plt.show()