import numpy as np
import torch
import cv2
  
model = torch.hub.load('ultralytics/yolov5', 'custom', path='last.pt', force_reload=True)
video = cv2.VideoCapture('fillname.mp4')
   
# Setting resolutions and a place to write video file.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename_latest.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
while(True):
    ret, frame = video.read()
    if ret: 
        frame=np.squeeze(model(frame).render())
        result.write(frame)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break
  
video.release()
result.release()
    
cv2.destroyAllWindows()
   
print("The video was successfully saved")