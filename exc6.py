# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:53:19 2023

@author: G702306
"""

from math import *


a= int(input("enter a "))
b= int(input("enter b "))
c= int(input("enter c "))


if a == 0 :
    if b== 0 :
        if c==0:
            print("solution R")
        else:
            print("solution impossible")
    else  :
        print("solution est" ,  -c /b )
else :
    if b==0 :
        print("solution est " , sqrt(-c/b) )
        
    else :
        d = b**2- 4*a*c 
        if d > 0: 
            print("x1 = {} " .format((-b - sqrt(d)) / (2*a)))
            print("x2 = {}".format((-b + sqrt(d)) / (2*a)))
        elif  d== 0:
            print("x1 =x2" ,   (-b /2*a))
        
        
        else :
            print("pas soltion dans R")
        
    