def main():
#The main function

    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) #The function that starts the game is also here.

def intro():
#this functions introduces the rules of the gam Tic Tac Toe
    print("Hello! Welcome do DNCAZ's game of TIC TAC TOE!") 
    print("\n")
    print("Rules: \n"" Player_1 and Player2, represented by X or 0, take turns "
        "marking the spaces in a 3x3 grid.\n The player who succeds in placing  "
        "three of its markes in an horizontal, vertical or diagonal row wins.")
print("\n")
input("Press enter to continue.")
print("\n")

import time
time.sleep(2)

#Askin Players name

Player_1 = input("Player 1 - Who's Playing? (insert your name) ")
print("Player 1 name is:" + Player_1)
time.sleep(1)
Player_2 = input("Player 2 - Who's Playing? (insert your name) ")
print("Player 2 name is:" + Player_2)

time.sleep(2)

def create_grid():
#This functions create a blank playboard

    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def sym():
#this function decides the player's symbol

    symbol_1 = input(Player_1 + " do you want X or O? ")
    if symbol_1 == "X":
        symbol_2 = "0"
        print(Player_2 + " you are 0.")

    else:
        symbol_2 = "X"
        print(Player_2 + " you are X.")
        print("\n")
    input("Press enter to continue.")
    print("\n")

    return (symbol_1, symbol_2)

def startGamming(board, symbol_1, symbol_2, count):
#The function that starts the game.



#Decides the turn

    if count % 2 == 0:
        player = symbol_1
        print(Player_1 + ", it's your turn")
    elif count % 2 == 1:
        player = symbol_2
        print(Player_2 + ", it's your turn.")




    row = int(input("Pick a Row:"
                "[Upper row: enter 0, Middle row: enter 1, Bottom row: enter 2]"))

    column = int(input("Pick a column:"
                  "[Left column: enter 0, Middle colum: enter 1, Right column: enter 2]"))
    #Check if players' selection is out of range



    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                    "[enter 0, middle row: enter 1, bottom row: enter 2]:"))

        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    #Check if the square is already filled

    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
            filled = illegal(board, symbol_1, symbol_2, row, column)
            row = int(input("Pick a row:"
            "[Upper row: enter 0, Middle row: enter 1, Bottow Row: enter 2]"))
            column = int(input("Pick a column:"
                           "[Left column: enter 0, Middle column: enter 1, Right column: enter 2]"))

#Locates Player's symbol on the board

    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2

    return (board)

def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True


# This function checks if the board is full

    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)


        if count == 9:
            print("The Board is full. Game Over.")
            if winner == True:
                print("There is a tie.")

        #Check if there is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game Over.")

    #This function gives a report
    report(count, winner, symbol_1, symbol_2)

def outOfBoard(row, column):
#This function tells the player that their selection is out of range
    print("Out of board. Pick another one.")

def printPretty(board):
#This function prints on the board nice!

    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def isWinner(board, symbol_1, symbol_2, count):
#this function check if any player is winning
    winner = True
#check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print(Player_1  + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print (Player_2  + ", you won!")

#Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print(Player_1 + ", you won!")

        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print(Player_2 +  ", you won!")

#Check th Diagonals

    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print(Player_1 + "you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print(Player_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print(Player_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print(Player_2 + ", you won!")

    return winner


def illegal(board, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled. Pick another one.")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1):
        print("Winner :", Player_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner :", Player_2 + ".")
    else:
        print("There is a tie. ")


# Call Main
main()





