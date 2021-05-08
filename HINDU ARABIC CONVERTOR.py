import math
a=int(input("Enter number:"))
y=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
counter=0
NUMERALS = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']


for x in y:
    
        REMAINDER=a%x
        QUOTIENT=math.floor(a/x)
        
        print(QUOTIENT*NUMERALS[counter],end="")
        a=REMAINDER
        counter+=1




    
