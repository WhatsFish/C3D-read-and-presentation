# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:48:37 2020

@author: User
"""
from ezc3d import c3d
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D


path = './datasets/13_29.c3d'
c = c3d(path)
point_data = c['data']['points']

fig = plt.figure()
ax = fig.gca(projection='3d')
#my_y_ticks = np.arange(0, 1000, 200)
#my_z_ticks = np.arange(0, 2000, 200)
#ax.set_yticks(my_y_ticks)
#ax.set_zticks(my_z_ticks)
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.3, 0.3, 1, 1]))

used_label = {"RFHD":0, "LFHD":0, "CLAV":0, "STRN":0, "LSHO":0, "RSHO":0, "RFWT":0, "LFWT":0, "RKNE":0, "LKNE":0, \
             "RANK":0, "LANK":0, "RELB":0, "LELB":0, "RFIN":0, "LFIN":0, "RTOE":0, "LTOE":0 }
label_keys = used_label.keys()
labels = c['parameters']['POINT']['LABELS']['value']
for label in label_keys:
    index = [i for i,x in enumerate(labels) if x.find(label)!=-1]
    used_label[label] = index[0]

stick_difines_f_head=[
    (used_label['CLAV'], used_label['STRN']),
    (used_label['RFHD'], used_label['CLAV']),
    (used_label['CLAV'], used_label['LFHD']),
    (used_label['CLAV'], used_label['LSHO']),
    (used_label['CLAV'], used_label['RSHO']),
    (used_label['STRN'], used_label['RFWT']),
    (used_label['STRN'], used_label['LFWT']),
    (used_label['RFWT'], used_label['RKNE']),
    (used_label['LFWT'], used_label['LKNE']),
    (used_label['RKNE'], used_label['RANK']),
    (used_label['LKNE'], used_label['LANK']),
    (used_label['RSHO'], used_label['RELB']),
    (used_label['LSHO'], used_label['LELB']),
    (used_label['RELB'], used_label['RFIN']),
    (used_label['LELB'], used_label['LFIN']),
    (used_label['RANK'], used_label['RTOE']),
    (used_label['LANK'], used_label['LTOE'])
]


for _ in range(400):
    _ = _ + 4100
    print(_)
    frame = point_data[:, :, _]
    x = frame[0, :]
    y = frame[1, :]
    z = frame[2, :]
    #ax.scatter(x, y, z)
    
    for k, v in used_label.items():
        xi = frame[0, :][v]
        yi = frame[1, :][v]
        zi = frame[2, :][v]
        ax.scatter(xi, yi, zi, c = "b")
        
        if _ > 4230 and _ < 4470 and k == "RELB":
            ax.scatter(xi, yi, zi, c = "r")
        if _>4400 and k == "RKNE":
            ax.scatter(xi, yi, zi, c = "r")
    
    for i in stick_difines_f_head:
        xx = [x[i[0]], x[i[1]]]
        yy = [y[i[0]], y[i[1]]]
        zz = [z[i[0]], z[i[1]]]
        ax.plot(xx, yy, zz, c = 'g')
        
        if _ > 4230 and _ < 4470 and (i[0] == 18 or i[1] == 18):
            ax.plot(xx, yy, zz, c = 'r')
        if _>4400 and (i[0] == 35 or i[1] == 35):
            ax.plot(xx, yy, zz, c = 'r')
    
    plt.show()
    
    plt.pause(0.001)
    ax.cla()
