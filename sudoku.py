board = [[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]]
		
def findEmptyCell():
	for x in range(9):
		for y in range(9):
			if(board[x][y] == 0):
				return x, y
	return -1, -1

def checkRows(x,z):
	for i in range(9):
		if(board[x][i]==z):
			return False

	return True

def checkColumns(y,z):
	for i in range(9):
		if(board[i][y]==z):
			return False

	return True

def checkSector(x,y,z):
	sectorX = 3 * (x//3)
	sectorY = 3 * (y//3)
	for i in range(sectorX, sectorX+3):
		for j in range(sectorY, sectorY+3):
			if(board[i][j]==z):
				return False

	return True

def valid(x,y,z):
	rowvalid = checkRows(x,z)
	if(rowvalid):
		columnValid = checkColumns(y,z)
		if(columnValid):
			sectorValid = checkSector(x,y,z)
			if(sectorValid):
				return True

	return False

def solve(x=0,y=0):
	x, y = findEmptyCell()
	if(x==-1):
		return True

	for i in range(1,10):
		if valid(x,y,i):
			board[x][y] = i
			if solve(x,y):
				return True

			board[x][y] = 0

	return False


solve()
print(board)