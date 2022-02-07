from functions import pass_gen

# a = int(input("How long password do You want?"))
a = int(input("How strong password do You want?\n"
              "Type 1 for weak password (8 characters)\n"
              "Type 2 for medium password (16 characters)\n"
              "Type 3 for strong password (24 characters)\n"))

pass_gen(a)