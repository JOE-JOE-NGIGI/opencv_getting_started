import numpy as np 
import cv2


#load image file. 1 is for color, 0 is grayscale
img = cv2.imread('lena.jpg',1)

#Function to draw line
#first argument = cordinate of the line
#second argument
img = cv2.line(img, (0,255), (255,255), (0, 0, 255), 5)

#draw rectangle
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 5)

#display the image
cv2.imshow('image',img)

#user input character 0 to quit
cv2.waitKey(0)
cv2.destroyAllWindows()