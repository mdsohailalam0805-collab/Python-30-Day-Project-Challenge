
board =[" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

# print(board[0], "|", board[1], "|", board[2])
# print("----------")

# print(board[3], "|", board[4], "|", board[5])
# print("----------")

# print(board[6], "|", board[7], "|", board[8])


player = "X"

for turn in range (9):
    
    position = int(input(f"Player {player}, Enter position (1-9):"))
    
    board [position-1] = player
    
    
    # Updated board dikhana
    print(board[0], "|", board[1], "|", board[2])
    print("----------")

    print(board[3], "|", board[4], "|", board[5])
    print("----------")

    print(board[6], "|", board[7], "|", board[8])

    
    if player == "X":
        player = "O"
        
    else:
        player = "X"

