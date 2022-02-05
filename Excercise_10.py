import random

z = random.randint(5, 25)
y = random.randint(5, 25)
a = random.sample(range(10, 50), z)
b = random.sample(range(10, 50), y)
print("List: ", a)
print("List: ", b)

common = [c for c in b if c in a]
print(common)