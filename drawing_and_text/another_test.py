import cv2 as cv

img = cv.imread('../Photos/cat.jpg')

cv.imshow('Img', img)
cv.waitKey(0)
