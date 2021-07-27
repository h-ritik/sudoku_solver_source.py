# this function finds the next empty cell
def find_next_spot(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i,j
    return -1,-1

# this function checks if the guess v is valid
def check_validity(sudoku,i,j,v):
    if all([v != sudoku[i][y] for y in range(9)]) and all([v!=sudoku[x][j] for x in range(9)]):
        startx,starty = 3*(i//3), 3*(j//3)
        for x in range(startx,startx+3):
            for y in range(starty,starty+3):
                if sudoku[x][y] == v:
                    return False
        return True
    return False

# this function makes a guess and invokes ifvalid to check its validity
# in case the guess is valid, the function calls itself recursively
def solve_sudoku(sudoku):
    i,j = find_next_spot(sudoku)
    if i == -1:
        return True
    for v in range(1,10):
        if check_validity(sudoku,i,j,v):
            sudoku[i][j] = v
            if solve_sudoku(sudoku):
                return True
            sudoku[i][j] = 0
    return False

# this function prints the sudoku
def print_sudoku(sudoku):
    for i in range(9):
        print((("\n"*2) if i%3 == 0 else ""),end= "")
        for j in range(9):
            print(("    " if j%3 == 0 else " "),end= "")
            print(sudoku[i][j],end="")
        print()
# a sample input
sudoku=[[5,1,7,6,0,0,0,3,4],
        [0,8,9,0,0,4,0,0,0],
        [3,0,6,2,0,5,0,9,0],
        [6,0,0,0,0,0,0,1,0],
        [0,3,0,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]]

# invokes the solve function
solve_sudoku(sudoku)

# prints the output
print_sudoku(sudoku)