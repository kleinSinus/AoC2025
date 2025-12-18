#file = open("test05.txt")
file = open("input05.txt")

freshRangesParsed = False
freshnessLimits = []
ingredients = []
for line in file:
    if line[0] == '\n':
        freshRangesParsed = True
    elif freshRangesParsed:
        if(line[-1] == '\n'):
            ingredients.append(int(line[:-1]))
        else:
            ingredients.append(int(line))
    else:
        start = int(line.split('-')[0])
        end = int(line.split('-')[1])
        freshnessLimits.append([start, end])

# determines whether an ingredient is found within a certain range
def findItemInRange(item, range):
    if (item >= range[0]) and (item <= range[1]):
        return True
    else:
        return False

countFresh = 0
for ingredient in ingredients:
    for idRange in freshnessLimits:
        if findItemInRange(ingredient, idRange):
            countFresh += 1
            break

print(countFresh)

mergeLimits = freshnessLimits.copy()

# merges a pair of ranges from a list of ranges if they overlap, returns mergability
def mergeRanges(i, j, rangeList):
    startI = rangeList[i][0]
    endI = rangeList[i][1]
    startJ = rangeList[j][0]
    endJ = rangeList[j][1]
    newStart = startI
    newEnd = endI
    overlapFound = False
    if (startI >= startJ) and (startI <= endJ): # start within second range --> overlap
        overlapFound = True
        newStart = startJ
    if (endI >= startJ) and (endI <= endJ): # end within second range --> overlap
        overlapFound = True
        newEnd = endJ
    if overlapFound:
        del rangeList[j]
        del rangeList[i]
        rangeList.append([newStart, newEnd])
    return overlapFound
        
#print(freshnessLimits)
for limit in freshnessLimits:
    if limit[0] > limit[1]:
        print("Boah ne")
        break

iterI = 0
iterJ = 1
while (iterI < iterJ):
    if (iterJ == len(mergeLimits)):
        iterI += 1
        iterJ = min(len(mergeLimits),iterI+1)
    elif not mergeRanges(iterI, iterJ, mergeLimits):
        iterJ += 1
    else:
        iterI = 0
        iterJ = 1
    #print(mergeLimits)

#print(mergeLimits)
sumFresh = 0
for limit in mergeLimits:
    sumFresh += limit[1] - limit[0] + 1
print(len(freshnessLimits), len(mergeLimits))
print(sumFresh)