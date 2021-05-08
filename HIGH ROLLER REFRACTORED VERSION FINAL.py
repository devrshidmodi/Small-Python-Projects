from tkinter import *   #import the tkinter library
import tkinter as tk    #defines the imported content from the library as tk for faster typing

import random   
random.seed()  

class HighRoller(tk.Frame):
    
    def __init__(self, master=None):    
        tk.Frame.__init__(self, master) 
        self.grid()                     

        self.initializeScreen()         


    def initializeScreen(self):
        
        global uScore,cScore,userButton,compButton,gamePrompt,gameButton,scoreLabel
        
         
        uScore = IntVar()
        cScore = IntVar()

        uScore.set(0)
        cScore.set(0)

        
        header = tk.Label(self, text="High Roller",font="Arial 40 bold",fg="red")
        header.grid(row=0,column=0, columnspan=3)

        subHeader = tk.Label(self, text="You roll. The computer rolls. High Roller Wins.")
        subHeader.grid(row=1,column=0, columnspan=3)

        separate = tk.Frame(self,height=2, bd=1, relief=SUNKEN)
        separate.grid(row=2,column=0, columnspan=3)

        dice = tk.PhotoImage(file="blank.gif") 
        
               
        userLabel = tk.Label(self, text="Your Dice", font="Arial 18 bold")
        userLabel.grid(row=3,column=0)

        
        userDice = tk.Label(self, image=dice )
        userDice.grid(row=3,column=1)      
        userDice.image = dice               

        
        userButton = tk.Button(self, text="ROLL User", command=self.UserRoll, state=NORMAL)
        userButton.grid(row=3,column=2)

        
        compLabel = tk.Label(self, text="Comp Dice", font="Arial 18 bold")
        compLabel.grid(row=5,column=0)

        
        compDice = tk.Label(self, image=dice ) 
        compDice.grid(row=5,column=1)          
        compDice.image = dice                  


        
        
        compButton = tk.Button(self, text="ROLL Comp", command=self.CompRoll, state=DISABLED)
        compButton.grid(row=5,column=2)

        
        
        gamePrompt = tk.Label(self, text="Roll your dice to begin.", font="Arial 15 bold", fg="royal blue")
        gamePrompt.grid(row=7, column=0, columnspan=3)

        
        
        gameButton = tk.Button(self, text="Play Game", command=self.PlayAgain, state=DISABLED)
        gameButton.grid(row=8, column=0, columnspan=3)

        
        
        scoreLabel = tk.Label(self, text="Score:   USER " + str(uScore.get())+ "      COMP " + str(cScore.get()), font="Arial 12 bold")     
        scoreLabel.grid(row=9, column=0, columnspan=3)

        
    def UserRoll(self):
        
        print("User Roll")
        self.rollDice(True)
        userButton.configure(state=DISABLED)
        compButton.configure(state=NORMAL)
    def CompRoll(self):
        
        print("Computer roll")
        self.rollDice(False)
        
        compButton.configure(state=DISABLED)
        gameButton.configure(state=NORMAL)

        if userRoll > compRoll:
            gamePrompt.configure(text="YOU WIN")
            uScore.set(uScore.get()+1)
            scoreLabel.configure(text="Score:   USER "+str(uScore.get())+"    COMP "+str(cScore.get()))
            
            

        elif userRoll == compRoll:
                                 
            gamePrompt.configure(text="TIE")
           

        else :
           
            gamePrompt.configure(text="YOU LOSE!")
            cScore.set(cScore.get()+1)
            scoreLabel.configure(text="Score:   USER "+str(uScore.get())+"    COMP "+str(cScore.get()))
           

           
    def rollDice(self,userLocation):
        global userRoll,compRoll
        
        
        print ("Rolling Dice")
        roll = random.randint(1,6)
        print (roll)
        
        dice =  tk.PhotoImage(file="d"+str(roll)+".gif")
        
        
        if userLocation:
            userRoll=roll
            userDice = tk.Label(self,image=dice )
            userDice.grid(row=3,column=1)      
            userDice.image = dice
            
        else:
            compRoll=roll
            compDice = tk.Label(self, image=dice ) 
            compDice.grid(row=5,column=1)      
            compDice.image = dice
    def PlayAgain(self):
        
        userButton.configure(state=NORMAL)
        gameButton.configure(state=DISABLED)
        

        dice=tk.PhotoImage(file="blank.gif")

        userDice=tk.Label(self,image=dice)
        userDice.grid(row=3,column=1)
        userDice.image=dice

        compDice=tk.Label(self,image=dice)
        compDice.grid(row=5,column=1)
        compDice.image=dice        
        print("Another Round Accumulation Occurs")
            
        

    




 
window = HighRoller()   
window.master.title("High Roller")
window.master.geometry('300x500')  

 
window.mainloop()   
