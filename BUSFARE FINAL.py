from tkinter import *

def busfare(event):
    age=int(txt.get())
    if age>18:
     fare=4.00
     lbl= Label(window,text="Busfare running $4.00")
     lbl.grid(column=0,row=5)
     
    elif age<=18:
     fare= 2.50
     lbl= Label(window,text="Busfare running $2.50")
     lbl.grid(column=0,row=5) 
        

window=Tk()
window.title("Bus Fare")
window.geometry('300x100')

lbl= Label(window,text="Enter age and then press Return")
lbl.grid(column=0,row=0)

txt= Entry(window,width=35)
txt.grid(column=0,row=1)
txt.focus()



txt.bind('<Return>',busfare)

window.mainloop()
