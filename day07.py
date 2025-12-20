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

def calcCurrMags(prevBeams, currBeams, prevMags):
    newMags = [0] * len(currBeams)
    for beamNr in range(len(currBeams)-1):
        currBeam = currBeams[beamNr]
        nextBeam = currBeams[beamNr+1]
        if (nextBeam-currBeam == 2): # possible split children
            parentCandidate = currBeam + 1
            if contains(parentCandidate, prevBeams): # parent established
                for i in range(len(prevBeams)): # look up parents magnitude
                    if prevBeams[i] == parentCandidate:
                        parentMag = prevMags[i]
                        newMags[beamNr] += parentMag # and add it to children
                        newMags[beamNr+1] += parentMag
        if contains(currBeam, prevBeams): # direct descent
            parent = currBeam
            for i in range(len(prevBeams)): # look up parent mag
                if prevBeams[i] == parent:
                    parentMag = prevMags[i]
                    newMags[beamNr] += parentMag # and add it to child
    lastBeam = currBeams[-1]
    if contains(lastBeam, prevBeams): # direct descent of last beam
        parent = lastBeam
        for i in range(len(prevBeams)): # look up parent mag
            if prevBeams[i] == parent:
                parentMag = prevMags[i]
                newMags[beamNr] += parentMag # and add it to child
    return newMags

def getMagnitudes(trace): # magnitude of a single traceline goes up where two timelines merge
    magnitudes = []
    magnitudes.append([1])
    for stepNr in range(1, len(trace)):
        currBeamList = trace[stepNr]
        prevBeamList = trace[stepNr-1]
        prevMagList = magnitudes[stepNr-1]
        newMagList = calcCurrMags(prevBeamList, currBeamList, prevMagList)
        magnitudes.append(newMagList)
    return magnitudes

#print(trace1)
#print(getMagnitudes(trace1))

def getTimelinesCount(trace):
    count = 0
    lastMags = getMagnitudes(trace)[-1]
    for mag in lastMags:
        count += mag
    return count

print("Timelines counted in test data: " + str(getTimelinesCount(trace1)))
print("Timelines counted in challenge: " + str(getTimelinesCount(trace2)))