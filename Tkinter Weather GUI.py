from tkinter import *



def Heads():
   
        lbl=Label(window,text="DRESS FOR HOT WEATHER")
        lbl.grid(column=0,row=5)
def Tails():
        lbl=Label(window,text="")
        lbl.grid(column=0,row=5)


    



window=Tk()
window.title("Bus Fare")
window.geometry('300x100')

lbl= Label(window,text="                What should i wear today?")
lbl.grid(column=0,row=0)

lbls=Label(window,text="Click on the Button that describe's today's weather")
lbls.grid(column=0,row=1)

Sunny=Button(window,text="Heads",command=lambda:Heads())
Sunny.grid(column=1,sticky=W,row=3)

Rainy=Button(window,text="Tails",command=lambda:Tails())
Rainy.grid(column=2,row=3)



window.mainloop()

