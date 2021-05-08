


import time

while True:
 
   
      
   a=float(input("Enter the value of a:\n"))
   b=float(input("Enter the value of b:\n"))
   c=float(input("Enter the value of c:\n"))

   x= (-b)/(2*a)
   y=(a*(x**2))+(b*x)+c

   print((x,y))
   q=int(input("Do you want to enter another equation?1=Yes,2=No:\n"))
   if q==1:
       continue
   else:
       break



      

