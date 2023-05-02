import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import gridspec
width_mm = 60
height_mm = 100
top_margin_mm = 5
left_margin_mm = 10
bottom_margin_mm =15
right_margin_mm = 5

h_space_mm = 35
w_space_mm = 50

xinch = width_mm*0.0394
yinch = height_mm*0.0394

space_w = w_space_mm/width_mm
space_h = h_space_mm/height_mm

m_left = left_margin_mm/width_mm
m_right = (width_mm-right_margin_mm)/width_mm
m_bottom = bottom_margin_mm/height_mm
m_top = (height_mm-top_margin_mm)/height_mm

fig = plt.figure(figsize=(xinch, yinch))
gs = gridspec.GridSpec(1, 1, height_ratios=[1, 1], width_ratios=[1])
gs.update(wspace=space_w, hspace=space_h)
plt.subplots_adjust(left=m_left, right=m_right, top=m_top, bottom=m_bottom)

ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
file = 'AFM-map.txt'

MF = open(file,"r", encoding='utf-8')
data = MF.readlines()
MF.close()

for i in range(len(data)-4):
    data[i+4] = " ".join(data[i+4] .split())
    data[i+4] = data[i+4].split()
AFMmap = np.zeros((len(data)-4,len(data[5])))
for i in range(len(data)-4):
    for j in range(len(data[i+4])):
        AFMmap[i][j] = 1e9*float(data[i+4][j])

print('Max height (nm) = ', AFMmap.max())
print('Min height (nm) = ', AFMmap.min())
afm = ax1.imshow(AFMmap, cmap = plt.cm.afmhot, vmin = 30, vmax = 60)
ax1.set_xticks([])
ax1.set_yticks([])
cbar = plt.colorbar( ax = ax1, shrink = 0.85)

ax1.text(1.15, 1.05, 'nm',
         horizontalalignment = "left",
         color = 'black',
         verticalalignment = "top", fontsize = 12,
         transform = ax1.transAxes)

m = 300/len(AFMmap[0])
print('Scale = ', m, 'nm/pixel')
bar = 100
barl = bar/m
X1 = 0.05*len(AFMmap[0])
Y1 = 0.87*len(AFMmap)
XX = [X1,X1+barl]
YY = [Y1,Y1]

Yt1 = Y1 + 0.02*len(AFMmap)
Xt1 = X1 + int(barl/2)
ax1.plot(XX, YY, color = 'white', linewidth = 1.8)
ax1.text(Xt1, Yt1, r'0.1 $\mu$m', horizontalalignment = "center", color = "white", verticalalignment = 'top')

from PIL import Image
picture = Image.open("3_13.jpg")
arr_picture = np.array(picture)

ax2. imshow(arr_picture,cmap=plt.cm.gray)
#ax2.set_xticks([])
#ax2.set_yticks([])
Xb1 = 0
Xb2 = 0
k = 400
print(arr_picture)
while k<600:
    if (arr_picture[850][k][0]>200) and (Xb1>0) and (Xb2==0):
       Xb2=k
       print("stop point =",k)
        break
    if (arr_picture[850][k][0]>200) and (Xb1==0):
       Xb1=k
       print('Start point = ',k)
        k=k+4
    k = k+1
mashtab=20000/(Xb2-Xb1)
bar = 100000
print('Maschtab = ',mashtab, 'nm/pixel')
arr_picture_crop = arr_picture[:847]
ax2.imshow(arr_picture_crop,cmap=plt.cm.gray)
XX = [50,50+(bar/mashtab)]
YY = [650,650]
ax2.plot(XX,YY,color= 'white', linewidth = 2)
xbt = 0.5*(XX[0]+XX[1])
ybt = YY[0]-20
ax2.text(xbt,ybt,r'100$\mu$m',horizontalalignment="center",
         verticalalignment="bottom",fontsize = 12,
         color = "white")
ax2.set_xticks([])
ax2.set_yticks([])

plt.show()


