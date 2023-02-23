#pip install opencv-python
import cv2
import datetime as dt
import locale
#Cada camara sera un numero desde 0 hasta n
cap = cv2.VideoCapture(0)
locale.setlocale(locale.LC_ALL, '')
#En leido guardaremos si saco la foto o no y en frame la foto
leido, frame = cap.read()
fecha_actual = dt.datetime.now()
name = fecha_actual.strftime('%Y%m%d%H%M')
#Gestionamos el resultado

if leido == True:
    cv2.imwrite(f"npfoto\{name}.png", frame)
    print("Foto tomada correctamente")
else:
    print("Error al acceder a la camara")
#Cerramos la webcam
cap.release()