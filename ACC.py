import numpy as np
import pandas as pd

#data = pd.read_table('C:/Users/Sara/Desktop/myTable.txt', sep=',', engine='python')
#data = pd.read_table('C:/Users/Sara/Desktop/few-shot learning data.txt', sep=',', engine='python')
#data = pd.read_table('C:/Users/Sara/Desktop/table_0.85.txt', sep=',', engine='python')
data = pd.read_table('C:/Users/Sara/Downloads/AMEF/fewshotlearningdata6conf0.txt', sep=',', engine='python')
##data = pd.read_table('C:/Users/Sara/Downloads/AMEF/oven_panel_new.txt', sep=',', engine='python')
#data = pd.read_table('C:/Users/Sara/Downloads/AMEF/tableiou0.txt', sep=',', engine='python')
print(data.columns)
print(data['Class'])
TP = data['Labels'] * data['R']
FP = TP/data['P']  - TP
FN = TP / data['R'] - TP
ACC = 1 - (FP + FN)/(TP + FP + FN)

print("TP:", TP)
print("FP:", FP)
print("FN:", FN)
print("ACC:", ACC)
#ACC_FN = pd.concat(FN, ACC)
#ACC_table = pd.concat(pd.concat(TP, FP),ACC_FN)
#print("ACC_table:", ACC_table)


data['TP'] = TP
data['FP'] = FP
data['FN'] = FN
data['ACC'] = ACC
print(data)

#calculate the sum of the table(column)
#ALL_sum = data.sum()
TP_ALL = data['TP'].sum()
FP_ALL = data['FP'].sum()
FN_ALL = data['FN'].sum()

print("TP_ALL:", TP_ALL)
ACC_ALL = 1 - (FP_ALL + FN_ALL)/(TP_ALL + FP_ALL + FN_ALL)
print('ACC_ALL: ', ACC_ALL)
data.to_excel('ACC table.xlsx')


m_ACC = data['ACC'].mean()
print("m_ACC:", m_ACC)