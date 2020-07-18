import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("hist.csv")
age = data['Age']
plt.style.use("Solarize_Light2")
bins = [10,20,30,40,50,60,70,80,90,100]
plt.hist(age,bins=bins,log=True,label="Ages",edgecolor="black",color='red')
plt.ylabel("Responded")
plt.xlabel("Ages")
plt.legend()
plt.tight_layout( )
plt.show()
