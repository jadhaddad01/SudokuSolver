# Author: Jad Haddad

# To remove random items from finished puzzle
from random import sample

# Start of sudoku api request
import http.client
import ast

conn = http.client.HTTPSConnection("online-sudoku.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "online-sudoku.p.rapidapi.com",
    'x-rapidapi-key': "ENTERYOUROWNKEY"
}

conn.request("GET", "/random", headers=headers)

res = conn.getresponse()
data = res.read()

# dictionary parsed from string then item taken
puzzleApi = ast.literal_eval((data.decode("utf-8")))
puzzleNums = puzzleApi.get("item")
# End of sudoku api request

# creating 1D matrix from puzzleNums
matrix = [puzzleNums[i*9: (i+1)*9] for i in range(9)]

def getPuzzle(difficulty):
    puzzle = []
    solvedPuzzle = []
    # loop through each row
    for row in matrix:

        # add row to tmp1 list
        tmp1 = list(row)
        # switch everything to int as they are in string
        tmp1 = [int(i) for i in tmp1]
        solvedPuzzle.append(tmp1)

        # change 4 random numbers to 0 in each row
        for i in sample(range(9), difficulty):  # TO MAKE GAME HARDER CHANGE 4 TO 5, 6, 7 etc
            row = f"{row[:i]}0{row[i+1:]}"

        tmp = list(row)
        tmp = [int(i) for i in tmp]
        puzzle.append(tmp)
    
    return (puzzle, solvedPuzzle)
