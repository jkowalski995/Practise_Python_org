birthday_dict = {"Paulina": 19.01, "Kuba": 11.05, "Magdalena": 08.03, "Konstanty": 22.04,
                 "Mirosława": 05.04, "Andrzej": 17.01}
error = "This person not exist on the list"

print("Welcome to Birthday Dict")
print("Already available are:")

keys_ = list(birthday_dict.keys())

for i in range(len(keys_)):
    print(keys_[i], end="\n")

key = input("Who birthday's do You want to know?")

birthday = birthday_dict.get(key, error)

if birthday == error:
    print(error)
else:
    print("Dear {} your birthday is on {}".format(key, birthday))
