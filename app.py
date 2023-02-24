import cv2
import matplotlib.pyplot as plt

#Abrimos la camara
cam = cv2.VideoCapture(0)

#Guardamos el frame en una variable y si a leido bien o no en otra
conf, frame = cam.read()


#Cerramos la webcam
cam.release()