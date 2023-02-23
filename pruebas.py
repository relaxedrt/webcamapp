#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt

#CREAMOS LA VARIABLE DE LA IMAGEN BASE
img = cv2.imread("formas.jpg")
#LA CONVERTIMOS A HSV
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV_FULL)
#ELEGIMOS EL UMBRAL DEL COLOR VERDE EN HSV
umbral_bajo = (70,100,100)
umbral_alto = (80,255,255)

#Creamos una mascara y filtramos la imagen original
mask = cv2.inRange(img_hsv, umbral_bajo, umbral_alto)
res = cv2.bitwise_and(img, img ,mask = mask)

#Mostramos las imagenes por pantalla
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1,2,2)
plt.imshow(res)
plt.show()


""" plt.imshow(img_hsv)
plt.show() """