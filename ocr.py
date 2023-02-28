import cv2
import easyocr

#Establecemos los idiomas que usaremos para el easyocr
reader = easyocr.Reader(["es"], gpu=False)

#Importamos una foto
img = cv2.imread("npfoto/lectura.jpeg")

#Extraemos el texto de la imagen
result = reader.readtext(img, paragraph=False)
print(result)