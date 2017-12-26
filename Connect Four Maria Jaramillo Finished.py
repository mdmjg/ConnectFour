##############Board
import os
row=6
col=7
numWins = 4
variables = ["X", "O", "@"]
numPlayers = 2

board=[]
for x in range(row):
    temp=[]
    for x in range(col):
        temp.append("*")
    board.append(temp)

def printboard():
    for y in range(row):
        for x in range(col):
           print(board[y][x],end=" ")
        print()

def check_horizontal_win(variable, row): #take the row as an argument because we are checking rows
    cols=0 
    isthereX = 0
    while cols < col: #While the loop is less than the total number of columns
        if board[int(row)][int(cols)] != variable: #If the position in the board is not the same as the variable
            isthereX = 0 #The counter goes back to zero
        else:
            isthereX +=1 #If the position is the same as the variable, the counter goes up by one
            if isthereX == numWins: #If the counter reaches 4, then the game stops.
                print("Horizonal win")
                return True
                cols = col
        cols+=1
    return False



def extract_column(column): #method to extract the column of a 2D array and make it into a list that could be used in the next method
    final_column = [row[int(column)] for row in board]
    return final_column 


def check_vertical_win(variable, column):
    extract_column(column)
    rows = 0
    isthereX = 0
    while rows < row:
        if board[int(rows)][int(column)] != variable:
            isthereX = 0
        else:
            isthereX +=1
            if isthereX == numWins:
                print("Vertical win")
                return True
                rows = row
        rows+=1
    return False
            


def check_diagonal_left(variable):
    count = 0
    for columns in range(col-numWins+1): #This will make sure we only check the first 4 colums, which are the only ones possible for making the conect 4
        for rows in range(row-numWins+1): #This will check only the first 3 rows which are the only ones that can make the connect 4
            count=0
            for i in range(numWins):
                if board[rows+i][columns+i] == variable: #If the element in that position is equal to the variable, then you add one to the counter.
                    count += 1
                    if count == numWins: #The counter has to reach 4
                        print("Diagonal left win")
                        return True

    return False

def check_diagonal_right(variable):
    count = 0
    for columns in range(col-1, col-numWins-1, -1): #I made the range begin at 6 so it would fit in the index, it finishes at 2 so that it includes 3
        for rows in range(row-numWins+1):
            count = 0
            for i in range(numWins):                    
                    if board[rows+i][columns-i] == variable: #If the element in that position is equal to the variable, then you add one to the counter.
                        count += 1
                        if count == numWins: #The counter has to reach 4
                            print("Diagonal right win")
                            return True

    return False

def check_if_draw():
    count = 0
    for c in range(col):
        if board[0][c] == "*":
            return False
    return True

def play_again():
    play_again = input("Press Y to play again or any other key to stop")
    if play_again == "Y":
        print("I'm here")
        board=[]
        for x in range(row):
            temp=[]
            for x in range(col):
                temp.append("*")
            board.append(temp)
    else:
        win = True



############

win = False
turn = 0
printboard()
while win == False:
    os.system("cls")
    variable = variables[turn]
    user_column = input(variable + " Enter your column")
    try:
        user_column = int(user_column)
        if(user_column < 0 or user_column >= col):
            user_column = int(input("Invalid column. Choose another column"))
        for r in range(row-1, -1, -1): # start from the bottom most row and go up by one
            while board[r][user_column] != "*": #While the specific place is not empty
                r -= 1                          #Change the value of r in order to try the line above
                if(user_column >= col or user_column < 0 or r > row or r < 0): #Make sure the column is within range and make sure the column hasn't been filled yet
                    user_column = int(input("Invalid column. Choose another column"))
            if(board[r][user_column] == "*" and r < row and user_column < col): #Replace the board section ONLY if it has an asterisk in it, the program wont work otherwise, trust me
                board[r][user_column] = variable
                turn = (turn+1) % numPlayers
                final_row = r 
            break
        printboard()
        if(check_horizontal_win(variable, final_row) or check_vertical_win(variable, user_column) or check_diagonal_left(variable) or check_diagonal_right(variable)):
            print(variable, "You've won")
            temp = True #This temporary variable will be used to ask the user if they want to play again later.

        if(check_if_draw() == True):
            print("There's a draw")
            temp = True
            
        if temp == True: #If there was a draw or a win, the game wil ask the user if they want to play again or not
            play_again = input("Press Y to play again or any other key to stop").lower()
            if play_again == "y":
                board=[]
                for x in range(row):
                    temp=[]
                    for x in range(col):
                        temp.append("*")
                    board.append(temp)
                printboard()
                turn = 0
            else:
                win = True
            
    except:
        print("Invalid input")

            
                


    
    
