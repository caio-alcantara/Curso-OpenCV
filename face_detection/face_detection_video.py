import cv2 as cv 

## Lendo vídeos
capture = cv.VideoCapture(0) ## Pode passar 0 como argumento para acessar webcam

haar_cascade = cv.CascadeClassifier("./haar_face.xml")

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
 
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+w), (0, 255, 0), thickness=2)

    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

