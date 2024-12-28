import cv2 as cv 
import numpy as np 

# Masking: focar em determinadas partes de uma imagem (rostos, cores, etc)

img = cv.imread("../Photos/park.jpg")
cv.imshow("Park", img)
blank = np.zeros(img.shape[:2], dtype="uint8") # Tamanho tem que ser igual ao da img

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, thickness=-1)
cv.imshow("mask", mask)


masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked img", masked_image)


cv.waitKey(0)
