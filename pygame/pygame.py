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
system("mode con cols=95 lines=30")
while(True):
    system("cls")
    print("\n\n")
    print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   this is a experimental console , it will be changed after some time")
    print("█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█                         if you have questions commment      ")
    print("█░░║║║╠─║─║─║║║║║╠─░░█                             or ask me when im active           ")
    print("█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█                     at tuugii0660#6913 (ha its the sex number)     ")
    print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\n           type in help to see the commands \n\n")
    command = input("         command : ")
    while(command == "help"):
        print("\n\n commands : \n 1. math \n 2.ip lookup(look up ip of a website) \n 3.color (change color )")
        paused()
        print("\n\n\n\n\n")
        break
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
        system("cls")
        print("                            ,-.")
        print("       ___,---.__          /'|`\          __,---,___")
        print("    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.")
        print("  ,'        |           ~'\     /`~           |        `.")
        print(" /      ___//              `. ,'          ,  , \___      \ ")
        print("|    ,-'   `-.__   _         |        ,    __,-'   `-.    |")
        print("|   /          /\_  `   .    |    ,      _/\          \   |")
        print("\  |           \ \`-.___ \   |   / ___,-'/ /           |  /")
        print(" \  \           | `._   `\\  |  //'   _,' |           /  /")
        print("  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'")
        print("     ``       /     \    ,='/ \`=.    /     \       ''")
        print("             |__   /|\_,--.,-.--,--._/|\   __| ")
        print("             /  `./  \\`\ |  |  | /,//' \,'  \ ")
        print("            /   /     ||--+--|--+-/-|     \   \ ")
        print("           |   |     /'\_\_\ | /_/_/`\     |   |")
        print("            \   \__, \_     `~'     _/ .__/   /")
        print("             `-._,-'   `-._______,-'   `-._,-'")
        print('\n\n      to go back please enter "back"\n\n')
        ip = input("     enter ip or url : ")
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
    


        
