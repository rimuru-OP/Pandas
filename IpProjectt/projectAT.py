# THIS IS MY IP CLASS 12 PROJECT..
import os
os.system("start cmd /c pip install keyboard")
import keyboard as kb
os.system("start cmd /c pip install pandas")
os.system("start cmd /c pip install random")
os.system("start cmd /c pip install numpy")
os.system("start cmd /c pip install matplotlib")
os.system("start cmd /c pip install sys")
os.system("start cmd /c pip install art")
os.system("start cmd /c pip install rich")
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import art
import rich
from rich.console import Console 
from rich.prompt import Prompt
# databases
f = os.path.dirname(os.path.abspath(__file__))
f = f.replace('c', 'C',1)
f = f.replace('\\', '/')
cons=Console()
#
pinn=input("Please Enter Your Name: ")
kb.press('f11')
print ('\033[1A\033[K')
inn = pinn+','
size = os.get_terminal_size()
clo = size.columns
print("\033[1A")
cons.print("\u2252"*clo,style="red on black")
art.tprint("Welcome")
print('\033[1A\033[K')
cons.print("\u2253"*clo,style="red on black")
cons.print("THIS PROJECT WILL HELP YOU", style='italic blue on black',justify="center")
cons.print('TO GET TO KNOW THE SCHOOLS OF', style='italic blue on black',justify="center")
cons.print("INDIA.", style='italic blue on black',justify="center")
cons.print(" ", style='black on black',justify="center")
cons.print("Hello "+inn, style='italic cyan on black',justify="center")
cons.print("Please choose the option that   ", style='italic cyan on black',justify="center")
cons.print("suits your interest from the menu given below:           ", style='italic cyan on black',justify="center")
cons.print("\u223D"*clo, style='red on black',justify="center")
#
lp=input("Shall we continue: ")
if lp == 'y':
    os.system('cls')
else:
    sys.exit()
