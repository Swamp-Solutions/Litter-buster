# Script to change the dataset into a 1-label dataset to examine accuracy.
import os
def change_labels(filen="labels.txt"):
    with open(filen, 'r') as f:
        labels = f.readlines()
    newlabels = ['0' + label[1:] for label in labels]
    with open(filen, 'w') as fh:
        fh.writelines(newlabels)

if __name__=='__main__':
    change_labels()
    for filename in os.listdir("./labels"):
        change_labels("./labels/"+filename)
        