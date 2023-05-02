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
#print(len(data),'strings in file')

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

Massa = 10*savgol_filter(Mass,55,3,deriv=1)

i2 = np.where(Temp>150)
#print(i2[0][0])
a = i2[0][0]
i3 = np.where(Temp>300)
#print(i3[0][0])
b = i3[0][0]
#print (a,b)
Massa1 = Massa[a:b]
Temp1 = Temp[a:b]
ax.plot(Temp1,Massa1)
c = np.amax(Massa1)
print(c)
i4 = np.where(Massa1==c)
print(i4[0][0])

v = i4[0][0]+a
ax.plot(Temp[v],Mass[v],marker = "o",markersize = 5)
d = 5
x = Temp[v-d:v+d]
y = Mass[v-d:v+d]
print (x,y)

p = np.polyfit(x,y,1)
print(p)
f = np.poly1d(p)
t1 = [100,300]
ax.plot(t1,f(t1))
#================Вторая прямая============
h = np.amin(Massa1)
print(h)
i5 = np.where(Massa1==h)
#print(i5[0][0])

k = i5[0][0]+a
ax.plot(Temp[k],Mass[k],marker = "o",markersize = 5)
s = 5
x = Temp[k-s:k+s]
y = Mass[k-s:k+s]
print (x,y)

p1 = np.polyfit(x,y,1)
print(p1)
f1 = np.poly1d(p1)
t2 = [220,300]
ax.plot(t2,f1(t2))

ax.set_xlabel(r'Temperature, $^{0}$C')
ax.set_ylabel('Mass,%')

k1 = p[0]
b1 = p[1]
k2 = p1[0]
b2 = p1[1]

xtr = (b2 - b1)/(k1 - k2)
y = k2*xtr + b2
print(x,y)

ax.plot(xtr,y,'ro')
x = [270,305]
y = [y,y]
textw =  "%.2f" % xtr + ' $^{0}$C'# "%.9f" % numvar
ax.plot(x, y, linestyle='-', linewidth=1, color='black')
ax.text(x[0] + 75, y[0]-3, textw ,
        horizontalalignment='left',
        verticalalignment='bottom',
        color='black',
        rotation='horizontal', fontsize=10)

plt.show()
