import matplotlib.pyplot as plt 
import cv2
from skimage.transform import swirl 

image = cv2.imread('image/marvel.jpg')
swirled = swirl(image, rotation=0, strength=10, radius=500) 
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), sharex=True, sharey=True) 

ax0.imshow(image, cmap=plt.cm.gray) 
ax0.axis('off') 
ax1.imshow(swirled, cmap=plt.cm.gray) 
ax1.axis('off') 

plt.show()