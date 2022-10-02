import matplotlib.pyplot as plt
import numpy as np


def powerTen(a):
    for i in range(0,len(a)):
        a[i] = 10**a[i]
    return(a)



file = open('data.dat')
lst = []

for line in file:
    lst += [line.split()]

print("hello")
counter = 0

for x in lst:
    print(float(x[0])+2)
    counter += 1
    if counter > 100:
        break
    
ID = []
V = []
BV = []
Para = []
Uncert = []
size=[]
colors = []

for i in lst:
    if float(i[2]) < 2.25:
        ID.append(float(i[0]))
        V.append(float(i[1]))
        BV.append(float(i[2]))
        #Para.append(float(i[3]))
        #Uncert.append(float(i[4]))
        size.append(7)




x = np.array(BV)
y = np.array(V)


x = powerTen(x) #Place a # in front of these two lines to make the log-log plots
y = powerTen(y)


#You can use the following three lines to change the xy-axes bounds if you want to change your plot.
#ax = plt.gca() #Uncomment these when making the log-log plots by deleting the # in the very front
#ax.set_xlim([-0.5, 2.25])
#ax.set_ylim([20, -2])


plt.scatter(x,y, size, alpha=0.75, c=x, cmap='turbo') #size is the size of the data points
plt.xlabel("B-V Color")
plt.ylabel("Absolute Magnitude")
plt.show()
