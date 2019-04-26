import numpy as np
import pandas as pd
from scipy import stats

expression_value = pd.read_csv('lung_injury_case copy.csv', sep='\t')
expression_value.index += 1
expression_value =  expression_value.drop(columns='Symbol')
expression_value = (expression_value - expression_value.mean()) / \
    (expression_value.max()-expression_value.min())
outcome =stats.pearsonr(expression_value.loc[1],expression_value.loc[2])
# print(outcome)
print(expression_value.head(5))
