import cv2 as cv
import numpy as np

from person_detection import detect_people

MODELPATH = "../models"
VIDEOPATH = "../Data/video"

faceCascade = cv.CascadeClassifier(MODELPATH+'/haar_face.xml')

def detect_culprit(frame, trash_prediction):

    peoples = detect_people(frame)
    print(trash_prediction)