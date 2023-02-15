## Work done by Andreas
### 2023-02-06 : 
##### First Model done
Tobacco and Metal - Just as an attempt to get a functioning model.

##### Researching and finding Images.
Finding images for first learning model.

### 2023-02-07 : 
##### E-mail client. 
Takes an image as input, checks against a log if a mail has been sent within a set time(standard 4 hours) and sends a mail with the image attachement if there's been no mail.

Started learning model.

### 2023-02-08 :
##### Create video-conversion-function
Created a python-function that can take as input a video without predictions and return a video with predictions done. 
##### Finished first version of model
Needs a lot of work. Running another attempt with freeze 12 at the end, frozen layers which should help a lot with making an accurate model. \
Also added more background-images. \
Will look to do one full 150 epoch run with frozen layers.

##### Created scripts to evaluate pictures
We have an issue where the pictures are in extremely different resolutions. Some pictures are lower than the learning resolution which may cause problems.

### 2023-02-09
##### Model Version 1 finished running! \
Fixed problems: Much less false positives, almost down to none. I believe this was fixed by adding background images. \
Current problems: We have some mislabeling. This may be due to a few factors: Too many of one class, unversatile labels, lack of background-data. \
##### Video-handling-function just about finished.
We have an issue where using the cv2 haar cascades is causing a loss of performance on predictions, making the videos laggy. \
They also give inaccurate boxes. \
This may be fixed by installing GPU-supporting software for openCV. \
Still need to add email function and get an announcement of the litterer by euclidian distance.

### 2023-02-10
##### Put a stop to Model-optimization \
We got a pretty good dataset and finished building a model with it.
##### 
