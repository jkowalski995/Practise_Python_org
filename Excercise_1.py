import datetime

name = input("What's your name?")
age = int(input("How old are You?"))
multiply = int(input("Please, provide a number."))

today = datetime.date.today()
hundred_years = today.year + (100 - age)
i = 0
while i < multiply:
    print("Dear ", name, ". You will reach 100 years in year ", hundred_years)
    i += 1


