import cv2 as cv
import numpy as np
## Translation, resizing, clipping and cropping

img = cv.imread("../Photos/cat.jpg")

cv.imshow('Cat', img)

# Translation
def translate(img, x, y):
    translation_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, translation_matrix, dimensions)

translated_image = translate(img, 100, 100)
cv.imshow("Translated img", translated_image)

# Rotation
def rotate(img, angle, rotation_point=None):
    (height, widht) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (widht//2, height//2)
    
    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (widht, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated_img = rotate(img, 45)
cv.imshow("Rotated img", rotated_img)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized img", resized)

# Flipping 
flip = cv.flip(img, 1)
cv.imshow("Flip img", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped img", cropped)

cv.waitKey(0)

