import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Fill_Between.csv")
age = data['Age']
python = data['Python']
all_devs = data['All_Devs']
plt.style.use('ggplot')
plt.plot(age,all_devs,label="All_devs",linestyle='--',color='red')
plt.plot(age,python,label="Python")
mean = 57287
plt.fill_between(age,python,all_devs,alpha=.5,where=(python > all_devs),interpolate=True,label="Above Avg")
plt.fill_between(age,python,all_devs,alpha=.5,where=(python <= all_devs),interpolate=True,label="Below Avg")
plt.legend()
plt.show()
