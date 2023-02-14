import cv2 as cv
import numpy as np
from person_detection import 

models = "../models"
faceCascade = cv.CascadeClassifier(models+'/faces.xml')

def detect_face(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
    )
    return faces

def detect_culprit(frame):
    