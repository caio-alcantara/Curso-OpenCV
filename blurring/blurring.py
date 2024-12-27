import cv2 as cv

img = cv.imread("../Photos/cats.jpg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow("Average", average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian", gauss)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bileteral blue
bileteral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bileteral", bileteral)

cv.waitKey(0)

