import cv2 as cv 
import numpy as np 

img = cv.imread("../Photos/cat.jpg")
blank = np.zeros(img.shape, dtype='uint8')

cv.imshow("Cat", img)
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale img", gray)

ret, tresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Treshold", tresh)


contours, hierarchies = cv.findContours(tresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(len(contours)) ## Quantidade de contornos

cv.drawContours(blank, contours, -1, (255,255,255), thickness=2)
cv.imshow("Contours drawn", blank)

cv.waitKey(0)
