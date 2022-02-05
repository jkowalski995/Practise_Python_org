num = int(input("Please, provide a number to calculate it's divisors: "))
i = 1
d_list = []
while i <= num:
    if num % i == 0:
        d_list += [i]
    i += 1
print("Divisors of number ", num, " are ", d_list)