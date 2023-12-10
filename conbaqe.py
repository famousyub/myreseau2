# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:34:39 2023

@author: G702306
"""




import matplotlib.pyplot  as plt
import  psycopg2

pgconn = psycopg2.connect(dbname="SAGEM",user='postgres',password='1234')
curso = pgconn.cursor()

curso.execute(""" select * from  produit1  """)

qut = dict()


for em in  curso:
    print(em[0])
    qut[em[0]] = em[2]
    

print(qut)


plt.bar(qut.keys(),qut.values(),width=0.5,color='green')

plt.show()
pgconn.close()