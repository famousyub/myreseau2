# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:11:10 2023

@author: G702306
"""



import numpy   as np



lm = np.array([t for t in range(10)])


print(lm)


import matplotlib.pyplot as plt

data = {'C': 20, 'C++': 34,'java': 30, 'Python':42}
Formations=list(data.keys())
Valeurs=list(data.values())

plt.bar(Formations, Valeurs, color= 'blue', width= 0.4)
plt.xlabel('Formations IT')
plt.ylabel('Nombre personnels formés')
plt.title('Formation SAGEMCOM')
plt.show()
