import cv2 as cv

## Lendo imgs
#cat_photo = cv.imread('../Photos/cat.jpg')

#cv.imshow('Cat', cat_photo)

## Lendo vídeos
capture = cv.VideoCapture(0) ## Pode passar 0 como argumento para acessar webcam

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)