# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:12:53 2023

@author: G702306
"""




import matplotlib.pyplot as  plt 

name = ['-18','18-25','25-50','50+']

data  = [5000, 26000,21400,12000]



explod = (0.35,0,0,0)

plt.pie(data, explode=explod, labels=name, autopct='%1.1f%%',startangle=90,shadow=True)




plt.axis('equal')

plt.savefig('pie122.jpg')
plt.show()