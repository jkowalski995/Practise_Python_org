import functions

print("Hello Players! It's a rock paper scissors game!")
p_1, p_2 = 0, 0
while True:
    play = input("Do You want to play? Type (Y)es or (N)o")
    if play == "Y" or play == "y":
        p_1_t, p_2_t = functions.game()
        p_1 += p_1_t
        p_2 += p_2_t
    else:
        break
print("The result of a game is:")
print("Player One ", p_1, ":", p_2, " Player Two")
if p_1 > p_2:
    print("Player One wins!")
elif p_2 > p_1:
    print("Player Two wins!")
else:
    print("It's a tie!")
