# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:18:24 2023

@author: G702306
"""



import matplotlib.pyplot  as plt
import  psycopg2

import pandas as pd

pgconn = psycopg2.connect(dbname="SAGEM",user='postgres',password='1234')
curso = pgconn.cursor()

curso.execute(""" select * from  produit1  """)

qut = dict()
price = []

for em in  curso:
    print(em[0])
    qut[em[0]] = int(em[2])
    price.append(float(em[1]))
    
    

print(qut)





new_data = pd.DataFrame({'nom':qut.keys() , 'quantity' :qut.values() ,'price':price})



new_data.to_excel('noveau_fichierr22quanty.xlsx',index=False)


pgconn.close()