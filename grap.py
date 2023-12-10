# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:53:51 2023

@author: G702306
"""





from tkinter import * 


fenetre =   Tk()

fenetre.title("Hello")
fenetre.geometry("640x480")

fenetre.resizable(width=False, height=False)




label = Label(fenetre, text="fenetre hello world")

button=Button(fenetre , text="quiter0" , command=fenetre.destroy)





champ = Entry(fenetre,width=100)







label.pack()
button.pack()

champ.pack()


fenetre.mainloop()
