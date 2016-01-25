#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
import math
from mpl_toolkits.mplot3d import Axes3D

infile = open('datas.txt', 'r')
errorVisualT = list()
errorVisualR = list()
for line in infile:
    line = line.split("   ")
    errorVisualT.append(float(line[1].split(":")[1]))
    errorVisualR.append(float(line[2].split(":")[1]))
infile.close()

# mean
errorVisualT = np.array(errorVisualT)
errorVisualR = np.array(errorVisualR)


for error in [errorVisualT,errorVisualR]:
    print "Media: "+str(np.average(error))+", Desviación típica: "+str(np.std(error))+", Máximo: "+str(np.amax(error))+", Mínimo: "+str(np.amin(error))

plt.xlim((0,52))
plt.ylim((0,100))
plt.plot(errorVisualT)
plt.xlabel(r"N\'umero del experimento")
plt.ylabel(r"Error $e$ traslaci\'on en cm")
plt.title(r"Gr\'afica de Traslaci\'on")
plt.plot(errorVisualT, label='Error producido')
Median = [np.average(errorVisualT)] * len(errorVisualT)
plt.plot(Median, label='Media Error')
plt.legend()
#plt.show()

plt.xlim((0,52))
plt.ylim((0,math.pi/float(2)))
plt.plot(errorVisualR)
plt.xlabel(r"N\'umero del experimento")
plt.ylabel(r"Error $e$ rotaci\'on en cm")
plt.title(r"Gr\'afica de Rotaci\'on")
plt.plot(errorVisualT, label='Error producido')
Median = [np.average(errorVisualR)] * len(errorVisualR)
plt.plot(Median, label='Media Error')
plt.legend()
#plt.show()




infile = open('datas.txt', 'r')
points = list()
for line in infile:
    line = line.split("(")
    line = line[1].split(")")[0].split(", ")
    points.append(line)
infile.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
xs = list()
ys = list()
zs = list()
for p in points:
    xs.append(float(p[0]))
    ys.append(float(p[1]))
    zs.append(float(p[2]))
    
ax.scatter(xs,zs, ys, c='b', marker='o')
plt.title(r"Posici\'on Objectivo")
ax.set_xlabel(r'posici\'on X (mil\'imetros)')
ax.set_ylabel(r'posici\'on Z (mil\'imetros)')
ax.set_zlabel(r'posici\'on Y (mil\'imetros)')

plt.show()













