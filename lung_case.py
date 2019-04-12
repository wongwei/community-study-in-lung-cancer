import numpy as np
import pandas as pd
import networkx as nx
from scipy import stats

mprofile = []
with open('lung_injury_case copy.txt') as f:
    next(f)
    while True:
        line = f.readline()
        x = line.split()
        x = x[1:len(x)-1]
        line = list(map(float, x))
        mprofile.append(line)
        if not line:
            break

pprofile = []
with open('lung_injury_control copy.txt') as f:
    next(f)
    while True:
        line = f.readline()
        x = line.split()
        x = x[1:len(x)-1]
        line = list(map(float, x))
        pprofile.append(line)
        if not line:
            break
pprofile.pop(-1)
mprofile.pop(-1)
allprofile1 = []
allprofile = pprofile + mprofile
for bigItem in allprofile:
    for item in bigItem:
        allprofile1.append(item)
allprofile = np.array(allprofile1)
allprofile = stats.zscore(allprofile)
print(allprofile)
# print("pprofile:",len(pprofile))
# print("mprofile:",len(mprofile))
