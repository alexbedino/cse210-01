'''
Brother Alex Bedino
CSE 210 | Programming With Classes
Project 01  Tic-Tac-Toe 

'''


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"] #defining the board first to be used by our function

currentPlayer = "X"
winner = None 
gameRunning = True

# print game board
def printBoard(board): 
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-"*5)
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-"*5)
    print(board[6] + "|" + board[7] + "|" + board[8])

# player input
def playerInput(board):
    global currentPlayer
    inp = int(input(currentPlayer + " Enter a square number(1-9): "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": #making sure the user types in a correct number in an empty slot
        board[inp-1] = currentPlayer
    else:
        print("That spot is already taken!")


def checkHor(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True #Boolean used to use the function with conditional statements to exit the game for instance
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[7]
        return True
    
def checkVert(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[4]
        return True 
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# change player
def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O" #using re-assign statement to change player
    elif currentPlayer == "O":
        currentPlayer = "X"


# check winner or tie again

def checkTie():
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False #stopping game from running

def checkWinner():
    global gameRunning
    global winner
    if checkHor(board) or checkVert(board) or checkDiag(board):
        if winner == "X":
            winner = "Player 1"
        elif winner == "O":
            winner = "Player 2"
        printBoard(board)
        print("The winner is " + winner + " Thanks for playing")
        gameRunning = False #stopping game from running


def main():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        changePlayer()
        checkWinner()
        checkTie()

print (f"Tic Tac Toe, choose a side, Player 1 (X) starts first, Player 2 (O) follows!")
main()