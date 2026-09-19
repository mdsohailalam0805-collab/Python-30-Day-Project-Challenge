
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

while True:
    
    position = int(input(f"Player {player}, Enter position (1-9):"))
    
    if position < 1 or position > 9:
        print("Invalid Position! Enter Between 1 and 9.")
        continue
    
    if board[position-1] == " ":
        board [position-1] = player
    
    else:
        print("Position Allready Occupied!")
        continue
    
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
        print(f"\n Player {player} Winner!")
        break
    
    
    # Draw condition

    if " " not in board:
        print("\n Game Draw!")
        break

    # player switch
    if player == "X":
        player = "O"
        
    else:
        player = "X"

