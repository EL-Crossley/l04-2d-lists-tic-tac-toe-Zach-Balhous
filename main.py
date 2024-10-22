# Put your function here
def ticTacToe(board):
    #Three vartical X's
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == "X":
        return("X")
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == "X":
        return("X")
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == "X":
        return("X")
    
    #Three horizontal X's
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == "X":
        return("X")
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == "X":
        return("X")
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == "X":
        return("X")
    
    #Three Diaganol X's
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "X":
        return("X")
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == "X":
        return("X")
    
    
    
    #Three vartical O's
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == "O":
        return("O")
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == "O":
        return("O")
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == "O":
        return("O")
    
    #Three horizontal O's
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == "O":
        return("O")
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == "O":
        return("O")
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == "O":
        return("O")
    
    #Three Diaganol O's
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "O":
        return("O")
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == "O":
        return("O")
    
    else:
        return("tie")
    
    
# testing
board = [['X','O','O'],['O','X','O'],['X','O','X']]
print(ticTacToe(board))