# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:44:03 2023

@author: G702306
"""



from tkinter import  * 

from PIL  import Image,ImageTk


window =Tk()


window.title('Parametrage')



window.geometry("500x500")


def   clicked():
    res = 'Ok'
    lbl.configure(text=res)
    #txt.setattr(text='bnj sagemcom')
    
    
    
lbl =Label(window, text='numero carte:')

lbl.grid(column=0,row=0)



btn= Button(window,text='click me',bg='white',fg='red',command=clicked)

btn.grid(column=1,row=1)

 
btnh= Button(window,text='exit me',bg='white',fg='purple',command=window.destroy)

btnh.grid(column=2,row=1)




txt =Entry(window,width=10)


from tkinter.ttk import Combobox


txt.grid(column=1,row=0)

txt.focus()

combo = Combobox(window)

combo['values']= ('panne tecknique' , 'panne   soft' , 'panne reseau', 'passage ok ','pasaage ko')
combo.current(1)
combo.grid(column=3,row=1)









#d = Entry(window)


#d.pack()















selected  =IntVar()






rad1 = Radiobutton(window,text='port 1 ',value=1,variable=selected)
rad2 = Radiobutton(window,text='port  2',value=2,variable=selected)
rad3 = Radiobutton(window,text='port 3',value=3,variable=selected)
 







rad1.grid(column=0,row=4)
rad2.grid(column=1,row=4)
rad3.grid(column=2,row=4)



def clicked2():
    res ="Port " + txt.get() + " Messsage " + combo.get() + " " + str(selected.get())  + " "    + str(selected.get())
    lbl2.configure(text=res)




ok= Button(window,text='test',bg='white',fg='purple',command=clicked2)

ok.grid(column=2,row=5)

    
lbl2 =Label(window, text='')

lbl2.grid(column=1,row=12)

"""canvas = Canvas(window,width=100,height=100,bg='white')
img_ = PhotoImage(file="sagem.png")
canvas.create_image(0,0,anchor=NW,image=img_)
canvas.gird(column=2,row=1,columnspan=2)
"""

ok.grid(column=2,row=5)
 
    
lbl2 =Label(window, text='')
 
lbl2.grid(column=1,row=12)
 
canvas = Canvas(window,width=100,height=100,bg='white')
img = PhotoImage(file="sagem1.png")
canvas.create_image(0,0,anchor=NW,image=img)
canvas.grid(column=2,row=5,columnspan=2)
 

window.mainloop()


