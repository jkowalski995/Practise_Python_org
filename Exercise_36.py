import json
from collections import Counter
from bokeh.plotting import figure, show, output_file
import math

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

counted_months = Counter(months)

months, counts = list(zip(*counted_months.items())) # zip creates a tuple from iterables
# The asterisk, *, or unpacking operator, unpacks counted_months list, and passes the values, or elements,
# of counted_months list as separate arguments to the zip function.

cats = list(num_to_string.values())

output_file("plot.html")

p = figure(x_range=cats, title="Birthday Months")
p.xaxis.major_label_orientation = math.pi/4 # Rotates labels pi/4
p.vbar(x=months, top=counts)
show(p)
