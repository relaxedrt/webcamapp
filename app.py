#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt

#Abrimos la camara
cam = cv2.VideoCapture(0)

#Guardamos el frame en una variable y si a leido bien o no en otra
leido, frame = cam.read()

#ELEGIMOS EL UMBRAL DEL COLOR AZUL EN HSV
umbral_bajo1 = (85,100,20)
umbral_alto1 = (135,255,255)

#Evaluamos si se consiguio sacar la foto y la mostramos
if leido == True:
    #Mostramos el resultado
    print("Foto tomada correctamente.")
    print("Foto siendo procesada.")
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mask1 = cv2.inRange(img, umbral_bajo1, umbral_alto1)
    res = cv2.bitwise_and(img, img ,mask = mask1)
    plt.imshow(res)
    plt.show()
    print("Resultado mostrado.")
else:
    print("Error al acceder a la camara.")

#Cerramos la webcams
cam.release()

