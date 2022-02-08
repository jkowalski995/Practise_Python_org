from functions import list_app, bin_se

new_list = []

counter = int(input("How much arguments do want in the list?\n"))

for i in range(0, counter, 1):
    element = input("Write list element: ")
    new_list.append(element)

number = input("Provide number to check it appearance in the list\n")

print("Answer: ", list_app(new_list, number))
print("Answer: ", bin_se(new_list, number))
