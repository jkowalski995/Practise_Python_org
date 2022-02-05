import random
import functions

z = random.randint(2, 25)

a = random.sample(range(1, 26), z)
print(a)
print(functions.beg_end(a))