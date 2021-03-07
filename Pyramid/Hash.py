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
