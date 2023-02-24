#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt

#CREAMOS LA VARIABLE DE LA IMAGEN BASEfire
img = cv2.imread("npfoto/formas.jpg")
#LA CONVERTIMOS A HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV_FULL)
#ELEGIMOS EL UMBRAL DEL COLOR VERDE EN HSV
umbral_bajo1 = (170,100,100)
umbral_alto1 = (179,255,255)

umbral_bajo2 = (0,100,100)
umbral_alto2 = (10,255,255)

#Creamos una mascara y filtramos la imagen original
mask1 = cv2.inRange(img_hsv, umbral_bajo1, umbral_alto1)
mask2 = cv2.inRange(img_hsv, umbral_bajo2, umbral_alto2)
mask = mask1 + mask2
res = cv2.bitwise_and(img, img ,mask = mask)

#Mostramos las imagenes por pantalla
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1,2,2)
plt.imshow(res)
plt.show()  