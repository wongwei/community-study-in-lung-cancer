import numpy as np
import re
import pandas as pd


pprofile = pd.read_csv('lung_injury_case copy.csv',sep='\t',usecols=[*range(1,55)],header=None)
mprofile = pd.read_csv('lung_injury_control copy.csv',sep='\t')
allprofile = pd.concat([pprofile,mprofile],ignore_index=True)
print(pprofile.head(1))
# print(mprofile.head(1))
