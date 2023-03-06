#Importamos la libreria open-cv
import cv2

#Accedemos a la foto que vamos a usar
img_rgb = cv2.imread("npfoto/figurascolores.png")
#La convertimos a escala de grises
img_eg = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#Usamos canny para detectar los bordes
canny = cv2.Canny(img_eg, 10, 150)

#Usamos dilatacion y erosión para limpiar la imagen
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#_, th = cv2.threshold(img_eg, 10, 255, cv2.THRESH_BINARY)

#Encontramos los contornos de la imagen binaria
contorno, hierachy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for c in contorno:
    epsilon = 0.01*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    #print(len(approx))
    x, y, w, h = cv2.boundingRect(approx)

    #Detectar el triangulo
    if len(approx) == 3:
        cv2.putText(img_rgb, "Triangulo", (x, y -5), 1, 1.5, (0,255,0), 2)
    
    #Detectar cuadrado y rectangulo
    if len(approx) == 4:
        #Checkeamos el aspect ratio mediante dividir un lado entre otro
        aspect_ratio = float(w)/h
        print("aspect_ratio", aspect_ratio)
        #Si el aspect ratio es uno es un cuadrado porque los dos lados son iguales, sino sera un rectangulo
        if aspect_ratio == 1:
            cv2.putText(img_rgb, "Cuadrado", (x, y -5), 1, 1.5, (0,255,0), 2)
        else:
            cv2.putText(img_rgb, "Rectangulo", (x, y -5), 1, 1.5, (0,255,0), 2)
    
    #Detectar el pentagono
    if len(approx) == 5:
        cv2.putText(img_rgb, "Pentagono", (x, y -5), 1, 1.5, (0,255,0), 2)

    #Detectar el hexagono
    if len(approx) == 6:
        cv2.putText(img_rgb, "Hexagono", (x, y -5), 1, 1.5, (0,255,0), 2)

    #Detectar el circulo
    if len(approx) > 10:
        cv2.putText(img_rgb, "Circulo", (x, y -5), 1, 1.5, (0,255,0), 2)
    
    cv2.drawContours(img_rgb, [approx], 0, (0, 255, 0), 2)
#Dibujamos los contronos y lo mostramos por pantalla
cv2.imshow("Resultado", img_rgb)
cv2.waitKey(0)    
