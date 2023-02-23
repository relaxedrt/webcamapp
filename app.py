#IMPORTAMOS LAS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt

#Abrimos la camara
cam = cv2.VideoCapture(0)

#Guardamos el frame en una variable y si a leido bien o no en otra
leido, frame = cam.read()

#Evaluamos si se consiguio sacar la foto y la mostramos
if leido == True:
    #Mostramos el resultado
    print("Foto tomada correctamente")
    plt.imshow(frame)
    plt.show()
else:
    print("Error al acceder a la camara")

#Cerramos la webcams
cam.release()

