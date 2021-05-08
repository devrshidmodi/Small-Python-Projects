import turtle
wn = turtle.Screen()
class BG():
    def bg():
        wn.bgpic("background.png")




t=turtle.Pen()
t.pensize(6)
t.pencolor('black')

class drawMan():
 def body():
    #Legs of Stick Man
    t.penup()                
    t.goto(-300, -100)       
    t.showturtle()
    t.pendown()
    t.left(45)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.penup()
    #Physical Body
    t.goto(-243.43145751,-43.43145751)#Co-Ordinates Found Using Right Angle Trigonometry!80sin(45)
    t.pendown()
    t.left(135)
    t.forward(100)
    t.right(90)
    #Face Outline
    t.begin_fill()
    t.circle(60)
    t.color('brown')
    t.end_fill()
    t.penup()
    t.goto(-243.43145751,15)
    t.pendown()
    t.color('black')
    t.forward(50)
    t.penup()
    t.goto(-293.43145751,15)
    t.pendown()
    t.forward(50)



    t.penup()
    t.goto(-220,136.5685425)
    t.pendown()
    t.circle(10)

    t.penup()
    t.goto(-219,144.5685425)
    t.pensize(2)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(3)
    t.end_fill()


    t.penup()
    t.pensize(6)
    t.color("black")
    t.goto(-266.862915,136.5685425)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(-265.862915,142.5685425)
    t.pendown()
    t.pensize(2)
    t.color("brown")
    t.begin_fill()
    t.circle(3)
    t.end_fill()



    t.penup()
    t.goto(-260.862915,96.5685425)
    t.color("black")
    t.pensize(6)
    t.pendown()
    t.forward(40)




    t.penup()
    t.goto(-243.4314575,5)
    t.right(20)
    t.pendown()
    t.forward(240)



    t.penup()
    t.goto(-9,-75)
    t.pendown()
    t.left(110)
    t.forward(50)
    t.right(120)
    t.forward(30)
    t.penup()
    t.goto(-9,-75)
    t.left(70)
    t.pendown()
    t.forward(30)
    t.right(150)
    t.circle(50,340)
    t.penup()
    t.goto(81,-40)
    t.pendown()
    t.circle(7.5)
    t.penup()
    t.goto(61,-40)
    t.pendown()
    t.circle(7.5)
    t.penup()
    t.goto(61,-70)
    t.left(40)
    t.pendown()
    t.circle(14,180)

drawMan.body()
BG.bg()
