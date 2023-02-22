#pip install opencv-python
import cv2
#Cada camara sera un numero desde 0 hasta n
cap = cv2.VideoCapture(1)
#En leido guardaremos si saco la foto o no y en frame la foto
leido, frame = cap.read()
#Gestionamos el resultado
if leido == True:
    cv2.imwrite("foto.png", frame)
    print("Foto tomada correctamente")
else:
    print("Error al acceder a la camara")
#Cerramos la webcam
cap.release()