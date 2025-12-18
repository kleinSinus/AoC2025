file = open("test05.txt")
#file = open("input05.txt")

freshRangesParsed = False
freshnessLimits = []
ingredients = []
countLines = 0
for line in file:
    if not freshRangesParsed:
        countLines += 1
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
    i0 = rangeList[i][0]
    i1 = rangeList[i][1]
    j0 = rangeList[j][0]
    j1 = rangeList[j][1]
    new0 = 0
    new1 = 1
    countNewMerges = 0
    overlapFound = False
    if (i0 < i1) and (i1 < j0) and (j0 < j1) and (i1 == (j0-1)): # touching I < J
        overlapFound = True
        new0 = i0
        new1 = j1
    elif (j0 < j1) and (j1 < i0) and (i0 < i1) and (j1 == (i0-1)): # touching J < I
        overlapFound = True
        new0 = j0
        new1 = i1
    elif (i0 < j0) and (j0 < i1) and (i1 < j1): # overlap I < J
        overlapFound = True
        new0 = i0
        new1 = j1
    elif (j0 < i0) and (i0 < j1) and (j1 < i1): # overlap J < I
        overlapFound = True
        new0 = j0
        new1 = i1
    elif (i0 < j0) and (j0 < j1) and (j1 < i1): # I contains J
        overlapFound = True
        new0 = i0
        new1 = i1
    elif (j0 < i0) and (i0 < i1) and (i1 < j1): # J contains I
        overlapFound = True
        new0 = j0
        new1 = j1
    elif (i0 == j0) and (i1 == j1): # I and J identical
        overlapFound = True
        new0 = i0
        new1 = i1
    elif (i0 == j0) and (i1 < j1): # I and J identical start, but J contains I
        overlapFound = True
        new0 = i0
        new1 = j1
    elif (i0 == j0) and (j1 < i1): # I and J identical start, but I contains J
        overlapFound = True
        new0 = i0
        new1 = i1
    elif (i1 == j1) and (i0 < j0): # I and J identical end, but J contains I
        overlapFound = True
        new0 = i0
        new1 = j1
    elif (i1 == j1) and (j0 < i0): # I and J identical end, but I contains J
        overlapFound = True
        new0 = i0
        new1 = i1
    if overlapFound:
        del rangeList[j]
        del rangeList[i]
        rangeList.append([new0, new1])
    return overlapFound

def mergeRangeList(rangeList):
    iterI = 0
    iterJ = 1
    while (iterI < iterJ):
        if (iterJ == len(rangeList)):
            iterI += 1
            iterJ = min(len(rangeList),iterI+1)
        elif not mergeRanges(iterI, iterJ, rangeList):
            iterJ += 1
        else:
            iterI = 0
            iterJ = 1
    print(len(rangeList))

mergeRangeList(mergeLimits)

sumFresh = 0
for limit in mergeLimits:
    sumFresh += (limit[1] - limit[0] + 1)
print(sumFresh)