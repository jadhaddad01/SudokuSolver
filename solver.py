## Author: Jad Haddad

import puzzleAPI
import time

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
# Main variables
easy = 4
medium = 5
hard = 6

# printPuzzle prints a 2D array puzzle in a neat format


def printPuzzle(puz):
    for i in range(len(puz)):
        # seperating boxes horizontally
        if(i % 3 == 0 and i != 0):
            print((len(puz[i]) * 2 + 3) * "-")

        for j in range(len(puz[i])):
            # seperating boxes vertically
            if((j % 3 == 0) and j != 0):
                print("| " + str(puz[i][j]), end=" ")

            elif(j != (len(puz[i]) - 1)):
                print(puz[i][j], end=" ")

            # last number in row
            else:
                print(puz[i][j])

# Find next empty block


def emptyBlock(puz):
    for i in range(len(puz)):
        # return first empty block we find
        for j in range(len(puz[i])):
            if(puz[i][j] == 0):
                return (i, j)

    # no blocks are empty
    return None

# Check if number in certain index is valid as to respect the rules of sudoku
# No same num in same row Or column Or box


def numValid(puz, num, index):
    # Check row for duplicate
    for i in range(len(puz[0])):
        if(puz[index[0]][i] == num and index[1] != i):
            return False

    # Check column for duplicate
    for j in range(len(puz)):
        if(puz[j][index[1]] == num and index[0] != j):
            return False

    # Check box for duplicate
    for k in range((index[0] // 3) * 3, (index[1] // 3) * 3 + 3):
        for l in range((index[1] // 3) * 3, (index[0] // 3) * 3 + 3):
            if(puz[k][l] == num and (k, l) != index):
                return False

    # Number is valid
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
            puz[row][column] = num
            # recursive call to solve this block
            if(solvePuzzle(puz)):
                return True
            # we reset the block to 0 if no num worked
            puz[row][column] = 0

    # if this block finished counting to 9 and nothing is valid
    # we reset to 0 and the previous block continues to 9
    return False

(puzzle, solvedPuzzle) = puzzleAPI.getPuzzle(hard)
print("\nAPI Generated Puzzle:")
printPuzzle(puzzle)
print("\nAPI Solved Puzzle:")
printPuzzle(solvedPuzzle)
print("\nAlgorithmicaly Solved Puzzle:")
# start time
start_time = time.time()
solvePuzzle(puzzle)
print("--- solved in %s seconds ---" % (time.time() - start_time))
printPuzzle(puzzle)

(puzzle1, solvedPuzzle1) = puzzleAPI.getPuzzle(hard)
print("\nAPI Generated Puzzle:")
printPuzzle(puzzle1)
print("\nAPI Solved Puzzle:")
printPuzzle(solvedPuzzle1)
print("\nAlgorithmicaly Solved Puzzle:")
# start time
start_time1 = time.time()
solvePuzzle(puzzle1)
print("--- solved in %s seconds ---" % (time.time() - start_time1))
printPuzzle(puzzle1)
