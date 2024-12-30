import os 
import cv2 as cv 
import numpy as np 

haar_cascade = cv.CascadeClassifier("../face_detection/haar_face.xml")

people = []
DIR = r"C:\Users\Inteli\Desktop\MedIn\open_cv_course\Faces\train"
for i in os.listdir(DIR):
    people.append(i)

print(people)


features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

features = np.array(features, dtype='object')
labels = np.array(labels)

print(len(features), len(labels))

face_recognizer = cv.face.LBPHFaceRecognizer.create()

# Treinar o modelo
face_recognizer.train(features, labels)

np.save('features.npy', features)
np.save('labes.npy', labels)
face_recognizer.save('face_trained.yml')
