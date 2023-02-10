import os
import pandas as pd
from collections import defaultdict

labelpath = os.path.abspath(
    'C:\\Users\\mcvk\\Downloads\\dataset\\equilized_dataset\\labels\\')
counter = defaultdict(lambda: 0)

for labeltxt in os.listdir(labelpath):
    if labeltxt[-4:] == '.txt' and labeltxt != "classes.txt":
        with open(os.path.join(labelpath, labeltxt)) as fh:
            rowlist = fh.readlines()

    for row in rowlist:
        if row:
            if row.split()[0] == '0':
                counter['Glas'] += 1
            elif row.split()[0] == '1':
                counter['Metal'] += 1
            elif row.split()[0] == '2':
                counter['PET'] += 1
            elif row.split()[0] == '3':
                counter['Paper'] += 1
            elif row.split()[0] == '4':
                counter['Plastic'] += 1
            elif row.split()[0] == '5':
                counter['Tobacco'] += 1


df = pd.DataFrame(counter.items())
df.rename(columns={0: 'Label', 1: 'Number of labels'}, inplace=True)

print(df)
