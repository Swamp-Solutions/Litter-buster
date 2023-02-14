import numpy as np
import torch
import cv2
# from person_detection import detect_people, draw_boxes
import os
from PIL import Image
import matplotlib.pyplot as plt

MODELPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
VIDEOPATH = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), 'Data/video')

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path=MODELPATH + '/2023-02-09-last.pt', force_reload=True)

classes = {
    0: "Glas",
    1: "Metal",
    2: "PET",
    3: "Paper",
    4: "Plastic",
    5: "Tobacco"
}


def get_midpoint(xyxy):

    midpoint = ()
    return midpoint


def transform_frame(frame, model=model, video=False):
    res = model(frame)
    frame2 = np.squeeze(res.render())
    if not video:
        classdict = {}
        #pboxes = detect_people(frame)
        resarray = res.xyxy[0].cpu().numpy()
        size = frame2.shape[:2]
        for arr in resarray:
            classdict[arr[5]] = classdict.get(arr[5], 0)+1
        x = 0
        for key in classdict.keys():
            key = int(key)
            itext = f'{classes[key]}: {classdict[key]}'
            pos = (int(size[0]-(720/(6-int(key)))), int(size[1]-size[1]/6))
            cv2.putText(frame2, itext, (40, 80+x),
                        cv2.FONT_HERSHEY_TRIPLEX, 3, (250, 250, 0), 4)
            x += 80
        #frame2 = draw_boxes(frame2,pboxes, (0,255,0))
    elif video:
        classdict = {}
        resarray = res.xyxy[0].cpu().numpy()
        size = frame2.shape[:2]
        for arr in resarray:
            classdict[arr[5]] = classdict.get(arr[5], 0)+1
        x = 0
        for key in classdict.keys():
            key = int(key)
            itext = f'{classes[key]}: {classdict[key]}'
            cv2.putText(frame2, itext, (40, 50+x),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (180, 150, 40), 4)
            x += 40
    return frame2


def convert_video(video="/fillname.mp4"):
    video = cv2.VideoCapture(VIDEOPATH + video)

    # Setting resolutions and a place to write video file.
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter(os.path.join(VIDEOPATH, 'filename_test.mp4'),
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             10, size)
    while(True):
        ret, frame = video.read()
        if ret:

            frame2 = transform_frame(frame, model, video=True)
            result.write(frame2)
            cv2.imshow('Video', frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    video.release()
    result.release()
    cv2.destroyAllWindows()
    print("The video was successfully saved")


if __name__ == '__main__':
    # img = Image.open('./saofas.jpg')
    # arr = np.array(img)
    # transformed_image = transform_frame(arr,model)
    # plt.imsave('biild.jpg', transformed_image)
    # plt.imshow(transformed_image)
    # print("Image saved")
    convert_video()
