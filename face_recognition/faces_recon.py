import cv2 as cv 
import numpy as np
import os

people = []
DIR = r"C:\Users\Inteli\Desktop\MedIn\open_cv_course\Faces\train"
for i in os.listdir(DIR):
    people.append(i)

print(people)

haar_cascade = cv.CascadeClassifier("../face_detection/haar_face.xml")

# features = np.load('features.npy')
# labels = np.load('labes.npy')
face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\Inteli\Desktop\MedIn\open_cv_course\Faces\val\mindy_kaling\6.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detecta face na img

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label: {people[label]} com confianca de {confidence}%")

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)

    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)


cv.imshow('Detected face', img)

cv.waitKey(0)


