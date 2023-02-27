#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import cv2

#CREAMOS LA VARIABLE DE LA IMAGEN BASE
img = cv2.imread("npfoto/formas.jpg")
#LA CONVERTIMOS A HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV_FULL)
#ELEGIMOS EL UMBRAL DEL COLOR VERDE EN HSV
umbral_bajo = (70,100,100)
umbral_alto = (80,255,255)

while True:
    #Creamos una mascara y filtramos la imagen original
    mask = cv2.inRange(img_hsv, umbral_bajo, umbral_alto)
    res = cv2.bitwise_and(img, img ,mask = mask)
    #res_rgb = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    res_rgb = img
    #Encontramos los contornos y los dibujamos en la imagen que queremos
    contorno, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contorno:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(res_rgb, [i], -1, (0,255,0), 2)
            cv2.circle(res_rgb, (cx,cy), 7, (0,0,255), -1)
            cv2.putText(res_rgb, f"x: {cx} y:{cy}", (cx -20, cy -20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    cv2.imshow('res', res_rgb)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
print(f"x: {cx}\n y:{cy}")

