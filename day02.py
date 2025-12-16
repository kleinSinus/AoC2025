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

def checkIDs (idRange):
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
                #print("Bad ID: " + str(id))
    return(bad)

badIDs = []
for item in ranges:
    badIDs += checkIDs(item)

badSum = 0
for badID in badIDs:
    badSum += badID

print(badSum)