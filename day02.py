import math

#file = open("test02.txt")
file = open("input02.txt")

lines = []
for line in file:
    lines.append(line)

ranges = []

if len(lines) > 1:
    print("More than one input line given.")
else:
    input = lines[0].split(',') # split the ranges 
    for item in input:
        temp = item.split('-') # determine start and end of each range entry
        entry = []
        entry.append(int(temp[0]))
        entry.append(int(temp[1]))
        ranges.append(entry)

def getDoubles(idRange):
    bad = []
    start = idRange[0]
    end = idRange[1]
    idList = range(start, (end + 1)) # generate list from range limits
    for id in idList:
        digits = 0
        digitsCounted = False
        idCopy = id
        while not digitsCounted: # counting digits more reliable than imprecision of log
            idCopy //= 10
            digits += 1
            if idCopy < 1:
                digitsCounted = True
        if digits % 2 == 0:
            halfDigits = int(digits / 2)
            if (id // 10**halfDigits) == (id % 10**halfDigits):
                bad.append(id)
    return(bad)

def getMultiples(idRange):
    bad = []
    start = idRange[0]
    end = idRange[1]
    idList = range(start, (end + 1)) # generate list from range limits
    for id in idList:
        badID = False # assume bad ID
        digits = len(str(id))
        #print("Examining ID: " + str(id))
        for seqNum in range(2, digits+1): # up to n different sequences for an n-digit number, min 2 sequences
            if (digits % seqNum) == 0: # only do something if id divisible into number of sequences
                seqLen = digits // seqNum
                seq = str(id)[0:seqLen]
                compFailedAlready = False
                for i in range(1, seqNum): # compare everything with first sequence
                    seqStart = seqLen * i
                    seqEnd = seqLen * (i+1)
                    compSeq = str(id)[seqStart:seqEnd]
                    #print("Sequence comparison: " + str(seq) + " vs. " + str(compSeq))
                    if not (int(compSeq) == int(seq)):
                        compFailedAlready = True
                if not compFailedAlready:
                    badID = True
        if badID:
            bad.append(id)
    return(bad)

badIDs = []
badderIDs = []

#print(ranges)
for item in ranges:
    badIDs += getDoubles(item)
    badderIDs += getMultiples(item)

#print('')
#print(badIDs)
#print(badderIDs)
#print('')

badSum = 0
badderSum = 0
for badID in badIDs:
    badSum += badID

for badderID in badderIDs:
    badderSum += badderID

print(badSum)
print(badderSum)