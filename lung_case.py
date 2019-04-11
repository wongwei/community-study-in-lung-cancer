import numpy as np
import re
import pandas as pd
import networkx as nx

mprofile = []

with open('lung_injury_case copy.txt') as f:
    next(f)
    while True:
        line = f.readline()
        x = line.split()
        x = x[1:len(x)-1]
        line = list(map(float,x))
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
print("pprofile:",len(pprofile))
print("mprofile:",len(mprofile))