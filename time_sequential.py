import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import pickle


with open('network_edges_group.pickle', 'rb') as file:
    network_edges_group = pickle.load(file)

expression_value = pd.read_csv('lung_injury_case copy.csv', sep='\t')
expression_value.index += 1
expression_value = expression_value.drop(columns='Symbol')
expression_value = (expression_value - expression_value.mean()) / \
    (expression_value.max()-expression_value.min())
# divide the expression_value by time(6) into 9 chunks
timeSequence = []
timeSequence = np.split(expression_value, 9, axis=1)
# print("The PCC:{0}".format(outcome))
PccValue = []

differential_num = {}
threshold = 0.9
PccValue_group = {}
for j,k in enumerate(network_edges_group):
    differential_val_group = {}
    PccValue_subGroup = {}
    for index,edges in enumerate(network_edges_group[j]):
        i = 0
        differential_val = 0
        PccValue = []
        differential_val_subgroup = []
        for df in timeSequence:
            result = stats.pearsonr(df.loc[edges[0]], df.loc[edges[1]])
            PccValue.append(result[0])
        PccValue_subGroup[index] = PccValue
        # while i < len(PccValue)-1:            
        #     if((PccValue[i]-threshold)*(PccValue[i+1]-threshold) < 0):
        #         differential_val += 1
        #         # print(differential_val)
        #     differential_val_subgroup.append(differential_val)
        #     i += 1
        # differential_val_group[index] = differential_val_subgroup
#     # print(differential_val)    
    # differential_num[j] = differential_val_group
    PccValue_group[j] = PccValue_subGroup
    # print(PccValue_group)
#     # print('The Pcc for edges{0} is {1}'.format(edges, PccValue))
# file = open('differential_num.pickle', 'wb')
# pickle.dump(differential_num, file)
# file.close()
file = open('PccValue_group.pickle', 'wb')
pickle.dump(PccValue_group, file)
file.close()
