#To remove random items from finished puzzle
from random import sample

## Start of sudoku api request
import http.client
import ast

conn = http.client.HTTPSConnection("online-sudoku.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "online-sudoku.p.rapidapi.com",
    'x-rapidapi-key': "4423dd6a18msh77e7bbdfc9584b4p153abdjsn96f9b7cc4dd5"
}

conn.request("GET", "/random", headers=headers)

res = conn.getresponse()
data = res.read()

#dictionary parsed from string
puzzleApi = ast.literal_eval((data.decode("utf-8")))
#get item from json
puzzleNums = puzzleApi.get("item")
## End of sudoku api request

# creating 1D matrix from puzzleNums
matrix = [puzzleNums[i*9: (i+1)*9] for i in range(9)]

#Removing 4 items in each row as api gives us solved puzzle
puzzle = []
#solvedPuzzle USED FOR TESTING SOLVING ALGORITHM
solvedPuzzle = []
#loop through each row
for row in matrix:

    #add row to tmp1 list
    tmp1 = list(row)
    #switch everything to int as they are in string
    tmp1 = [int(i) for i in tmp1]
    #add the row to the puzzle
    solvedPuzzle.append(tmp1)

    #change 4 random numbers to 0 in each row
    for i in sample(range(9), 4): #TO MAKE GAME HARDER CHANGE 4 TO 5, 6, 7 etc
        row = f"{row[:i]}0{row[i+1:]}"
    #add row to a new list
    tmp = list(row)
    #switch everything to int as they are in string
    tmp = [int(i) for i in tmp]
    #add the row to the puzzle
    puzzle.append(tmp)

#var puzzle is the final 2D matrix TO BE SOLVED
#var solvedPuzzle is the final 2D matrix ALREADY SOLVED