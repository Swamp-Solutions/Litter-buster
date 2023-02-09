import numpy as np
import torch
import cv2
from person_detection import detect_people, draw_boxes
import os
from PIL import Image
import matplotlib.pyplot as plt

MODELPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
VIDEOPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Data/video')

model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODELPATH + '/2023-02-09-last.pt', force_reload=True)
video = cv2.VideoCapture(VIDEOPATH + '/littervid.mp4')

# Setting resolutions and a place to write video file.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter(os.path.join(VIDEOPATH,'filename_latest.mp4'),
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
x=0

def transform_frame(frame):
    #pboxes = detect_people(frame)
    res = model(frame)
    #print(" xyxy: ", res.xyxy[0].cpu().numpy())
    frame2=np.squeeze(res.render())
    #frame2 = draw_boxes(frame2,pboxes, (0,255,0))
    return frame2


while(True):
    ret, frame = video.read()
    if ret: 
        frame2 = transform_frame(frame)
        result.write(frame2)
        cv2.imshow('Video', frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    x+=1
video.release()
result.release()
    
cv2.destroyAllWindows()
   
print("The video was successfully saved")

img = Image.open('./bild.png')
result = model(img)
plt.imsave('biild.jpg',np.squeeze(result.render()))