# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:34:23 2023

@author: G702306
"""

import matplotlib.pyplot as plt 


dc_for = {'C' : 4700, 'Python' : 3800, 'Java' : 5200 , 'C#': 2800}

print(dc_for)





plt.bar(dc_for.keys(),dc_for.values(),width=0.4,color='blue')

plt.savefig("barr.png")
plt.show()

