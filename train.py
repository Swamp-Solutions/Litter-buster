!git clone https://github.com/ultralytics/yolov5
!pip install -r yolov5/requirements.txt

import torch,cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

model = torch.hub.load('ultralytics/yolov5', 'yolov5l')

# !python ./yolov5/train.py --img 640 --batch 32 --epochs 300 --data dataset.yaml --weights yolov5s.pt