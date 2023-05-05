import cv2
import numpy as np

face_detection = cv2.CascadeClassifier('C:\opencv\data\haarcascades\haarcascade_frontalface_default.xml')

#Cada camara sera un numero desde 0 hasta n
cap = cv2.VideoCapture(0)

while True:
    #Leido = confirmación de lectura, frame = imagen
    leido, frame = cap.read()

    if leido == True:
        #Convertimos la imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Detectamos las caras en la imagen
        faces = face_detection.detectMultiScale(gray, 1.3, 5)

        #Mostramos cuantas caras hemos encontrado
        print(len(faces))

        #Dibujamos un ectangulo que rodee las caras
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),3)

        #Mostramos las caras por pantalla
        cv2.imshow("Face_Detect", frame)

        #Si tenemos la letra s o 1 paramos el ciclo
        if cv2.waitKey(1) & 0xFF == ord('s'):
	        break
    #else:
	#	print("Error al acceder a la camara.")