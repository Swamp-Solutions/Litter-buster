import cv2 as cv
import sys


cascade_path = "haar_front.xml"

def detect_faces(image_path,cascade_path = "haar_front.xml"):
    face_cascade = cv.CascadeClassifier(cascade_path)
    image = cv.imread(image_path)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return faces, image

def show_faces(faces, image):
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("Faces found", image)
    cv.waitKey(0)

if __name__ == "__main__":
    image_path = sys.argv[1]
    faces, image = detect_faces(image_path)
    print("Found {0} faces!".format(len(faces)))
    show_faces(faces, image)
