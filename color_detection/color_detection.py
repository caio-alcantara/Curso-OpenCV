import cv2 as cv 
import numpy as np 

## Lendo vídeos
capture = cv.VideoCapture(0) ## Pode passar 0 como argumento para acessar webcam

while True:
    isTrue, frame = capture.read()
    # cv.imshow('Video', frame)
    frame = cv.resize(frame, (640, 480))    
    frame = cv.flip(frame, 1)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    if cv.waitKey(20) & 0xff == ord('q'):
        break

    
    lower_blue = np.array([94, 31, 0])
    higher_blue = np.array([159, 255, 255])
    

    kernel = np.ones((5,5), np.uint8)
    mask = cv.inRange(hsv, lower_blue, higher_blue)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    result = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("result", result)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv.contourArea(x), reverse=True)
    
    x_medium = 0

    if contours:
        print("Objeto detectado!")
        cv.putText(frame, "Objeto detectado!", (50, 350), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
        for cnt in contours:
            if cv.contourArea(cnt) > 500:
                (x, y, w, h) = cv.boundingRect(cnt)
                x_medium = int(x + w / 2)
                break
    else:
        print("Nenhum objeto detectado.")
        cv.putText(frame, "Nenhum objeto detectado!", (50, 350), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)

    cv.putText(frame, f"Posicao: {x_medium}", (50, 450), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)

            
    cv.line(frame, (x_medium, 0), (x_medium, 640), (255, 0, 0), 2)

    cv.imshow("Frame", frame)

capture.release()
cv.destroyAllWindows()


