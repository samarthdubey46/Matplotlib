import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

Data = pd.read_csv("Barchart.csv")
counter = Counter()
id = Data['Responder_id']
langauge = Data['LanguagesWorkedWith']
l = []
p = []
for i in langauge:
    counter.update(i.split(";"))
for i in counter.most_common(15):
    l.append(i[0])
    p.append(i[1])
plt.style.use('dark_background')
l.reverse()
p.reverse()
plt.barh(l,p)
# plt.gca().xaxis()
plt.tight_layout()
plt.show()
