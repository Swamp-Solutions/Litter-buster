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
video = cv2.VideoCapture(VIDEOPATH + '/fillname.mp4')

# Setting resolutions and a place to write video file.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter(os.path.join(VIDEOPATH,'filename_test.mp4'),
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
classes = {
  "0": "Glas",
  "1": "Metal",
  "2": "PET",
  "3": "Paper",
  "4": "Plastic",
  "5": "Tobacco"
}
def add_counter(frame, classdict):
    size = (frame2.shape[0],frame2.shape[1])
    for key in classdict.keys():
        print((5*int(key),80+int(key), 50*int(key)), (int(size[0]-(720/(6-int(key)))),int(size[1]-size[1]/6)), f'{classes[key]}: {classdict[key]}')
        cv2.putText(frame2, "Hello", (70,180), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(250,250,0))
        cv2.putText(frame2, f'{classes[key]}: {classdict[key]}', (int(size[0]-(720/(6-int(key)))),int(size[1]-size[1]/6)), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color=(255,0,0))
    
def transform_frame(frame, classdict={}, x=0):
    #pboxes = detect_people(frame)
    res = model(frame)
    #resarray = res.xyxy[0].cpu().numpy()
    
    # if resarray.any() and x%5==0:
    #     for arr in resarray:
    #         classdict[str(int(arr[5]))] = classdict.get(str(int(arr[5])), 0) + 1
            
    frame2=np.squeeze(res.render())
    

    #frame2 = draw_boxes(frame2,pboxes, (0,255,0))
    return frame2, classdict

classdict = {}
x=0
while(True):
    ret, frame = video.read()
    if ret: 
        
        frame2, classdict = transform_frame(frame, classdict,x)
        result.write(frame2)
        cv2.imshow('Video', frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    x+=5
video.release()
result.release()
cv2.destroyAllWindows()
print(classdict)
print("The video was successfully saved")

img = Image.open('./bild.png')
result = model(img)
plt.imsave('biild.jpg',np.squeeze(result.render()))