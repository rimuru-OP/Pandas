# THIS IS MY IP CLASS 12 PROJECT..
import fontstyle as fts
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import random as rd
os.system("start cmd /k pip install fontstyle")
os.system("start cmd /k pip install pandas")
os.system("start cmd /k pip install math")
os.system("start cmd /k pip install random")
os.system("start cmd /k pip install numpy")
os.system("start cmd /k pip install matplotlib")
# databases
f = os.path.dirname(os.path.abspath(__file__))
f = f.replace('c', 'C',1)
f = f.replace('\\', '/')
g = pd.read_csv(f+'/Government.csv')
h = pd.read_csv(f+'/Central.csv')
i = pd.read_csv(f+'/HRD.csv')
j = pd.read_csv(f+'/Private.csv')
#
print(fts.apply("           Welcome           ", 'bold/BLINK/red/black_bg'))
print(fts.apply("THIS PROJECT WILL HELP YOU   ", 'bold/italic/CYAN/black_bg'))
print(fts.apply('TO GET TO KNOW THE SCHOOLS OF', "bold/italic/CYAN/black_bg"))
print(fts.apply("INDIA.                       ", 'bold/italic/CYAN/black_bg'))
print(fts.apply("Please enter your name :     ", 'CYAN/black_bg'))
c = input()
print(fts.apply("\nHello "+c +
      " Please choose the\noption that suits your interest: ", 'CYAN/black_bg'))
#
e = fts.apply("|", 'green/black_bg')
d = fts.apply("-*-*-*-*-*-*-Menu-*-*-*-*-*-*-*", 'italic/green/black_bg')
p = 1
x = 0
while x<p:
    x+=1
    print("\n", e+d)
    print('', e, "1. Government Schools       ", e)
    print('', e, "2. Central Schools          ", e)
    print('', e, "3. HRD Schools              ", e)
    print('', e, "4. Private Schools          ", e)
    print('', e, "5. Miscellaneous            ", e)
    print('', e, "6. Exit                     ", e)
    print("", fts.apply("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", 'italic/green/black_bg')+e)
    # PROGRAM Starts j
    print()
    k = int(input(fts.apply("Option :",)))
    if k == 1:
        print("\nYou want to see :\n1. Schools from Starting\n2. Schools from Last\n3. Specific Schools\n4. Return To Menu\n5.histogram")
        q = int(input("Your choice :"))
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(g.head(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
            sys.exit()
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(g.tail(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 226] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 3] :"))
            print(g.iloc[m:t+1,n:r])
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 4 :
            p+=1     
        else:
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
    elif k == 2 :
        print("\nYou want to see :\n1. Schools from Starting\n2. Schools from Last\n3. Specific Schools\n4. Return To Menu")
        q = int(input("Your choice :"))
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(h.head(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(h.tail(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 149] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 6] :"))
            print(h.iloc[m:t+1,n:r])
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 4 :
            p+=1
        else:
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
    elif k == 3 :
        print("\nYou want to see :\n1. Schools from Starting\n2. Schools from Last\n3. Specific Schools\n4. Return To Menu")
        q = int(input("Your choice :"))
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(i.head(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(i.tail(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 764] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 2] :"))
            print(i.iloc[m:t+1,n:r])
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 4 :
            p+=1
        else:
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
    elif k == 4 :
        print("\nYou want to see :\n1. Schools from Starting\n2. Schools from Last\n3. Specific Schools\n4. Return To Menu")
        q = int(input("Your choice :"))
        if q == 1:
            m = int(input("Number of rows you want to see from first :"))
            print(j.head(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 2:
            m = int(input("Number of rows you want to see from first :"))
            print(j.tail(m))
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 3:
            m = int(input("Range of rows you want (first) :"))
            t = int(input("Range of rows you want (second) [max 405] :"))
            n = int(input("Range of columns you want (first) :"))
            r = int(input("Range of columns you want (second) [max 2] :"))
            print(j.iloc[m:t+1,n:r])
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        elif q == 4 :
            p+=1
        else:
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
    elif k == 5:
        print('',"1. sine function graph       ")
        print('',"2. cosine function graph     ")
        print('',"3. exponential function graph")
        print('',"4. Return to menu            ")
        mon=int(input("Enter your choice:"))
        if mon==1:
            x = np.arange(0, 2*np.pi, 0.01)
            plt.plot(x,np.sin(x))
            plt.show()
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
                sys.exit()
        elif mon == 2:
            x = np.arange(0, 2*np.pi, 0.01)
            plt.plot(x,np.cos(x))
            plt.show()
            v=input("Do you want to return to menu(Y/N) :")
            if v== 'Y':
                p+=1
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
                sys.exit()
        elif mon == 3:
            x = np.arange(0,10,0.01)
            plt.bar(x,np.e**x,color=rd.choices(["g","b","r","orange","yellow","black"],k=1001))
            plt.show()
            pass
            v=input("Do you want to return to menu(Y/N) :")
            print()
            if v== 'Y':
                p+=1
                pass
            else:
                print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
                sys.exit()
        elif mon == 4:
            p+=1
        else:
            print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
            sys.exit()
    elif k == 6:
        print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        sys.exit()
    else:
        print(fts.apply("         THANK YOU(～￣▽￣)~", 'CYAN/black_bg'))
        sys.exit()
        
