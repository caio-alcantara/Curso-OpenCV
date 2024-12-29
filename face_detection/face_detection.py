import cv2 as cv 

img = cv.imread("./mororos.png")
cv.imshow("Lady", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier("./haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Numero de faces detectadas: {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0), thickness=2)

cv.imshow("Faces", img)


cv.waitKey(0)
