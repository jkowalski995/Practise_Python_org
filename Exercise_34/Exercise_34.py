import json

error = "This person not exist on the list"

while True:
    decision = input("Do You want to (R)ead data or (W)rite data?. To end type (E)")
    if decision.lower() == "r":

        key = input("Who birthday's do You want to know?")

        with open("info.json", "r") as f:
            dates = json.load(f)

        birthday = dates.get(key, error)

        if birthday == error:
            print(error)
        else:
            print("Dear {} your birthday is on {}".format(key, birthday))
        f.close()
    elif decision.lower() == "w":

        name = input("Please provide Name: ")
        birth = input("Please provide Date of birth: ")

        tmp_dict = {name: birth}

        with open("info.json", "r") as f:
            dates = json.load(f)
        f.close()

        dates.update(tmp_dict)

        with open("info.json", "w") as f:
            json.dump(dates, f)
        f.close()
    elif decision.lower() == "e":
        break
    else:
        print("You typed wrong letter. Try again")
        continue
