import cv2 as cv

img = cv.imread("../Photos/cat.jpg")

cv.imshow("Cat", img)

# Converter para grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (11,11), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
resize = cv.resize(img, (500, 500))
cv.imshow("Resized", resize)

# Cropping
crop = img[50:200, 200:400]
cv.imshow("Crop", crop)

cv.waitKey(0)
