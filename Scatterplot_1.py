import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Scatter_plot.csv')
view = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.style.use("dark_background")
plt.scatter(view,likes,edgecolors='black',cmap='winter',c=ratio)
plt.xscale('log')
plt.yscale("log")
plt.title("Youtube Trending Videos")
plt.tight_layout()
cbar = plt.colorbar()
cbar.set_label("Views : Likes")
plt.show()