import json
from collections import Counter

with open("info.json", "r") as f:
    dates = json.load(f)

# Dates in info.json are as DD.MM and every date is in ""

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = []

for name, birthday in dates.items():
    month = int(birthday.split(".")[1])
    months.append(num_to_string[month])

print(Counter(months))