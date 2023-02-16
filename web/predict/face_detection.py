import cv2 as cv
import numpy as np
import os
from person_detection import detect_people, draw_boxes

models = os.path.join(os.path.dirname(os.path.dirname(__file__)),'models')
faceCascade = cv.CascadeClassifier(os.path.join(models,'faces.xml'))


def detect_face(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
    )
    return faces
