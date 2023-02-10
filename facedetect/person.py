import numpy as np
import cv2

cv2.startWindowThread()
cap = cv2.VideoCapture(0)

while(True):
    # read frame
    ret, frame = cap.read()
    # display frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # breakingloop if the user types q

        break

cap.release()
cv2.destroyAllWindows()

cv2.waitKey(1)

# turn to greyscale:
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
# apply threshold. all pixels with a level larger than 80 are shown in white. the others are shown in black:
ret,frame = cv2.threshold(frame,80,255,cv2.THRESH_BINARY)