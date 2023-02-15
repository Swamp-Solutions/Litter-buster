import os
labelpath = os.path.abspath('./labels')
counter = dict()
for labeltxt in os.listdir(labelpath):
    print(labeltxt[-4:])
    if labeltxt[-4:] == '.txt' and labeltxt != "classes.txt":
        with open(os.path.join(labelpath,labeltxt)) as fh:
            rowlist = fh.readlines()
    print(rowlist)
    for row in rowlist:
        if row:
            print(row)
            counter[row.split()[0]] = counter.get(row.split()[0],0)+1
print(counter)