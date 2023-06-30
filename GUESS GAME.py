#!/usr/bin/env python
# coding: utf-8

# In[1]:


from colorama import Fore,Back,Style
import time
a=38
inp=(input('''Do you want to play game
                      1.Yes
                      2.No
           '''))
if inp=="yes":
    b=int(input("How many chances you want, To Guesss the Number.."))
    print("Game will Start after....")
    time.sleep(1)
    print(Fore.RED+"3...")
    time.sleep(1)
    print(Fore.YELLOW+"2...")
    time.sleep(1)
    print(Fore.GREEN+"1...")
    time.sleep(1)
    while b>0:
        print(b,Fore.RED+"chance left for Guess..")
        inp1=int(input(Fore.GREEN+"\nguess the number..\U0001F643\n"))
        if inp1<a:
            print(Fore.CYAN+"\nThis is Smaller then that Number..","\U0001F644")
            b-=1
        elif inp1>a:
            print(Fore.YELLOW+"\nThis is Greater then that Number.. ","\U0001F644")
            b-=1    
        elif inp1==a:
            print(Fore.GREEN,Back.BLACK+"\nCongrats... you WON the game..","\U0001F970")
            break
    else:
        print(Fore.YELLOW,Back.BLACK+"\nBetter luck next time..","\U0001F92A")
else:
    print(Fore.RED,Back.BLACK+"\nOkay...","\U0001F614")

