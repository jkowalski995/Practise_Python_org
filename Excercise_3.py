a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#main task
for i in a_list:
    if i < 5: print(i)

#Extras_1
b_list = []
for i in a_list:
    if i < 5: b_list += [i]
print(b_list)

#Extras_1&2
print([ i for i in a_list if i < 5])

#Extras_3
number = int(input("Please, provide a number."))

b_list = []
for i in a_list:
    if i < number: b_list += [i]
print(b_list)