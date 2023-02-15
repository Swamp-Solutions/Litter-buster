import PIL
from PIL import Image
import os


def find_smallest_res(fpath='.'):
    widlst = []
    hgtlst=[]
    filelist=[]
    for x in os.listdir(fpath):
        if x == 'chkres.py':continue
        img = PIL.Image.open(fpath+'/'+x)
        wid, hgt = img.size
        
        if wid < 640 or  hgt < 640:
            print(wid, 'x', hgt)
            widlst.append(wid)
            hgtlst.append(hgt)
            filelist.append(x)
    
    print(min(hgtlst), 'x', min(widlst))
    print(filelist[widlst.index(min(widlst))])
    print("lengths: ", len(widlst))
    return filelist

find_smallest_res()
