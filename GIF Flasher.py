#Devrshi Modi
#April 11,2018
#This code will flash a GIF across the screen.
#Screen Size is 1000 by 500 pixels


import turtle,time,random

wn = turtle.Screen()
wn.bgcolor("#f442a1")


t=turtle.Turtle()
t.penup()
t.goto(0,0)                                                                   #Initial Co-ordinates
t.speed(0)                                                                    #Fastest Speed
turtle.register_shape("LION123.gif")                                          #Register GIF
t.shape("LION123.gif")


                                                      

for x in range(500):                                                          #Executes 500 times

 screenwidth=1000                                                             #Screenwidth Variable
 screenheight=500                                                             #Screenheight variable  
 t.hideturtle()
 time.sleep(0.3)                                                               #Delay of 0.3 seconds
 a=random.randint((-screenwidth/2),(screenwidth/2))                            #Screen Width Defined
 b=random.randint((-screenheight/2),(screenheight/2))                          #Screen Height defined
 t.goto(a,b)                                                                   #Range of x and y coordinates from -225 to 225
 t.showturtle()                                                                #Shows turtle when it goes to random co-ordinate
 time.sleep(0.3)                                                               #Delay of 0.3 seconds
                                                                               #Hides turtle when moving
                                                               



    
    

   
    


    
