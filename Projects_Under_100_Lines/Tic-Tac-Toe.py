
board =[" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

# print(board[0], "|", board[1], "|", board[2])
# print("----------")

# print(board[3], "|", board[4], "|", board[5])
# print("----------")

# print(board[6], "|", board[7], "|", board[8])


player = "X"
winner = False

for turn in range (9):
    
    position = int(input(f"Player {player}, Enter position (1-9):"))
    
    board [position-1] = player
    
    
    # Updated board dikhana
    print(board[0], "|", board[1], "|", board[2])
    print("----------")

    print(board[3], "|", board[4], "|", board[5])
    print("----------")

    print(board[6], "|", board[7], "|", board[8])


    # Winning condition
    
    if (board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " " or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "):
        
        winner = True
        print(f"\n Player {player} Wins!")
        break
    
    # player switch
    
    if player == "X":
        player = "O"
        
    else:
        player = "X"

if not winner:
    print("\n Game Draw!")