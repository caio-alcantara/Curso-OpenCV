import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #imagens, videos, capturas ao vivo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #capturas ao vivo apenas
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread("../Photos/cat_large.jpg")
resized_img = rescaleFrame(img, scale=0.3)

cv.imshow('Cat', resized_img)

cv.waitKey(0)

# capture = cv.VideoCapture('../Videos/dog.mp4') ## Pode passar 0 como argumento para acessar webcam

# while True:
#     isTrue, frame = capture.read()
    
#     resized_frame = rescaleFrame(frame, scale=0.5)
    
#     cv.imshow('Video', resized_frame)
#     if cv.waitKey(20) & 0xff == ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()