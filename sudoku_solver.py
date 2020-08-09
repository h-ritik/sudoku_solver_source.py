# solves a 9*9 sudoku by backtracing

# global variable backtrack
backtrack=0

# this function finds the next empty cell
def nextbox(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return (i,j)
	return -1,-1


# this function checks if the guess v is valid
def ifvalid(sudoku,i,j,v):
	rowcheck=all([v!=sudoku[i][z] for z in range(9)])
	if rowcheck:
		columncheck=all([v!=sudoku[z][j] for z in range(9)])
		if columncheck:
			x,y=3*(i//3),3*(j//3)
			for m in range(x,x+3):
				for n in range(y,y+3):
					if sudoku[m][n]==v:
						return False
				return True
	return False

# this function makes a guess and invokes ifvalid to check its validity
# in case the guess is valid, the function calls itself recursively
def solve(sudoku):
	global backtrack
	i,j=nextbox(sudoku)
	if i==-1:
		return True

	for v in range(1,10):
		if ifvalid(sudoku,i,j,v):
			sudoku[i][j]=v
			if solve(sudoku):
				return (True)
			sudoku[i][j]=0
			backtrack+=1
	return(False)

# this function prints the sudoku
def printSudoku(sudoku):
	global backtrack
	for x in range(9):
		if x%3==0 and x!=0:
			print(" ")
		print(sudoku[x][0:3]," ",sudoku[x][3:6]," ",sudoku[x][6:9])
	print("backtrack=",backtrack)

# an input to the program
put=[[5,1,7,6,0,0,0,3,4],
     [0,8,9,0,0,4,0,0,0],
     [3,0,6,2,0,5,0,9,0],
     [6,0,0,0,0,0,0,1,0],
     [0,3,0,0,0,6,0,4,7],
     [0,0,0,0,0,0,0,0,0],
     [0,9,0,0,0,0,0,7,8],
     [7,0,3,4,0,0,5,6,0],
     [0,0,0,0,0,0,0,0,0]]

# solve is invoked
print(solve(put))

# prints the output
printSudoku(put)