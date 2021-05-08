a=int(input(""))
counter=0

import math

while True:
    b= a%10
    c= math.floor(a/10)

    d= c%10
    e=math.floor(c/10)

    f=e%10
    g=math.floor(e/10)

    h=g%10

    LIST1=[h,f,d,b]
    LIST2=[h,f,d,b]

    LIST1.sort()
    LIST2.sort(reverse=True)

    number1 = ""

    for i in range(len(LIST1)):
        number1 += str(LIST1[i])

    number2= ""

    for i in range(len(LIST2)):
        number2 += str(LIST2[i])




    counter+=1
    
    y = (int(number2)-int(number1))
    print(y)

    a = y

    if (y == 6174):
        print("Number of iterations:",counter)
        break
        

