#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt

#Abrimos la camara
cam = cv2.VideoCapture(0)

#Guardamos el frame en una variable y si a leido bien o no en otra
leido, frame = cam.read()

#ELEGIMOS EL UMBRAL DEL COLOR AZUL EN HSV
umbral_bajo1 = (170,100,100)
umbral_alto1 = (179,255,255)

umbral_bajo2 = (0,100,100)
umbral_alto2 = (10,255,255)
#Evaluamos si se consiguio sacar la foto y la mostramos
if leido == True:
    #Mostramos el resultado
    print("Foto tomada correctamente.")
    print("Foto siendo procesada.")
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(img, umbral_bajo1, umbral_alto1)
    mask2 = cv2.inRange(img, umbral_bajo2, umbral_alto2)
    mask = mask1 + mask2
    res = cv2.bitwise_and(img, img ,mask = mask)
    res_rgb = cv2.cvtColor(res, cv2.COLOR_HSV2RGB)
    #Mostramos las imagenes por pantalla
    plt.subplot(1, 2, 1)
    plt.imshow(mask1, cmap="gray")
    plt.subplot(1,2,2)
    plt.imshow(res_rgb)
    plt.show()
    print("Resultado mostrado.")
else:
    print("Error al acceder a la camara.")

#Cerramos la webcams
cam.release()

