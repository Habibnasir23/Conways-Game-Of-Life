# The Game of Life (an example of a cellular automaton) is played on an infinite two-dimensional
# rectangular grid of cells. Each cell can be either alive or dead. The status of each cell changes
# each turn of the game depending on the statuses of that cell's 8 neighbors.
# A cell's status is determined by the following rules:
# If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
# If the cell is dead, then it springs to life only in the case that it has 3 live neighbors

import random, time, copy

# creates an empty board of length and width. Initializes the board with either "#" or " "
# changes the status of the cells depending on the rules.
def random_state(len, wid):
    board = []

    # initializing the board
    for x in range(wid):
        col = []
        for y in range(len):
            num = random.randint(0, 1)
            if num == 0:
                col.append("#")
            else:
                col.append(" ")

        board.append(col)

    while True:
        # copying the board and printing it
        print("\n\n\n\n\n")
        copy_state = copy.deepcopy(board)
        for l in range(len):
            for w in range(wid):
                print(copy_state[w][l], end="")
            print()

        for x in range(wid):
            for y in range(len):

                # setting up the coordinates.
                left = (x - 1) % wid
                right = (x + 1) % wid
                top = (y - 1) % len
                bottom = (y + 1) % len

                # checking if the 8 neighbors are alive
                aliveneighbors = 0
                if copy_state[left][top] == "#":
                    aliveneighbors += 1
                if copy_state[right][top] == "#":
                    aliveneighbors += 1
                if copy_state[left][bottom] == "#":
                    aliveneighbors += 1
                if copy_state[right][bottom] == "#":
                    aliveneighbors += 1
                if copy_state[left][y] == "#":
                    aliveneighbors += 1
                if copy_state[right][y] == "#":
                    aliveneighbors += 1
                if copy_state[x][top] == "#":
                    aliveneighbors += 1
                if copy_state[x][bottom] == "#":
                    aliveneighbors += 1

                # changing the status of the cells
                if copy_state[x][y] == "#" and (
                    aliveneighbors == 2 or aliveneighbors == 3
                ):
                    board[x][y] = "#"
                elif aliveneighbors == 3 and copy_state[x][y] == " ":
                    board[x][y] = "#"
                else:
                    board[x][y] = " "
        time.sleep(1)
    return copy_state


temp = random_state(20, 20)
