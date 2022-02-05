import functions
import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
z = random.randint(5, 25)
y = random.randint(5, 25)
a = random.sample(range(10, 50), z)
b = random.sample(range(10, 50), y)
print("List: ", a)
print("List: ", b)
if len(a) > len(b):
    print("Common numbers are: ", functions.common(a, b))
else:
    print("Common numbers are: ", functions.common(b, a))