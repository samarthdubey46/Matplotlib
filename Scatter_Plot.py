import matplotlib.pyplot as plt
import pandas as pd
import random as r
x = []
y = []
#MAKING RANDOM VALUES
for i in range(10):
    s =r.randint(1,10)
    x.append(s)
    d =r.randint(1,10)
    y.append(d)
plt.style.use('seaborn')
plt.scatter(x,y,edgecolors='black',linewidths=1,cmap='bwr',c=[1,2,3,4,5,6,7,8,9,10])
plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar()
cbar.set_label("Random")
plt.show()