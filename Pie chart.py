import matplotlib.pyplot as plt
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0.,2,0.,.1,0.5]
colors = ['#ff9999','#66b3ff','#ffcc99','#99ff99','#ffa500']
plt.pie(slices,wedgeprops={'edgecolor':'black'},labels=labels,shadow=True,explode=explode,startangle=90,colors=colors,autopct='%1.1f%%')
plt.show()
# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f