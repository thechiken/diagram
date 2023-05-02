import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import gridspec
import os

Datapath = os.getcwd()
FileName ='лит порф.txt'
MF= open(FileName,'r', encoding = 'cp1251')
data = MF. readlines()
MF. close()
#print(len(data),'strings in file')

data2 = []

for i in range (len(data)):
    data[i] = data[i].split('.,')[:-1]
    #data2.append(data[i][0])
    # data2[i] = data2[i].split(', ')
#print(data)
avth = []
n = 0
for i in range (len(data)):
         for g in range(len(data[i])):
             a = False
             n = n+1
             for k in range(len(avth)):
                 if avth[k] == data[i][g]:
                     a = True
             if not (a):
                 avth.append(data[i][g])

v = np.zeros(len(avth))

print(len(avth),n)
print(avth)