file1 = open("input/test07.txt")
file2 = open("input/input07.txt")

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

def contains(integer, inputList):
    for item in inputList:
        if item == integer:
            return True
    return False

# traces a tachyon beam and returns the number of splits
def traceBeam(input):
    trace = []
    splitNum = 0
    for lineNr in range(len(input)):
        beams = []
        line = input[lineNr]
        for charNr in range(len(line)):
            char = line[charNr]
            if lineNr == 0:
                if char == 'S':
                    beams.append(charNr)
            elif char == '.':
                if contains(charNr, trace[lineNr-1]):
                    beams.append(charNr)
            elif char == '^':
                if contains(charNr, trace[lineNr-1]):
                    beams.append(charNr-1)
                    beams.append(charNr+1)
                    splitNum += 1
        trace.append(beams)
    return splitNum

splits1 = traceBeam(input1)
splits2 = traceBeam(input2)

print("Splits with test data: " + str(splits1))
print("Splits with challenge: " + str(splits2) + '\n')