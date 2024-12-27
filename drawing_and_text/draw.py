import cv2 as cv
import numpy as np

variavel_nao_utilizada = 4

def draw_rectangle_in_center(img):
    return cv.rectangle(img, (img.shape[1]//4, img.shape[0]//4), (img.shape[1]//2 + img.shape[1]//4, img.shape[0]//2 + img.shape[0]//4), (0, 0, 0), thickness=-1)

def draw_circle_in_center(img):
    return cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 50, (0, 0, 255), thickness=3)

def draw_line(img, x1, y1, x2, y2):
    return cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), thickness=3)

def write_text(img, x, y, text):
    cv.putText(img, text, (x//2, y//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)

blank_img = np.zeros((500, 500, 3), dtype="uint8")

##img = cv.imread("../Photos/cat.jpg")

# Mudar a cor da imagem
blank_img[:] = 255, 255, 255

# Desenhar um retangulo
#cv.rectangle(blank_img, (blank_img.shape[1]//4, blank_img.shape[0]//4), (blank_img.shape[1]//2 + blank_img.shape[1]//4, blank_img.shape[0]//2 + blank_img.shape[0]//4), (0, 0, 0), thickness=-1) ## thickness = -1 preenche retangulo

draw_rectangle_in_center(blank_img)
draw_circle_in_center(blank_img)
draw_line(blank_img, 250, 0, 250, 500)
write_text(blank_img, 225, 225, "Ola, mundo")

cv.imshow("Img", blank_img)
print("OI!")
cv.waitKey(0)
