# import puzzle from puzzleAPI
import puzzleAPI

"""
#manually entered puzzle
puzzle = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
"""
# puzzle taken from puzzleAPI file
puzzle = puzzleAPI.puzzle

# solvedPuzzle FOR TESTING taken from puzzleAPI file
solvedPuzzle = puzzleAPI.solvedPuzzle

# printPuzzle prints a 2D array puzzle in a neat format


def printPuzzle(puz):
    # we loop through each column
    for i in range(len(puz)):
        # seperating boxes horizontally
        if(i % 3 == 0 and i != 0):
            # accouting for vertical seperation + 3
            print((len(puz[i]) * 2 + 3) * "-")
        # then through each number in that column
        for j in range(len(puz[i])):
            # seperating boxes vertically
            if((j % 3 == 0) and j != 0):
                print("| " + str(puz[i][j]), end=" ")
            # printing numbers between vertical seperation
            elif(j != (len(puz[i]) - 1)):
                print(puz[i][j], end=" ")
            # last number in a row to print a new line
            else:
                print(puz[i][j])

# Solve puzzle


def solve(puz):
    # Base Case finding the next empty block, and if no empty block is found we return true
    nextEmpty = emptyBlock(puz)
    if nextEmpty == None:
        # puzzle loved
        return True
    else:
        # we start with the next empty block
        row, column = nextEmpty
    # try nums 1 to 9 and place first valid num
    for num in range(1, 10):
        # Add numb in block if valid
        if(numValid(puz, num, (row, column))):
            puzzle[row][column] = num
            # recursive call to solve this block
            if(solve(puz)):
                return True
            # we reset the block to 0 if no num worked
            puz[row][column] = 0

    # if this block finished counting to 9 and nothing is valid
    # we reset to 0 and the previous block continues to 9
    return False


printPuzzle(puzzle)
print()
printPuzzle(solvedPuzzle)
