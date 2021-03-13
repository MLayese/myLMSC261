for s in range(1,101):
    string = ""
    if s % 3 == 0:
        string = string + "Fizz"
    if s % 5 == 0:
        string = string + "Buzz"
    if s % 5 != 0 and s % 3 != 0:
        string = string + str(s)
    print(string)