import math
a = int(input("Enter number you want to convert:"))
counter=0
y=[32768,16384,8192,4096,2048,1024,512,256,128,64,32,16,8,4,2,1]

for x in y:
    
    REMAINDER=a%x
    QUOTIENT=math.floor(a/x)
    if QUOTIENT==0:
        print(QUOTIENT, end = "")

    elif QUOTIENT==1:
        print(QUOTIENT, end = "")
        
        
    a=REMAINDER
    



