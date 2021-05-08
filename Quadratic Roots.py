import time
import math

while True:
 a=float(input("A:"))
 b=float(input("B:"))
 c=float(input("C:"))
 if (b**2)-(4*a*c)>0:
  x1=(-(b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
  x2=(-(b)- math.sqrt((b**2)-(4*a*c)))/(2*a)
 
  print("You have two real solutions")
  time.sleep(0.8)
  print("X1=",x1,)
  print("X2=",x2,)
  z=int(input("Do you want to input other values?1=Yes,2=No:"))
  if z == 1:
          continue
  elif z == 2:
          print("Thank you for playing")
          break
  else:
          print("Follow the rules boiii!")
          break

 if (b**2)-(4*a*c)==0:
    x=(-(b))/(2*a)
    print("You have  one real solution")
    time.sleep(0.8)
    print("X=",x,)
    k=int(input("Do you want to input other values?1=Yes,2=No:"))
    if k == 1:
          continue
    elif k == 2:
          print("Thank you for playing")
          break
    else:
          print("Follow the rules boiii!")
          break

 if (b**2)-(4*a*c)<0:
    print("NO real solutions")
    z=int(input("Do you want to input other values?1=Yes,2=No:"))
    if z == 1:
          continue
    elif z == 2:
          print("Thank you for playing")
          break
    else:
          print("Follow the rules boiii!")
          break

    
    
    
