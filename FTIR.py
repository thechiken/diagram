import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Datapath=os.getcwd()
FileName ='FTIR-BC (1).dpt'
MF= open(FileName,'r', encoding = 'cp1251')
data = MF. readlines()
MF. close()
print(len(data),'strings in file')

for i in range(5):
    print (data [i])
Wavenumber = np.zeros(len(data)-2)
Absorbance = np.zeros(len(data)-2)

for i in range (len(data)-2):
    data[i+2]=data[i+2].split()
    Wavenumber[i]=float(data[i+2][0])
    Absorbance[i]=float(data[i+2][1])
fig, ax = plt.subplots()


# from scipy.signal import savgol_filter
# Absf = savgol_filter(Absorbance,75,3,deriv=0)
# ax.plot(Wavenumber,Absf,color = 'yellow')
from scipy.signal import savgol_filter
# Absb = savgol_filter(Absf,55,3,deriv=1)
# Absn = savgol_filter(Absf,55,3,deriv=2)
Absb = savgol_filter(Absorbance,55,3,deriv=1)
Absn = savgol_filter(Absorbance,55,3,deriv=2)
#ax.plot(Wavenumber,Absb)
#ax.plot(Wavenumber,Absn*10)
ax.plot(Wavenumber,Absorbance)
maximumW =[]
maximumA =[]

# i = len(Absf)-1
i = len(Absorbance)-1
while Wavenumber[i]<3700:
     if Absorbance[i]>0.05 and Absb[i]>-8e-4 and Absb[i]<8e-4 and Absn[i] < 0:
     # if Absf[i]>0.25 and Absb[i]>-8e-5 and Absb[i]<8e-5 and Absn[i] < 0:
        maximumW.append(Wavenumber[i])
        # maximumA.append(Absf[i])
        maximumA.append(Absorbance[i])
        i = i-30
     else:
        i = i-1
for i in range(len(maximumW)):
    x = [maximumW[i],maximumW[i]]
    y = [maximumA[i]+ 0.2,maximumA[i]-0.2]
    ax.plot(x,y, linestyle='-', linewidth = 0.9, color = 'black')
    textw = "%.0f" % maximumW[i]
    ax.text(x[0],y[0]+0.05,textw,
            horizontalalignment = 'center',
            verticalalignment = 'bottom',
            color = 'red',
            rotation = 'vertical', fontsize = 8)
print(maximumW)
print(maximumA)

ax.set_xlabel(r'Wavenumber, cm$^{-1}$')
ax.set_ylabel('Absorbance')
#fig.savefig("impedance.png")
plt.show()
