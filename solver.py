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

# Find next empty block


def emptyBlock(puz):
    # loop through rows
    for i in range(len(puz)):
        # loop through numbers
        for j in range(len(puz[i])):
            # first empty block we find we directly return the position
            if(puz[i][j] == 0):
                return (i, j)
    # if we couldn't find a value we solved the puzzle
    return None

# Check if number in certain index is valid as to respect the rules of sudoku
# No same num in same row Or column Or box


def numValid(puz, num, index):
    # Check Row
    for i in range(len(puz[0])):
        # if any num in the row EXCEPT the num we are checking to be valid = to that num
        if(puz[index[0]][i] == num and index[1] != i):
            # we would return false
            return False
    # Check Column
    for j in range(len(puz)):
        # we any num in the column EXCEPT the num we are checking to be valid = to that num
        if(puz[i][index[1]] == num and index[0] != i):
            # we would return false
            return False

    # CHECK BOX MAKE IT
    for k in range((index[0] // 3) * 3, (index[1] // 3) * 3 + 3):
        for l in range((index[1] // 3) * 3, (index[0] // 3) * 3 + 3):
            #if any num in the box EXCEPT the num we are checking to be valid = to that num
            if(puz[k][l] == num and (k, l) != index):
                # we would return false
                return False
    
    #If false not returned the number we are placing is valid
    return True

# Solve puzzle


def solvePuzzle(puz):
    # Base Case finding the next empty block, and if no empty block is found we return true
    nextEmpty = emptyBlock(puz)
    if not nextEmpty:
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
            if(solvePuzzle(puz)):
                return True
            # we reset the block to 0 if no num worked
            puz[row][column] = 0

    # if this block finished counting to 9 and nothing is valid
    # we reset to 0 and the previous block continues to 9
    return False

print("\nAPI Generated Puzzle:")
printPuzzle(puzzle)
print("\nAPI Solved Puzzle:")
printPuzzle(solvedPuzzle)
print("\nAlgorithmicly Solved Puzzle:")
solvePuzzle(puzzle)
printPuzzle(puzzle)