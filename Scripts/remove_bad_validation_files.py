import os
import pandas as pd

LABEL_PATH = os.path.abspath(
    'C:\\Users\\mcvk\\Downloads\\dataset\\validation_dataset\\labels\\')
IMAGE_PATH = os.path.abspath(
    'C:\\Users\\mcvk\\Downloads\\dataset\\validation_dataset\\images\\')

counter = 0
label_counter = 0
for labeltxt in os.listdir(LABEL_PATH):
    if labeltxt[-4:] == '.txt' and labeltxt != "classes.txt":
        with open(os.path.join(LABEL_PATH, labeltxt)) as fh:
            rowlist = fh.readlines()

    row_list = list()
    for row in rowlist:
        if row:
            row_list.append(row.split()[0])

    if len(row_list) == 1:

        counter += 1

        os.remove(f'{LABEL_PATH}\\{labeltxt}')
        os.remove(f'{IMAGE_PATH}\\{labeltxt[:-4]}.jpg')


print(counter)
