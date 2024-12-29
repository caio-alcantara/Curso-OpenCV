import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../Photos/cats 2.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, 1)
# Histogramas: distribuição da intensidade de pixeis numa imagem 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

mask = cv.bitwise_and(gray, gray, mask=circle)

# Histogram grayscale
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title("Histograma Grayscale")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color Histogram

colors = ('b', 'g', 'r')

for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim(0, 256)
plt.show()

cv.waitKey(0)
