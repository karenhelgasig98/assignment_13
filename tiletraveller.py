# A computer game where a player is located in a certain tile in a grid
# the player chooses directions and the program tells him/her if the direction
# is valid or not
# the goal is to reach the victory location [3,1].

# define the beginning tile [1,1]
# Create a function for each direction
# Ask player for direction
# go to the function for the direction chosen
# the functions check the tile where the player is located
# and returns the new location
# if the direction chosen is a closed wall the function prints 
# out 'invalid direction'
# repeated until the player reaches the victory tile [3,3]
# game ends when player reaches victory tile

# constants
NORTH = 'n'
SOUTH = 's'
EAST = 'e'
WEST = 'w'

def pull_lever(coins):

    pull = input('Pull a lever (y/n): ').lower()
    if pull == 'y':
        coins += 1
        print('You received 1 coin, your total is now {}.'.format(coins))
        return coins
    else:
        return coins


def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''

    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions == NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 1:  # (3,1)
        valid_directions = NORTH
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST
    return valid_directions


def print_directions(directions_str):

    print("You can travel: ", end='')
    # if we only have to run once through there is
    # only one direction otherwise we print 'or'
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")



def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == WEST:
        col -= 1
    elif direction == EAST:
        col += 1

    return col, row


def is_victory(col, row):
    '''returns True if victory otherwise False'''
    return col == 3 and row == 1  # (3,1)


def play_one_move(col, row, valid_directions, coins):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''

    victory = False
    direction = input('Direction: ').lower()

    if direction in valid_directions:
        col, row = move(direction, col, row)
        if col == 1 and row == 2:# (1,2)
            coins = pull_lever(coins)
        elif col == 2 and row == 2: # (2,2)
            coins = pull_lever(coins)
        elif col == 2 and row == 3:
            coins = pull_lever(coins) # (2,3)
        elif col == 3 and row == 2:
            coins = pull_lever(coins) # (3,2)

        victory = is_victory(col, row)
    else:
        print('Not a valid direction!')

    return victory, col, row, coins


def play():
    # main program starts here
    victory = False
    # start at tile (1,1)
    row = 1
    col = 1
    # begin with 0 coins
    coins = 0

    while victory == False:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, coins = play_one_move(col, row, valid_directions, coins)

    print('Victory! Total coins {}.'.format(coins))

play_again = True
while play_again:
    play()

    play_again = input("Play again (y/n): ").lower()
    if play_again != 'y':
        play_again = False



