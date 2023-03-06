import cv2
import easyocr

#Establecemos los idiomas que usaremos para el easyocr
reader = easyocr.Reader(["es"], gpu=True)

#Importamos una foto
img = cv2.imread("npfoto/lectura.jpeg")

#Extraemos el texto de la imagen
result = reader.readtext(img, paragraph=True)
for res in result:
    print("res:", res)
    pt0 = res[0][0]
    pt1 = res[0][1]
    pt2 = res[0][2]
    pt3 = res[0][3]
    cv2.rectangle(img, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
    cv2.putText(img, res[1], (pt0[0], pt0[1] - 3), 2, 0.88, (255, 255, 255), 1)
    
    cv2.rectangle(img, pt0, pt2, (166, 56, 242), 2)
    cv2.circle(img, pt0, 2, (255, 0, 0), 2)
    cv2.circle(img, pt1, 2, (0, 255, 0), 2)
    cv2.circle(img, pt2, 2, (0, 0, 255), 2)
    cv2.circle(img, pt3, 2, (0, 255, 255), 2)

    cv2.imshow("Imagen", img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
