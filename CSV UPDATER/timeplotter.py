import matplotlib.pyplot as plt
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight"
              )
def a(i):
    data = pd.read_csv("test1.csv")
    x =data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x,y1,label="Chanel 1",color='#fc00c2')
    plt.plot(x,y2,label = 'Chanel 2',color='#e5ff00')
    plt.tight_layout()
    plt.legend(loc='upper left')
ani = FuncAnimation(plt.gcf(),a,interval=1000)
plt.tight_layout()
plt.show()