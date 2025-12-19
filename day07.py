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
                    if not contains(charNr, beams):
                        beams.append(charNr)
            elif char == '^':
                if contains(charNr, trace[lineNr-1]):
                    if not contains(charNr-1, beams):
                        beams.append(charNr-1)
                    if not contains(charNr+1, beams):
                        beams.append(charNr+1)
        trace.append(beams)
        cleanTrace = []
        for i in range(len(trace)):
            if i % 2 == 0:
                cleanTrace.append(trace[i])
    return cleanTrace

def countSplits(trace):
    splits = 0
    for step in range(len(trace)-1):
        for pos in trace[step]:
            if not contains(pos,trace[step+1]): # directly after a split, the split position is not in the trace
                splits += 1
    return splits

trace1 = traceBeam(input1)
trace2 = traceBeam(input2)

print("Splits with test data: " + str(countSplits(trace1)))
print("Splits with challenge: " + str(countSplits(trace2)) + '\n')

def areNeighbors(intA, intB):
    if (intA == intB+1) or (intA+1 == intB):
        return True
    else:
        return False

def getMagnitudes(trace): # magnitude of a single traceline goes up where two timelines merge
    magnitudes = []
    for step in trace:
        magnitudes.append([1]*len(step))
    for stepNr in range(1, len(trace)):
        prevStep = trace[stepNr-1]
        currStep = trace[stepNr]
        for beamNr in range(len(currStep)):
            currBeam = trace[stepNr][beamNr]
            if contains(currBeam-1, prevStep) and contains(currBeam+1, prevStep): # merge happens with two possible parent 
                magnitudes[stepNr][beamNr] += 1
    return magnitudes

print(trace1)
print(getMagnitudes(trace1))