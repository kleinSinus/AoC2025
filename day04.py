#file = open("test04.txt")
file = open("input04.txt")

grid = []

for line in file:
    if line[-1] == '\n':
        grid.append(line[:-1])
    else:
        grid.append(line)

#for row in grid:
#    print (row)
#print('')

#returns number of adjacent rolls for given coordinates and input-grid
def checkNeighborhoodRolls(row, col, input):
    if (row < 0) or (col < 0) or (row >= len(input[0])) or (col >= len(input)): # requested cell out of bounds
        return -1
    if not (input[row][col] == '@'): # requested cell has no roll
        return -1 
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i < 0) or (j < 0) or (i >= len(input[0])) or (j >= len(input)) or ((i==row) and (j==col)): # neighborhood out of bounds
                pass
            else:
                if (input[i][j] == '@'):
                    count += 1
    return count

# removes accessible roles from a marked input grid, overwrites the grid, returns number of removed items
def removeMarkedRolls(input):
    removeNum = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if (input[row][col] == 'x'):
                input[row] = input[row][0:col] + "." + input[row][col+1:]
                removeNum += 1
    #print("\nRemove " + str(removeNum) + " rolls.\n")
    return removeNum

countAccessibleRolls = 0
markedGrid = grid.copy()

for row in range(len(grid)):
    for cell in range(len(grid[0])):
        cellStatus = checkNeighborhoodRolls(row, cell, grid)
        if (cellStatus >= 0) and (cellStatus < 4):
            markedGrid[row] = markedGrid[row][0:cell] + "x" + markedGrid[row][cell+1:]
            countAccessibleRolls += 1
        
#for row in markedGrid:
#    print(row)

while(removeMarkedRolls(markedGrid) > 0):
    newGrid = markedGrid.copy()
#    for row in markedGrid:
#        print(row)
    for row in range(len(markedGrid)):
        for cell in range(len(markedGrid[0])):
            cellStatus = checkNeighborhoodRolls(row, cell, markedGrid)
            if (cellStatus >= 0) and (cellStatus < 4):
                newGrid[row] = newGrid[row][0:cell] + "x" + newGrid[row][cell+1:]
                countAccessibleRolls += 1
#    print("\nMark new rolls\n")
    markedGrid = newGrid
#    for row in markedGrid:
#        print(row)

print(countAccessibleRolls)