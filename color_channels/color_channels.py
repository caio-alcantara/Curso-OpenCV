import cv2 as cv 
import numpy as np 

# Ex: separar uma imagem BGR em azul, verde e vermelho

img = cv.imread("../Photos/park.jpg")
cv.imshow("Park", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b,blank,blank])
cv.imshow("blue", blue)

cv.imshow("Blue", b)
cv.imshow("Red", r)
cv.imshow("Gren", g)

merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)



cv.waitKey(0)
