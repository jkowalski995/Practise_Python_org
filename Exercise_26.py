game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

# To do: if working put thi into function
# also move print out of the loop to avoid printing 3x the result

for i in range(3):
    if game[i][0] == game[i][1] == game[i][2] == 1:
        print("Player 1 wins!")
    elif game[i][0] == game[i][1] == game[i][2] == 2:
        print("Player 2 wins!")
    else:
        if game[0][i] == game[1][i] == game[2][i] == 1:
            print("Player 1 wins!")
        elif game[0][i] == game[1][i] == game[2][i] == 2:
            print("Player 2 wins!")
        else:
            if game[0][0] == game[1][1] == game[2][2] == 1:
                print("Player 1 wins!")
            elif game[0][0] == game[1][1] == game[2][2] == 2:
                print("Player 2 wins!")
            else:
                if game[0][2] == game[1][1] == game[2][0] == 1:
                    print("Player 1 wins!")
                elif game[0][2] == game[1][1] == game[2][0] == 2:
                    print("Player 2 wins!")
                else:
                    print("It's a tie!")