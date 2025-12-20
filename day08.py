import math

file1 = open("input/test08.txt")
file2 = open("input/input08.txt")

def parseInput(inputFile):
    inputList = []
    for line in inputFile:
        if(line[0] == '\n'): # keep empty lines as empty strings
            inputList.append("")
        elif(line[-1] == '\n'): # remove line break from line
            inputList.append(line[:-1])
        else:
            inputList.append(line) # last line has no line break
    return inputList

input1 = parseInput(file1)
input2 = parseInput(file2)

junctionBoxCoords1 = []
for line in input1:
    coordStrings = line.split(',')
    coords = []
    for coordString in coordStrings:
        coords.append(int(coordString))
    junctionBoxCoords1.append(coords)

junctionBoxCoords2 = []
for line in input2:
    coordStrings = line.split(',')
    coords = []
    for coordString in coordStrings:
        coords.append(int(coordString))
    junctionBoxCoords2.append(coords)

def euklideanDist3D(coordA, coordB):
    xDiffSquared = (coordA[0] - coordB[0])**2
    yDiffSquared = (coordA[1] - coordB[1])**2
    zDiffSquared = (coordA[2] - coordB[2])**2
    return math.sqrt(xDiffSquared + yDiffSquared + zDiffSquared)

def getMinDistancePair(coordList):
    numCandidates = len(coordList)
    candidates = [[],[]]
    if numCandidates < 2:
        print("Not enough candidates! Returning empty!")
    else:
        candidates = [coordList[0], coordList[1]] # init with first two and their distance
        minDist = euklideanDist3D(coordList[0], coordList[1])
        for i in range(numCandidates-1): # then compare if there's any lower distances
            for j in range(i+1, numCandidates):
                candA = coordList[i]
                candB = coordList[j]
                dist = euklideanDist3D(candA, candB)
                if dist < minDist:
                    minDist = dist
                    candidates[0] = candA
                    candidates[1] = candB
    return candidates



print(getMinDistancePair(junctionBoxCoords))