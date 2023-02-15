import chkres
import os

def find_all_dirs(d = '.'):
    dirdict={}
    for idir in os.listdir(d+'/images'):
        directory = d+'/images/'+idir
        dirdict[idir] = chkres.find_smallest_res(directory)
    for key,value in dirdict.items():
        print(key, ':', len(value))
        
    return dirdict