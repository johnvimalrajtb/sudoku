'''Algorithm to solve 9* 9  Suduko 
 @author: John Vimalraj
 Subject: CSC550 
 Date 1/09/2021
'''
def printCredits(cre):
	print(cre)
#constants
N = 9 #No of Row
M = 9 #No of Column
COLUMN_GRID = 3 # no of column grid
ROW_GRID = 3 # no of row grid 

input1 = [
    [9, 0, 0, 1, 7, 0, 4, 0, 2],
    [1, 6, 0, 0, 4, 0, 0, 9, 5],
    [0, 0, 8, 0, 0, 3, 0, 0, 0],
    [0, 1, 0, 9, 0, 0, 5, 7, 3],
    [0, 4, 0, 0, 0, 0, 0, 2, 0],
    [5, 8, 9, 0, 0, 7, 0, 1, 0],
    [0, 0, 0, 4, 0, 0, 7, 0, 0],
    [6, 7, 0, 0, 2, 0, 0, 5, 8],
    [3, 0, 1, 0, 5, 8, 0, 0, 6]
    ];
input = [
    [0, 0, 9, 4, 0, 1, 2, 0, 0],
    [0, 8, 3, 0, 0, 0, 1, 5, 0],
    [1, 2, 0, 0, 0, 0, 0, 3, 4],    
    [5, 0, 0, 8, 0, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 9, 0, 6, 0, 0, 8],
    [7, 1, 0, 0, 0, 0, 0, 2, 3],
    [0, 6, 5, 0, 0, 0, 8, 7, 0],
    [0, 0, 4, 7, 0, 8, 6, 0, 0]
    ];
  
def printSuduko(a):
    for i in range(M):
        for j in range(N):
            print(a[i][j],end = "|")
        print()

#printing the suduku board in formatted structure 
def drawSudokuBoard(board):    
    print()
    for row in range(M):
        s = ''
        for col in range(N):
            s += str(board[row][col]) + ' '
            if not (col + 1) % COLUMN_GRID:
                s += '| '# pipe symbol added
        s = s[:-1] # Removes trailing space

        print(s)
        if not (row + 1) % ROW_GRID:
            print('-' * len(s))



#search the number in row and column and the grid. if its not in neighbors return 
def findNeighbors(input, row, col, val):
    for C in range(M):
        if input[row][C] == val:
            return False
             
    for C in range(N):
        if input[C][col] == val:
            return False
 
 
    startRow = row - row % ROW_GRID
    startCol = col - col % COLUMN_GRID
    for i in range(ROW_GRID):
        for j in range(COLUMN_GRID):
            if input[i + startRow][j + startCol] == val:
                return False
    return True


def solveBoard(input, row, col):
 
    if (row == M - 1 and col == N): #return once completed
        return True
    if col == M: # increment to next line 
        row += 1
        col = 0
    if input[row][col] > 0: #if already number exist move to next column
        return solveBoard(input, row, col + 1)
    for num in range(1, M + 1, 1):     
        if findNeighbors(input, row, col, num):         
            input[row][col] = num #assign the value if its not in grid and neighbor
            if solveBoard(input, row, col + 1):
                return True
        input[row][col] = 0
        #print("Solve grid :"+  str(num))
        #drawSudokuBoard(input); #debug each check changes.
    return False

#printing credits:
printCredits("author :John Vimalraj");
printCredits("Subject : COSC550");
printCredits("Algorithm: Solving 9*9 suduko");
#printSuduko(input);
printCredits("Input Suduko Board");
drawSudokuBoard(input)
printCredits("Output Solved Suduko Board: ");
if (solveBoard(input, 0, 0)):
    drawSudokuBoard(input);
else:
    print("The given problem is not solvable")
