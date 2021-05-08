
import time
import os

print("Hello World")

z=input("Enter your password to continue:")
password=("Mathematics")

if password == z:
    print("You have successfully logged in.")
    

else:
    print("Wrong password.Try again")
    time.sleep(0.7)
    z=input("Enter your password to continue:")

    if password == z:
        print("You have successfully logged in.")

    else:
        print("Wrong password.Try again")
        time.sleep(0.7)
        z=input("Enter your password to continue:")


        if password ==z:
            print("You have successfully logged in.")

        else:
            print("Wrong password.Try again")
            time.sleep(0.7)
            z=input("Enter your password to continue:")

            if password ==z:
                print("You have successfully logged in.")

            else:
                print("You have been denied access!")
                print("INTRUDER ALERT!!AUTOMATIC SHUTDOWN!")
                os.system("shutdown /s /t 3")
