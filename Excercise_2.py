num = int(input("Please, provide a number to check."))
check = int(input("Please, provide another number to check."))

if num % 4 == 0:
    print("The number ", num, " is multiple of 4")
elif num % 2 == 0:
    print("The number ", num, " is even")
else:
    print("The number ", num, " is odd")

if num % check == 0:
    print("Check ", check, " divides evenly into num ", num)
else:
    print("Check ", check, " didn't divides evenly into num ", num)