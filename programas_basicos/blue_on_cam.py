import cv2
#Abrimos la camara
cam = cv2.VideoCapture(0)

#Creamos la mascara de color
umbral_bajo = (100,100,100)
umbral_alto = (125,255,255)
while True:
	conf, frame = cam.read()
	if conf == True:
		img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(img, umbral_bajo, umbral_alto)
		res = cv2.bitwise_and(img, img ,mask = mask)
		res_rgb = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
		contorno, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		#Mostramos las imagenes por pantalla
		cv2.drawContours(res_rgb, contorno, -1, (0,255,0), 3)
		cv2.imshow('res', res_rgb)
		if cv2.waitKey(1) & 0xFF == ord('s'):
			break
	else:
		print("Error al acceder a la camara.")