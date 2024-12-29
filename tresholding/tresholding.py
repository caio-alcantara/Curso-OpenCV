import cv2 as cv 

img = cv.imread("../Photos/group 1.jpg")
cv.imshow("Group", img)

# Tresholding: binarização de imagem 0 - preto, 255 - branco


# Simple:
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simples thresh", thresh)

# Inverse:
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simples thresh inverse", thresh_inv)

# Adaptive:
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive", adaptive_threshold)


cv.waitKey(0)
