import random
import os

# draw grid

# get random location

# get random location of exit door

# get random location of monster

# draw input in the Garfield

# move player, untill invalid move ex past edges of grid

#check win/loss

#clear screen and redraw grid

CELLS = [
(0,0),(1,0),(2,0),(3,0),(4,0),
(0,1),(1,1),(2,1),(3,1),(4,1),
(0,2),(1,2),(2,2),(3,2),(4,2),
(0,3),(1,3),(2,3),(3,3),(4,3),
(0,4),(1,4),(2,4),(3,4),(4,4),
]

def get_location():
    monster = random.sample(range(4), k=2)
    door = random.sample(range(4), k=2)
    player  = random.sample(range(4), k=2)

    while monster == door or player == door or player == monster:
        monster = random.sample(range(4), k=2)
        door = random.sample(range(4), k=2)
        player  = random.sample(range(4), k=2)

    return monster, door, player

def clear_scr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def move_player(player, move):
    if move == 'LEFT':
        return (player[0]-1,player[1])
    if move == 'RIGHT':
        return (player[0]+1,player[1])
    if move == 'UP':
        return (player[0],player[1]-1)
    if move == 'DOWN':
        return (player[0],player[1]+1)
    return False


def get_moves(player):
    moves = ["LEFT","RIGHT","UP","DOWN"]

    if player[0] == 0:
        if player[1] == 0:
            return ["RIGHT","DOWN"]
        if player[1] == 4:
            return ["RIGHT","UP"]
        return ["RIGHT","UP","DOWN"]

    if player[0] == 4:
        if player[1] == 0:
            return ["LEFT","DOWN"]
        if player[1] == 4:
            return ["LEFT","UP"]
        return ["LEFT","UP","DOWN"]

    if player[1] == 0:
        return ["LEFT","RIGHT","DOWN"]

    if player[1] == 0:
        if player[0] == 4:
            return ["RIGHT","DOWNq"]
        return ["LEFT","RIGHT","UP"]

    return moves

while True:
    clear_scr()
    try:
        move
    except:
        move = ''

    if move:
        player = move_player(player, move)
    else:
        data = get_location()
        player = tuple(data[2])
        monster = tuple(data[0])
        door = tuple(data[1])

    if player == monster:
        print('YOU LOSE! MONSTER EAT YOU ALIVE!!')
        break

    if player == door:
        print('YOU WON! YOU ESCAPE FROM DUNGEON. CONGRATULATIONS!!')
        break

    user_can_move = get_moves(player)

    print('\n---Welcome to the Dungeon !---\n\nTry to escape from dungeon before monster eat you! Good luck!')
    print('You are currently in room nr {}\n'.format(player))
    print('You can move {}\n'.format(user_can_move))
    print('\nEnter q to quit\n')

    move = str(input('> '))
    move = move.upper()

    if move == 'Q':
        break

    if move in user_can_move:
        continue
    else:
        print('Cant move these direction')
        move = str(input('> '))
        move = move.upper()
        if not move in user_can_move:
            print('Again You Cant move these direction! Over!')
            break
