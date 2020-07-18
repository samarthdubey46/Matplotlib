from matplotlib import pyplot as plt
import matplotlib.dates as mpl
import pandas as pd
plt.style.use('dark_background')
data = pd.read_csv("time.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values("Date",inplace=True)
pr_date = data["Date"]
pr_close = data["Close"]
plt.plot_date(pr_date,pr_close,color="#fc00c2",linestyle="solid")
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()