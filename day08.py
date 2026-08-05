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

class Junction:
    def __init__(self, position):
        self.position = position
    def __str__(self):
        return f"{self.position}"

class Circuit:
    def __init__(self, junction):
        self.junctions = [junction]
    def __str__(self):
        circOut = "Circuit of length " + str(len(self.junctions)) + "\nWith junctions at \n"
        for junction in self.junctions:
            circOut += "    " + str(junction)
        return circOut
    def contains(self, junction):
        for item in self.junctions:
            if (item[0] == junction[0]) and (item[1] == junction[1]) and (item[2] == junction[2]):
                return True
        return False
    def connect(self, junction):
        if not self.contains(junction):
            self.junctions.append(junction)

circuits = []
for line in input1:
    coordStrings = line.split(',')
    coords = []
    for coordString in coordStrings:
        coords.append(int(coordString))
    newJunction = Junction(coords)
    newCircuit = Circuit(newJunction)
    circuits.append(newCircuit)

for circuit in circuits:
    print(circuit)

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



print(getMinDistancePair(junctionBoxCoords1))