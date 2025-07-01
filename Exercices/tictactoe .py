from random import randrange

computer = "X"
user = "0"

def display_board(board):
    def display_sep():
        print("+", end ="")
        print("-------+"*3)
    
    def display_empty():
        print("|", end ="")
        print("       |"*3)

    def display_number(line):
        print("|   ", end ="")
        if line == 2:
            print(board[0][0], end ="")
            print("   |   ", end ="")
            print(board[0][1], end ="")
            print("   |   ", end ="")
            print(board[0][2], end ="")
            print("   |")
        elif line == 6:
            print(board[1][0], end ="")
            print("   |   ", end ="")
            print(board[1][1], end ="")
            print("   |   ", end ="")
            print(board[1][2], end ="")
            print("   |")
        else:
            print(board[2][0], end ="")
            print("   |   ", end ="")
            print(board[2][1], end ="")
            print("   |   ", end ="")
            print(board[2][2], end ="")
            print("   |")

    for line in range(13):
        if line%4==0:
            display_sep()
        elif line == 2 or line == 6 or line == 10:
            display_number(line)
        else:
            display_empty()


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move = int(input("What's your next Move? ")) - 1
    try:
        if(move > 0 and move < 10):
            board[int(move/3)][move%3] = user
    except ValueError:
        print("Invalid entry")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    result = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] != user and board[i][j] != computer ):
                result.append(tuple((i,j)))
    return result
                

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if((board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or
        (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or
        (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or
        (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or
        (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or
        (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or
        (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign) or
        (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign)):
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_field = make_list_of_free_fields(board)
    move = randrange(len(free_field))-1
    position = free_field[move]
    board[position[0]][position[1]] = computer


board_game = [[1,2,3],[4,5,6],[7,8,9]]
board_game[1][1] = computer
victory = False
while not victory:
    if len(make_list_of_free_fields(board_game)) == 0:
        print("Nobody wins!")
        break
    display_board(board_game)
    enter_move(board_game)
    if victory_for(board_game, user):
        victory = True
        print("Player wins!")
    else:
        draw_move(board_game)
        if victory_for(board_game, computer):
            victory = True
            print("Computer wins!")
display_board(board_game)
