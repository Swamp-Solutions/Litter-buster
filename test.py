import cv2
import numpy as np

def detect_faces(frame, faceCascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(30, 30),
    )
    return faces

def detect_people(frame, hog):
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    return boxes

def draw_boxes(frame, boxes, color=(0, 255, 0)):
    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB), color, 2)
    return frame

cascPath = "haar_face.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

while True:
    ret, frame = video_capture.read()
    frame = cv2.resize(frame, (640, 480))

    faces = detect_faces(frame, faceCascade)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    people = detect_people(frame, hog)
    frame = draw_boxes(frame, people)

    out.write(frame.astype('uint8'))
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()
