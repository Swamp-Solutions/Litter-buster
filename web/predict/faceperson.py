
import numpy as np
import cv2
from person_detection import detect_people, draw_boxes
from face_detection import detect_face
import os


def convert_video(video=0):
    video = cv2.VideoCapture(video)
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)

    while (True):
        ret, frame = video.read()
        if ret:
            pboxes = detect_people(frame)
            frame = draw_boxes(frame, pboxes, (0, 255, 0))
            frame = detect_face(frame)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
    if __name__ == '__main__':
        convert_video()