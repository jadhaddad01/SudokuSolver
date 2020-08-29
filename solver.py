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

#printPuzzle prints a 2D array puzzle in a neat format
def printPuzzle(puz):
    #we loop through each column
    for i in range(len(puz)):
        #seperating boxes horizontally
        if(i % 3 == 0 and i != 0):
            print((len(puz[i]) * 2 + 3)* "-") #accouting for vertical seperation + 3
        #then through each number in that column
        for j in range(len(puz[i])):
            #seperating boxes vertically
            if((j % 3 == 0) and j != 0):
                print("| " + str(puz[i][j]),end=" ")
            #printing numbers between vertical seperation
            elif(j != (len(puz[i]) - 1)):
                print(puz[i][j],end=" ")
            #last number in a row to print a new line
            else:
                print(puz[i][j])

        


printPuzzle(puzzle)
