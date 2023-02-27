import cv2
import numpy as np
#Abrimos la camara
cam = cv2.VideoCapture(0)

#Creamos la mascara de color
umbral_bajo = (100,100,100)
umbral_alto = (125,255,255)
#Creamos el kernel que usaremos para la limpieza del ruido de la imagen.
kernel = np.ones((7,7),np.uint8)

while True:
	conf, frame = cam.read()
	if conf == True:
		img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#Con esto limpiamos la imagen de ruido antes de pasarla por los filtros
		opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
		mask = cv2.inRange(opening, umbral_bajo, umbral_alto)
		res = cv2.bitwise_and(img, img ,mask = mask)
		res_rgb = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
		contorno, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		for i in contorno:
			M = cv2.moments(i)
			if M['m00'] != 0:
				cx = int(M['m10']/M['m00'])
				cy = int(M['m01']/M['m00'])
				cv2.drawContours(res_rgb, [i], -1, (0,255,0), 2)
				cv2.circle(res_rgb, (cx,cy), 7, (0,0,255), -1)
				cv2.putText(res_rgb, f"x: {cx} y:{cy}", (cx -20, cy -20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
				cv2.drawContours(res_rgb, contorno, -1, (0,255,0), 3)
		cv2.imshow('res', mask)
		print(f"Momento = {M}")
	if cv2.waitKey(1) & 0xFF == ord('s'):
		break