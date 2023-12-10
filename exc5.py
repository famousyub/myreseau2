# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:03:20 2023

@author: G702306
"""


import random 


a = random.randint(1, 100)


dif = int(input("enter degree  difficile 4 7 12") )

i = 0
while True  :
    
    
    f = int(input("enter   un  numero enter entre 1 et  100 "))
    i+= 1
    if   f  >  a  :
        print("{}  >  a cellll  num".format(f)) 
        if dif == i :
            print("mtle3thech :p Surpris")
            break
       
    elif  f < a :
        print("{} <   a cellll  num".format(f))
        if dif== i :
            print("mtle3thech :p Surpris")
            break
      
    
    
    else :
        print("bravooo  "  )
        break
    
    
print("tu found  {} apres {} ".format(f,i))