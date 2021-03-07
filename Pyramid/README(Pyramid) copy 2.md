# Hash ReadMe File

## Description
I actually had a like one or two issues with this
It took one or two attempts to realize my first print had to be " " and not "" or it would've been reflected on the wrong side.
My last print statement ("\r") was added in when I noticed print"\n" added an extra unnecessary space.

Created a new folder in 'mylmsc261' called 'Pyramid' and created this README.md

Opened PyCharm CE and creat "Hash.py"

Here's the code
def hash(p):
   X = 2*p - 2
   for m in range(0, p):
      for n in range(0, X):
         print(end=" ")
      X = X - 2
      for n in range(0, m+1):
         print("* ", end="")
      print("\r")
p = int(input("How tall do you want the pyramid?\n Name any number: "))
hash(p)

Saved it

Transported "Hash.py" into myLMSC261/Pyramid

Opened terminal and cd Desktop/LMSC261/myLMSC261/Pyramid

input the following "python3 Hash.py"

Doubled checked to make sure everything was running and sent it in

