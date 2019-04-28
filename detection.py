import pickle
import matplotlib
matplotlib.use("TkAgg")

with open('differential_num.pickle','rb') as file:
    differential_num = pickle.load(file)

with open('PccValue_group.pickle','rb') as file:
    PccValue_group = pickle.load(file)
print(PccValue_group)