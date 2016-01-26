#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
import math
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
from scipy.interpolate import interp1d


filename = 'timedata.txt'

infile = open(filename, 'r')
cont = 0
alltimeStamp = list()
allerrorVisual = list()
for line in infile:
    if "target" not in line:
        line = (line.replace(' ','')).split(",")
        time = line[0].split(":")
        errorT = line[1].split(":")
        errorR = line[2].split(":")
        timeStamp.append(float(time[1]))
        errorVisual.append(float(errorT[1])/float(1000)+float(errorR[1])*2)
    else:
        if cont > 0:
            alltimeStamp.append(timeStamp)
            allerrorVisual.append(errorVisual)
        else:
            cont += 1
        timeStamp = list()
        errorVisual = list()
    #errorVisualT.append(float(line[1].split(":")[1]))
    #errorVisualR.append(float(line[2].split(":")[1]))
infile.close()



print timeStamp[0]
print len(alltimeStamp)
allOrderErrorVisual = list()
allOrdertimeStamp = list()
for i in range(len(allerrorVisual)):
    allOrderErrorVisual += allerrorVisual[i]
    allOrdertimeStamp += alltimeStamp[i]

#inds = allOrdertimeStamp.argsort()
#allOrderErrorVisual = allOrderErrorVisual[inds]

allOrdertimeStamp, allOrderErrorVisual = zip(*sorted(zip(allOrdertimeStamp,allOrderErrorVisual)))


#new_x = np.linspace(min(allOrdertimeStamp), max(allOrdertimeStamp), len(allOrdertimeStamp))
#new_y = sp.interpolate.interp1d(allOrdertimeStamp, allOrderErrorVisual, kind='cubic')(new_x)


# mediante dos vectores x e y que almacenan, respectivamente, las coordenadas x e y de dichos datos, puede realizarse un ajuste polinómico
# de grado n (n=1 para una recta, ...) de los mismos sin más que invocar la función polyfit de la siguiente manera:
# El full solo para que devuelva todo lo demás que no es fp1, fp1 son los parámetros de la función modelo ajustado
fp, residuals, rank, sv, rcond = sp.polyfit(allOrdertimeStamp, allOrderErrorVisual, 1, full=True)
# contruimos la funcion
f = sp.poly1d(fp)
fx = sp.linspace(0,300, 1)

plt.plot(fx, f(fx), linewidth=4)

#f = interp1d(allOrdertimeStamp, allOrderErrorVisual)
##f2 = interp1d(allOrdertimeStamp, allOrderErrorVisual, kind='cubic')
#plt.plot(allOrdertimeStamp,allOrderErrorVisual , 'o', allOrdertimeStamp, f(allOrdertimeStamp))#, '-', allOrdertimeStamp, f2(allOrdertimeStamp), '--')
#plt.legend(['experimento', 'regresion'], loc='best')#, 'cubic'], loc='best')
#plt.xlabel("Experimento")
#plt.ylabel("Error (milimetros)")
#plt.show()


#x = np.linspace(1, 72, num=71, endpoint=True)

allOrderErrorVisual = allOrderErrorVisual / np.max(allOrderErrorVisual)
#f = interp1d(allOrdertimeStamp, allOrderErrorVisual)
#plt.plot(allOrdertimeStamp,allOrderErrorVisual , 'o', allOrdertimeStamp, f(allOrdertimeStamp), x, f(x))#, '-', allOrdertimeStamp, f2(allOrdertimeStamp), '--')
#plt.plot(x, f(x))#, '-', allOrdertimeStamp, f2(allOrdertimeStamp), '--')
plt.legend(['experimento', 'regresion','otro'], loc='best')#, 'cubic'], loc='best')
plt.xlabel("Experimento")
plt.ylabel("Error (milimetros)")
plt.show()




timeStamp = np.array(allOrdertimeStamp)
errorVisual = np.array(allOrderErrorVisual)
maxallOrderErrorVisual = np.amax(allOrderErrorVisual)
print "---------->", maxallOrderErrorVisual
newlist = list()
for i in range(len(allOrderErrorVisual)): 
    newlist.append(allOrderErrorVisual[i] / float(maxallOrderErrorVisual))
plt.plot(allOrdertimeStamp,newlist, label='Error')
plt.plot(new_x,new_y, label='Interpolate')
plt.xlabel("Tiempo (segundos)")
plt.ylabel("error (metros)")
#plt.ylim((0,1))
plt.title(r"Gr\'afica de error VS tiempo")
Median = [np.average(newlist)] * len(newlist)
plt.plot(allOrdertimeStamp,Median, label='Media Error')
plt.legend()
plt.show()



for i in range(len(alltimeStamp)):
    timeStamp = alltimeStamp[i]
    errorVisual = allerrorVisual[i]
    #print errorVisual
    timeStamp = np.array(timeStamp)
    errorVisual = np.array(errorVisual)
    maxerrorVisual = np.amax(errorVisual)
    for i in range(len(errorVisual)):
        errorVisual[i] = errorVisual[i] / float(maxerrorVisual)
    #print errorVisual
    #plt.xlim((0,52))
    plt.ylim((0,1))
    plt.plot(timeStamp,errorVisual)
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("error (metros)")
    plt.title(r"Gr\'afica de error VS tiempo")
    #plt.plot(errorVisual, label='Error producido')
    Median = [np.average(errorVisual)] * len(errorVisual)
    plt.plot(timeStamp,Median, label='Media Error')
    plt.legend()
    plt.show()





    #for error in [errorVisualT,errorVisualR]:
        #print "Media: "+str(np.average(error))+", Desviación típica: "+str(np.std(error))+", Máximo: "+str(np.amax(error))+", Mínimo: "+str(np.amin(error))

    #plt.xlim((0,52))
    #plt.ylim((0,1))
    #plt.plot(errorVisualT)
    #plt.xlabel(r"N\'umero del experimento")
    #plt.ylabel(r"Error $e$ traslaci\'on en cm")
    #plt.title(r"Gr\'afica de Traslaci\'on")
    #plt.plot(errorVisualT, label='Error producido')
    #Median = [np.average(errorVisualT)] * len(errorVisualT)
    #plt.plot(Median, label='Media Error')
    #plt.legend()
    #plt.show()

    #plt.xlim((0,52))
    #plt.ylim((0,math.pi))
    #plt.plot(errorVisualR)
    #plt.xlabel(r"N\'umero del experimento")
    #plt.ylabel(r"Error $e$ rotaci\'on en cm")
    #plt.title(r"Gr\'afica de Rotaci\'on")
    #plt.plot(errorVisualT, label='Error producido')
    #Median = [np.average(errorVisualR)] * len(errorVisualR)
    #plt.plot(Median, label='Media Error')
    #plt.legend()
    #plt.show()




    #infile = open(filename, 'r')
    #points = list()
    #for line in infile:
        #line = line.split("(")
        #line = line[1].split(")")[0].split(", ")
        #points.append(line)
    #infile.close()

    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #n = 100
    #xs = list()
    #ys = list()
    #zs = list()
    #for p in points:
        #xs.append(float(p[0]))
        #ys.append(float(p[1]))
        #zs.append(float(p[2]))
        
    #ax.scatter(xs,zs, ys, c='b', marker='o')
    #plt.title(r"Posici\'on Objectivo")
    #ax.set_xlabel(r'posici\'on X (mil\'imetros)')
    #ax.set_ylabel(r'posici\'on Z (mil\'imetros)')
    #ax.set_zlabel(r'posici\'on Y (mil\'imetros)')

    ##plt.show()













