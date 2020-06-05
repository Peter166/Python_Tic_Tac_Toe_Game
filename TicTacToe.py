
print("Welcome to tic Tac Toe")

player1 = {'name':"", 'marker':"X"}
player2 = {'name':"", 'marker':"O"}

player1['name'] = input('Player1 name: ')
print(' ')
print("{} your marker is : X ".format(player1["name"]))
print(' ')
print(' ')
player2['name'] = input('Player2 name: ')
print(' ')
print("{} your marker is : 0 ".format(player2["name"]))
print(' ')
print(' ')
print(' ')


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display(board):

    print(' ')
    print(' ')
    print(" "+ board[7]+'|'+board[8]+"|"+board[9])
    print('-------')
    print(" "+ board[4]+"|"+board[5]+"|"+board[6])
    print('-------')
    print(" "+ board[1]+"|"+board[2]+"|"+board[3])
    print(' ')
    print(' ')

#
def positionchoice(board,currentPlayer):

    choice = "wrong"

    while choice not in ['$','1','2','3','4','5','6','7','8','9'] or board[int(choice)] == 'X' or board[int(choice)] == 'O' :
        choice = input("pick a number from 1 to 9: ")

        if choice not in ['1','2','3','4','5','6','7','8','9'] or board[int(choice)] == 'X' or board[int(choice)] == 'O':
            print(' ')
            print("Sorry wrog input.")
            print(' ')
        else:

            board[int(choice)] = currentPlayer['marker']
            print(choice)
            return choice



def win():

    if board[1] == board[2] == board[3] and board[3] =='X' or board[3]=='0' or board[4] == board[5] == board[6] and board[6] =='X' or board[6]=='0' or board[7] == board[8] == board[9] and board[9] =='X' or board[9]=='0' or board[7] == board[4] == board[1] and board[1] =='X' or board[1]=='0' or board[8] == board[5] == board[2] and board[2] =='X' or board[2]=='0' or board[9] == board[6] == board[3] and board[3] =='X' or board[3]=='0' or board[7] == board[5] == board[3] and board[3] =='X' or board[3]=='0' or board[1] == board[5] == board[9] and board[9] =='X' or board[9]=='0':



        return True



counter = 0
currentPlayer = player2


while(counter < 9):
    display(board)


    if currentPlayer == player2:
        currentPlayer = player1
    else:
        currentPlayer == player1
        currentPlayer = player2


    print(currentPlayer["name"])
    positionchoice(board,currentPlayer)
    winCheck = win()

    if winCheck:

        counter =10
        display(board)
        print('{}  WON this game!'.format(currentPlayer['name']))

    counter +=1


if counter == 9:
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    display(board)
    print("It's a draw!")
    print(' ')
    print(' ')
