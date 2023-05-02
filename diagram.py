import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import gridspec
import os
fig = plt.figure()
ax = fig.add_subplot(111)

Datapath = os.getcwd()
FileName ='TGA-data.csv'
MF= open(FileName,'r', encoding = 'cp1251')
data = MF. readlines()
MF. close()
print(len(data),'strings in file')

#for i in range(5):
    #print (data [i])
Temp = np.zeros(len(data)-1)
Mass = np.zeros(len(data)-1)

for i in range (len(data)-1):
    data[i+1]=data[i+1].split(';')
    Temp[i]=float(data[i+1][0])
    Mass[i]=float(data[i+1][2])
#fig, ax = plt.subplots()
ax.plot(Temp,Mass)
ax.set_xlabel('Temperature')
ax.set_ylabel('Mass')
#plt.show()

from scipy.signal import savgol_filter

Massa = savgol_filter(Mass,55,3,deriv=1)
Massb = savgol_filter(Mass,55,3,deriv=2)
ax.plot(Temp,Massa*10)

maximumT =[]
maximumM =[]

i = len(Temp)-1
while Temp[i]<597:
     if Massa[i]<1 and Massa[i]>8e-3 and Massa[i]<-8e-3 and Massb[i] < 0:
        maximumT.append(Temperature[i])
        maximumM.append(Mass[i])
        i = i-30
     else:
        i = i-1
for i in range(len(maximumT)):
    x = [maximumT[i]+0.2,maximumT[i]-0.2]
    y = [maximumM[i],maximumM[i]]
    ax.plot(x,y, linestyle='-', linewidth = 0.9, color = 'black')
    textT = "%.0f" % maximumT[i]
    ax.text(x[0]+0.05,y[0],textT,
            horizontalalignment = 'center',
            verticalalignment = 'bottom',
            color = 'red',
            rotation = 'horizontal', fontsize = 8)
print(maximumT)
print(maximumM)

ax.set_xlabel(r'Temperature, $^{0}$C')
ax.set_ylabel('Mass,%')

#x = np.arange(20,100,2)
#y = p0*x + p1
#p = np.polyfit(Temp,Mass,1)
#ax.plot(x,y,'bo',label = 'Data')

#fig.savefig("impedance.png")
plt.show()