p = 3
x = 2
while x<p:
    x+=1
    print('\033[1A\033[K')
    cons.print("\u2630"*clo, style=" red on black")
    cons.print("|----------Menu---------|", style="italic blue on black",justify="center")
    cons.print("| 1. Government Schools |", style='italic cyan on black',justify="center")
    cons.print("| 2. Central Schools    |", style='italic cyan on black',justify="center")
    cons.print("| 3. HRD Schools        |", style='italic cyan on black',justify="center")
    cons.print("| 4. Private Schools    |", style='italic cyan on black',justify="center")
    cons.print("| 5. Miscellaneous      |", style='italic cyan on black',justify="center")
    cons.print("| 6. Exit               |", style='italic cyan on black',justify="center")
    cons.print("\u2630"*clo, style='italic red on black')
    # PROGRAM Starts j
    print()
    k = int(Prompt.ask("Option :"))
    if k == 1:
        g = pd.read_csv(f+'/Government.csv')
        os.system('cls')
        cons.print("\u2630"*clo,style="red on black")
        cons.print("|      Choose one option      |",style="blue on black",justify='center')
        cons.print("| 1. Schools from Starting    |\n| 2. Schools from Last        |\n| 3. Specific Schools         |\n| 4. Bar Graph of schools     |\n|    and their strength       |\n| 5.Return To Menu            |",style="cyan on black",justify='center')
        cons.print("\u2630"*clo,style="red on black")
        q = int(input("Your choice :"))
        os.system("cls")
        print ('\033[1A\033[K')
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(g.head(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
             
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(g.tail(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 227] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 3] :"))
            print(g.iloc[m:t+1,n:r])
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q==4:
            lo=int(input("Range of rows first (from starting) [least:0]: "))
            ol=int(input("Range of rows last (from starting) [max:227]: "))
            plt.barh((g.iloc[lo:ol,2:3]).squeeze().tolist(),(g.iloc[lo:ol,3:4]).squeeze().tolist(),color=rd.choices(["g","b","r","orange","yellow","black"],k=ol-lo))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 5 :
            print ('\033[1A\033[K')
            os.system('cls')
            p+=1     
        else:
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
    elif k == 2 :
        h = pd.read_csv(f+'/Central.csv')
        os.system('cls')
        cons.print("\u2630"*clo,style="red on black")
        cons.print("|      Choose one option      |",style="blue on black",justify='center')
        cons.print("| 1. Schools from Starting    |\n| 2. Schools from Last        |\n| 3. Specific Schools         |\n| 4. Bar Graph of schools     |\n|    and their strength       |\n| 5.Return To Menu            |",style="cyan on black",justify='center')
        cons.print("\u2630"*clo,style="red on black")
        q = int(input("Your choice :"))
        print ('\033[1A\033[K')
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(h.head(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(h.tail(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 149] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 6] :"))
            print(h.iloc[m:t+1,n:r])
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q==4:
            lo=int(input("Range of rows first (from starting) [least:0]: "))
            ol=int(input("Range of rows last (from starting) [max:146]: "))
            plt.barh((h.iloc[lo:ol,1:2]).squeeze().tolist(), (h.iloc[lo:ol,7:8]).squeeze().tolist(),color=rd.choices(["g","b","r","orange","yellow","black"],k=ol-lo))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 5 :
            print ('\033[1A\033[K')
            os.system('cls')
            p+=1
        else:
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
    elif k == 3 :
        i = pd.read_csv(f+'/HRD.csv')
        os.system('cls')
        cons.print("\u2630"*clo,style="red on black")
        cons.print("|      Choose one option      |",style="blue on black",justify='center')
        cons.print("| 1. Schools from Starting    |\n| 2. Schools from Last        |\n| 3. Specific Schools         |\n| 4. Bar Graph of schools     |\n|    and their strength       |\n| 5.Return To Menu            |",style="cyan on black",justify='center')
        cons.print("\u2630"*clo,style="red on black")
        q = int(input("Your choice :"))
        print ('\033[1A\033[K')
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(i.head(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(i.tail(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 764] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 2] :"))
            print(i.iloc[m:t+1,n:r])
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q==4:
            lo=int(input("Range of rows first (from starting) [least:0]: "))
            ol=int(input("Range of rows last (from starting) [max:764]: "))
            plt.barh((i.iloc[lo:ol,2:3]).squeeze().tolist(),(i.iloc[lo:ol,3:4]).squeeze().tolist(),color=rd.choices(["g","b","r","orange","yellow","black"],k=ol-lo))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 5 :
            print ('\033[1A\033[K')
            os.system('cls')
            p+=1
        else:
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
    elif k == 4 :
        j = pd.read_csv(f+'/Private.csv')
        os.system('cls')
        cons.print("\u2630"*clo,style="red on black")
        cons.print("|      Choose one option      |",style="blue on black",justify='center')
        cons.print("| 1. Schools from Starting    |\n| 2. Schools from Last        |\n| 3. Specific Schools         |\n| 4. Bar Graph of schools     |\n|    and their strength       |\n| 5.Return To Menu            |",style="cyan on black",justify='center')
        cons.print("\u2630"*clo,style="red on black")
        q = int(input("Your choice :"))
        print ('\033[1A\033[K')
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(j.head(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(j.tail(m))
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 405] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 4] :"))
            print(j.iloc[m:t+1,n:r])
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q==4:
            lo=int(input("Range of rows first (from starting) [least:0]: "))
            ol=int(input("Range of rows last (from starting) [max:405]: "))
            plt.barh((j.iloc[lo:ol,2:3]).squeeze().tolist(),(j.iloc[lo:ol,3:4]).squeeze().tolist(),color=rd.choices(["g","b","r","orange","yellow","black"],k=ol-lo))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif q == 5 :
            print ('\033[1A\033[K')
            os.system('cls')
            p+=1
        else:
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
    elif k == 5:
        cons.print("\u2630"*clo,style="red on black")
        cons.print("|---------Choose from below--------|",style='italic blue on black',justify="center")
        cons.print("| 1. Sine function graph           |",style='italic cyan on black',justify="center")
        cons.print("| 2. Cosine function graph         |",style='italic cyan on black',justify="center")
        cons.print("| 3. Exponential function graph    |",style='italic cyan on black',justify="center")
        cons.print("| 4. Return to menu                |",style='italic cyan on black',justify="center")
        cons.print("\u2630"*clo,style="red on black")
        mon=int(input("Enter your choice:"))
        if mon==1:
            d = np.arange(0, 2*np.pi, 0.01)
            plt.plot(d,np.sin(d))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v== 'Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                print("lol")
                p=p+1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()       
        elif mon == 2:
            d = np.arange(0, 2*np.pi, 0.01)
            plt.plot(d,np.cos(d))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v=='y'or'Y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
                
        elif mon == 3:
            d = np.arange(0,10,0.01)
            plt.bar(d,np.e**d,color=rd.choices(["g","b","r","orange","yellow","black"],k=1001))
            plt.show()
            v=Prompt.ask("Do you want to return to menu(Y/N) :")
            if v =='Y'or'y':
                print ('\033[1A\033[K')
                os.system('cls')
                p+=1
            else:
                cons.print("\u29D1"*clo, style='italic cyan on black')
                cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
                cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
                cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
                cons.print("\u29D2"*clo, style='italic cyan on black')
                chp=Prompt.ask("Press any key to exit   ")
                if kb.read_key(chp)==True:
                    sys.exit()
        elif mon == 4:
            print ('\033[1A\033[K')
            os.system('cls')
            p+=1
        else:
            cons.print("\u29D1"*clo, style='italic cyan on black')
            cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
            cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
            cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
            cons.print("\u29D2"*clo, style='italic cyan on black')
            chp=Prompt.ask("Press any key to exit   ")
            if kb.read_key(chp)==True:
                sys.exit()              
    elif k == 6:
        cons.print("\u29D1"*clo, style='italic cyan on black')
        cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
        cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
        cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
        cons.print("\u29D2"*clo, style='italic cyan on black')
        chp=Prompt.ask("Press any key to exit   ")
        if kb.read_key(chp)==True:
            sys.exit()
    else:
        cons.print("\u29D1"*clo, style='italic cyan on black')
        cons.print("Made By ~ Annany Thakur  ", style='italic red on black',justify="left")
        cons.print("Roll No. 9 of 12th Alpha ", style='red on black')
        cons.print("  THANK YOU (～￣▽￣)~  ", style='red on black')
        cons.print("\u29D2"*clo, style='italic cyan on black')
        chp=Prompt.ask("Press any key to exit   ")
        if kb.read_key(chp)==True:
            sys.exit()

        
