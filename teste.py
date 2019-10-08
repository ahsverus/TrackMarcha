import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Tracking') # janela para escolher os valores do hsv
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)# 0(minimo) -- 255(maximo)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('bolinhas.jpg') # ler a imagem
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# transformar a imagem de rgb para hsv

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v]) # esse valor pega o range minimo
    u_b = np.array([u_h, u_s, u_v]) # esse valor pega o range maximo

    mask = cv2.inRange(hsv, l_b , u_b) # cria a mascara (imagem preta e branca) -- transforma a cor escolhida em preto
    res = cv2.bitwise_and(frame, frame, mask=mask)# aplica a mascara na imagem -- tudo que era branco na mascara é deletado

    cv2.imshow('frame', frame)# apenas mostrar
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()