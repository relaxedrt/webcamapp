import cv2
import logging as log

#Iniciamos el modo de logging
log.basicConfig(level = 10)

#ELEGIMOS EL UMBRAL DEL ROJO VERDE EN HSV
umbral_bajo1 = (170,100,100)
umbral_alto1 = (179,255,255)

umbral_bajo2 = (0,100,100)
umbral_alto2 = (10,255,255)

conf = True
frame = cv2.imread('pruebas/sample/12v.jpg')

#Gestionamos el resultado
if conf == True:
    #log.debug(msg="Foto tomada correctamente")
    #Pasamos un filtro hsv 
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Creamos una mascara y filtramos la imagen original
    mask1 = cv2.inRange(img, umbral_bajo1, umbral_alto1)
    mask2 = cv2.inRange(img, umbral_bajo2, umbral_alto2)
    mask = mask1 + mask2
    #Colocamos la mascara sobre el filtro
    res = cv2.bitwise_and(img, img ,mask = mask)
    #Devolvemos el resultado a BGR
    res_rgb = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    #Detectamos los contornos que nos ha dejado la mascara
    contornos, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #Si encontramos algún contorno seguimos, sino mostramos un error
    if len(contornos) != 0:
        #Para cada contorno encontrado realizamos las operaciones
        for contorno in contornos:
            #Calculamos el perimetro del contorno
            epsilon = 0.01*cv2.arcLength(contorno, True)
            #Calculamos los vertices que tenemos
            vertices = cv2.approxPolyDP(contorno, epsilon, True)
            x,y,w,h = cv2.boundingRect(vertices)
            #Si tiene 4 vértices realizamos la localización del centro
            if len(vertices) == 12:
                #Calculamos el momento del contorno
                M = cv2.moments(contorno)
                #Si el momento es distinto a 0
                if M['m00'] != 0:
                    #Calculamos la x y la y central
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    #Dibujamos el contorno 
                    cv2.drawContours(res_rgb, [contorno], -1, (0,255,0), 2)
                    #Escribimos la figura que es
                    cv2.putText(res_rgb, f"Figura x:{cx} y:{cy}", (x,y-5),1,1.5,(0,255,0),2)
                    #Creamos un circulo indicando el centro
                    cv2.circle(res_rgb, (cx,cy), 7, (0,0,255), -1)
                    #Guardamos la foto
                    cv2.imwrite(f"pruebas/processed/prueba.png", res_rgb)
                    #Escribimos por consola la posición de la figura
                    log.debug(msg=f"Figura de 12 vertices encontrada en posición: {cx},{cy}")
            else:
                #Representamos el error de que no se ha encontrado un cuadrado
                log.error(msg="No se han detectado 12 vertices.")
    else:
        #Representamos el error de que no se ha encontrado el color rojo
        log.error(msg="No se ha detectado el color rojo.")