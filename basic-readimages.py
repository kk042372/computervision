
#read images
import matplotlib.image as mpimg

# import computer vision library
import cv2

import matplotlib.pyplot as plt

%matplotlib qt

#read the image
image = mpimg.imread('images/<car>.jpg')  #FIX THIS

#print the dimensions
print('Image dimensions: ', image.shape)

# change from color to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.imshow(gray_image, cmap='gray')

#print a pixel
x=190
y=375
pixel_val = gray_image[y, x]

print(pixel_val)
