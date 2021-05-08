import time


print("Hello user. Lets begin this story.")
time.sleep(1)

while True:

    z=input("Enter in a random word you would like to do something mysterious to:")



    y=int(input('''Would you like to,
1=Change your word to uppercase
2=Check to see if string has any numbers
3=Count number of characters
4=Search for a letter and return the position:'''))

   

    if y == 1:
            z=z.upper()
            print(z)
            time.sleep(1.5)
            e=input("Would you like to enter another word?Enter Yes or No:")
            if e=="Yes" or e=="yes" or e=="YES":
               continue

            else:
                print("Thank u for playing")
                time.sleep(1)
                break
    elif y == 2:
            t=z.isalpha()
            if t== True:
             print("You do not have numbers in your word!")
             e=input("Would you like to enter another word?Enter Yes or No:")
             if e=="Yes" or e=="yes" or e=="YES":
               continue

             else:
                print("Thank u for playing")
                time.sleep(1)
                break
            
            elif t== False:
             print("You have at least one number in your word")
             e=input("Would you like to enter another word?Enter Yes or No")
             if e=="Yes" or e=="yes" or e=="YES":
               continue

             else:
                print("Thank u for playing")
                time.sleep(1)
                break

    elif y == 3:
             q=len(z)
             print(q)
             print("you have ",q," characters in your string")
             e=input("Would you like to enter another word?Enter Yes or No:")
             if e=="Yes" or e=="yes" or e=="YES":
               continue

             else:
                print("Thank u for playing")
                time.sleep(1)
                break

    elif y == 4:
            h=input("Which letter do u want to find?:").lower()
            r=(z.find(h))
            if r<0:
                print("Your letter does not exist you fob.")

            else:
                print(r)

            
                
            e=input("Would you like to enter another word?Enter Yes or No:")
            if e=="Yes" or e=="yes" or e=="YES":
               continue

            else:
                print("Thank u for playing")
                time.sleep(1)
                break
                  
                
    
      

      


