import os

labelpath = os.path.abspath('C:\\Users\\mcvk\\Downloads\\dups2\\labels\\')
counter = dict()

for labeltxt in os.listdir(labelpath):
    if labeltxt[-4:] == '.txt' and labeltxt != "classes.txt":
        with open(os.path.join(labelpath, labeltxt)) as fh:
            rowlist = fh.readlines()
    print(rowlist)
    for row in rowlist:
        if row:
            counter[row.split()[0]] = counter.get(row.split()[0], 0)+1

print(counter)
