import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from matplotlib import dates as mpl
plt.style.use('ggplot')
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]
y = [0, 1, 3, 4, 6, 5, 7]
plt.plot_date(dates,y,linestyle="solid")
plt.gcf().autofmt_xdate()
date_for = mpl.DateFormatter('%d,%b,%Y')
plt.gca().xaxis.set_major_formatter(date_for)
plt.show()