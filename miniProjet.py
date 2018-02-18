game_grid = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]


def display(grid):
    for i in range(0, 3):
        for j in range(0, 3):
            print(grid[i][j] + " ", end="")
        print("")


def play(grid, x, y, xo):
    if grid[x][y] == "_":
        grid[x][y] = xo
        return True
    else:
        return False


def check_game(grid):
    for x in range(0, 3):
        if grid[x][0] != "_" and grid[x][0] == grid[x][1] and grid[x][0] == grid[x][2]:
            return grid[x][0]
        if grid[0][x] != "_" and grid[0][x] == grid[1][x] and grid[0][x] == grid[2][x]:
            return grid[0][x]
    if grid[0][0] != "_" and grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
        return grid[0][0]
    if grid[0][2] != "_" and grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
        return grid[0][2]
    return "_"


def react_and_play(grid):
    tabCar=['X','O']
    for car in tabCar:
        #1ère iteration : attaque, 2ème iteration: defense
        for x in range(0, 3):
            if grid[x][0] == car and grid[x][0] == grid[x][1] and grid[x][2] == "_":
                step_done = play(game_grid, x, 2, 'X')
                return (x, 2)
            if grid[x][1] == car and grid[x][1] == grid[x][2] and grid[x][0] == "_":
                step_done = play(game_grid, x, 0, 'X')
                return (x, 0)
            if grid[x][0] == car and grid[x][0] == grid[x][2] and grid[x][1] == "_":
                step_done = play(game_grid, x, 1, 'X')
                return (x, 1)

            if grid[0][x] == car and grid[0][x] == grid[1][x] and grid[2][x] == "_":
                step_done = play(game_grid, 2, x, 'X')
                return (2, x)
            if grid[1][x] == car and grid[1][x] == grid[2][x] and grid[0][x] == "_":
                step_done = play(game_grid, 0, x, 'X')
                return (0, x)

            if grid[0][x] == car and grid[0][x] == grid[2][x] and grid[1][x] == "_":
                step_done = play(game_grid, 1, x, 'X')
                return (1, x)

        #en diagonale
        if grid[0][0] == car and grid[0][0] == grid[1][1] and  grid[2][2]== "_" :
            step_done = play(game_grid, 2, 2, 'X')
            return (2, 2)

        if grid[1][1] == car and grid[2][2] == grid[1][1] and  grid[0][0]== "_" :
            step_d1one = play(game_grid, 0, 0, 'X')
            return (0, 0)

        if grid[0][0] == car and grid[0][0] == grid[2][2] and  grid[1][1]== "_" :
            step_done = play(game_grid, 1, 1, 'X')
            return (1, 1)

        if grid[0][2] == car and grid[0][2] == grid[1][1] and  grid[2][0]== "_" :
            step_done = play(game_grid, 2, 0, 'X')
            return (2, 0)

        if grid[1][1] == car and grid[2][0] == grid[1][1] and  grid[0][2]== "_" :
            step_d1one = play(game_grid, 0, 2, 'X')
            return (0, 2)

        if grid[0][2] == car and grid[0][2] == grid[2][0] and  grid[1][1]== "_" :
            step_done = play(game_grid, 1, 1, 'X')
            return (1, 1)

    if grid[0][0] == "X" and grid[0][0] == grid[1][1] and  grid[1][0]== "_" :
        step_done = play(game_grid, 1, 0, 'X')
        return (1, 0)

    if grid[0][0] == "X" and grid[0][0] == grid[1][1] and  grid[0][1]== "_" :
        step_done = play(game_grid, 0, 1, 'X')
        return (0, 1)

    if grid[0][2] == "X" and grid[0][2] == grid[1][1] and  grid[1][2]== "_" :
        step_done = play(game_grid, 1, 2, 'X')
        return (1, 2)

    if grid[0][2] == "X" and grid[0][2] == grid[1][1] and  grid[0][1]== "_" :
        step_done = play(game_grid, 0, 1, 'X')
        return (0, 1)

    if grid[2][2] == "X" and grid[2][2] == grid[1][1] and  grid[1][2]== "_" :
        step_done = play(game_grid, 1, 2, 'X')
        return (1, 2)
    if grid[2][2] == "X" and grid[2][2] == grid[1][1] and  grid[2][1]== "_" :
        step_done = play(game_grid, 2, 1, 'X')
        return (2, 1)


    x=1
    y=1
    if grid[x][y] == '_':
        print("ddd")
        play(game_grid, x,y, 'X')
        return (x,y)
    x=0
    y=0
    if grid[x][y] == '_':
        play(game_grid, x,y, 'X')
        return (x,y)
    x=0
    y=2
    if grid[x][y] == '_':
        play(game_grid, x,y, 'X')
        return (x,y)
    x=2
    y=0
    if grid[x][y] == '_':
        play(game_grid, x,y, 'X')
        return (x,y)
    x=2
    y=2
    if grid[x][y] == '_':
        play(game_grid, x,y, 'X')
        return (x,y)


    for i in range(0, 3):
        for j in range(0, 3):

            if play(game_grid, i, j, 'X'):
                print("iiii")
                return i,j

    return (-1,-1)

import fileinput

i = 0  # 0: read X, 1: read Y
for line in fileinput.input():
    if i == 0 and int(line) in range(0, 3):
        x = int(line)
        i = i + 1
    elif int(line) in range(0, 3):
        y = int(line)
        i = 0
        print("Player played", x, y)
        step_done = play(game_grid, x, y, 'O')
        if step_done:
            display(game_grid)
            print()

            if check_game(game_grid) == 'O':
                print("You win")
                exit(0)
            else:
                # computer turn
                x, y = react_and_play(game_grid)
                if x==-1 and y==-1:
                    print("Game over")
                    exit(0)
                print("Computer played", x, y)
                display(game_grid)
                if check_game(game_grid) == 'X':
                    print("Computer win")
                    exit(0)

        else:
            print("Choose an empty cell")
        print()
        print("_____________")
        print()
    else:
        print("enter a number between 0 and 2!")
