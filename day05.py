#file = open("test05.txt")
file = open("input05.txt")

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

for range in mergeLimits: # fix ordering of start and finish just in case
    if range[0] > range[1]:
        temp = range[0]
        range[0] = range[1]
        range[1] = temp

# merges a pair of ranges from a list of ranges if they overlap
# returns mergeability
def mergeRanges(i, j, rangeList):
    i0 = rangeList[i][0]
    i1 = rangeList[i][1]
    j0 = rangeList[j][0]
    j1 = rangeList[j][1]
    #print(rangeList)
    #print("Merging [" + str(i0) + ", " + str(i1) + "] with [" + str(j0) + ", " + str(j1) + "]")
    new0 = min(i0,i1,j0,j1)
    new1 = max(i0,i1,j0,j1)
    canMerge = True
    # I < J: we cannot merge if i0 < i1 < j0 < j1 and i1 < j0 - 1, analogous for J < I
    if ((i0 < i1) and (i1 < j0) and (j0 < j1) and (i1 < (j0-1))) or ((j0 < j1) and (j1 < i0) and (i0 < i1) and (j1 < (i0-1))):
        canMerge = False
    if canMerge:
        del rangeList[j]
        del rangeList[i]
        rangeList.append([new0, new1])
    #print(rangeList)
    #print('')
    return canMerge

def mergeRangeList(rangeList):
    iterI = 0
    iterJ = 1
    while (iterI < iterJ):
        if iterJ < len(rangeList): # make sure to not be out of bound
           merged = mergeRanges(iterI, iterJ, rangeList) # try to merge current two ranges
        # iterator handling to compare each pair of ranges
        if (iterJ == len(rangeList)): # secondary iterator reached end of list
            iterI += 1
            iterJ = min(len(rangeList), iterI+1) # restart secondary iterator at primary+1 or keep at end of list if exceeded to ensure iterI==iterJ
        else:
            iterJ += 1
        if merged: # successful merge changes list structure -> reset iteration
            iterI = 0
            iterJ = 1
    print(rangeList)
    print(len(rangeList))

mergeRangeList(mergeLimits)

sumFresh = 0
for limit in mergeLimits:
    sumFresh += (limit[1] - limit[0] + 1)
print(sumFresh)