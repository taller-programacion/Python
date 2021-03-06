# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

values = ["Aprobados", "No aprobados", "deserción", "NP"]
data = [2, 10, 20, 10]
expl =(0.05, 0.05, 0, 0)

fig, plot = plt.subplots()
plot.pie(data, explode=expl, labels=values, autopct='%1.1f%%', shadow=True, startangle=90)

fig.savefig("graph.png")
plt.show()