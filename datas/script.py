
import numpy as np
import matplotlib.pyplot as plt


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


#print errorVisualT
#print errorVisualR

#print np.average(errorVisualT)
#print np.average(errorVisualR)

print np.amax(errorVisualT)
print np.amax(errorVisualR), np.amax(errorVisualR)/float(3.14/float(2))*100

#print np.amin(errorVisualT)
#print np.amin(errorVisualR)

#plt.plot(errorVisualT),plt.show()
#plt.plot(errorVisualR),plt.show()
#deverrorVisualT  =
#plt.errorbar(errorVisualT,deverrorVisualT),plt.show()
