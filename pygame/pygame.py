import os
import time



def adding(num1, num2):
    print("the answer : ")
    print(num1+num2)
def removing(num1,num2):
    
    print(num1-num2)
def multiply(num1,num2):
    print("the answer : ")
    print(num1*num2)
def devide(num1,num2):
    if(num1 > num2):
        print("the answer : ")
        print(float(num1/num2))
    elif(num1 <num2):
        print("the answer : ")
        print(float(num2/num1))
def paused():
    while(True):
        time.sleep(1)
        pause = input("paused press enter to continue")
        if(pause != "1"):
            break
        


system = os.system

system("color a")
system("mode con cols=79 lines=20")
while(True):
    system("cls")
    print("\n\n\n")
    print("                    /\        |    |     0                           ")
    print("                   /  \       |    |     |                           ")
    print("                  /----\      |----|     |                           ")
    print("                 /__()__\     |    |     |                           ")
    print("                /________\    |    |     |                           \n\n")
    command = input("command : ")
    while(command == "math"):
        system("cls")
        print("Please select type :")
        print("1. adding\n")
        print('2. multiply\n')
        print("3. devide\n")
        print('3. remove\n')
        print("type in 'back' to back to the main menu")
        choice = input("choice : ")
        if(choice == '1'):
            n1 = int(input("1st num to add : "))
            n2 = int(input("2nd num to add : "))
            adding(n1,n2)
            paused()

        if(choice == '2'):
            n1 = int(input("1st num to multiply : "))
            n2 = int(input("2nd num to multiply : "))
            multiply(n1,n2)
            paused()
        
        if(choice == '3'):
            n1 = int(input("1st num to devide : "))
            n2 = int(input("2nd num to devide : "))
            devide(n1,n2)
            paused()
            

        if(choice == '4'):
            n1 = int(input("1st num to remove : "))
            n2 = int(input("2nd num to remove : "))
            removing(n1,n2)
            paused()

        if(choice == 'back'):
            system("cls")
            break
    while(command == "ip lookup"):
        print('to go back please enter "back"\n\n')
        ip = input("enter ip : ")
        if(ip != "back"):
            system("nslookup "+ip)
            paused()
        if(ip == "back"):
            break
    while(command == "color"):
        system("cls")
        print("The command is : [color of the backround][color of the text] ")
        print(" color code | color name")
        print("      0     |    black  ")
        print("      1     |    blue   ")
        print("      2     |    green  ")
        print("      3     |    cyan   ")
        print("      4     |     red   ")
        print("      5     |   magenta ")
        print("      6     |  yellow/brown")
        print("      7     |    white  ")
        print("      8     |    gray   ")
        print("      9     | bright blue")
        print("      a     | bright green")
        print("      b     | bright cyan")
        print("      c     | bright red")
        print("      d     | bright pink")
        print("      e     | bright yellow")
        print("      f     | white(idk why)")
        color = str(input("color of the backround (make it 0 for standart ) : "))
        color2 = str(input("color of the text (a for standart)  : "))
        system("color "+color+color2)
        print("\n\n the color has changed :d")
        paused()
        break

        
