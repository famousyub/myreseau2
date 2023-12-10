# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:15:55 2023

@author: G702306
"""

import matplotlib.pyplot as plt 
from math import *

y = [i ** 2 / pi   + cos(i * pi) **3 + i/2*sin(i) for  i  in  range(11) ]



plt.plot(y)




plt.savefig("C:\\Users\\g702306\\Desktop\\testy000\\formationpython\\df.png")
plt.savefig("C:\\Users\\g702306\\Desktop\\testy000\\formationpython\\ert.png")
plt.show()