#file = open("input/test05.txt")
file = open("input/input05.txt")

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

freshnessLimits2 = freshnessLimits.copy()

# order individual items in a list of ranges such that start <= end any time
def fixOrdering(rangeList):
    for range in rangeList: # fix ordering of start and finish just in case
        start = range[0]
        end = range [1]
        if start > end: # flip if start after end
            range[0] = end
            range[1] = start

# for two ranges checks whether they can be merged
def mergePossible(rangeA, rangeB):
    a0 = rangeA[0]
    a1 = rangeA[1]
    b0 = rangeB[0]
    b1 = rangeB[1]
    if (a0 < a1) and (a1 < b0) and (b0 < b1): # two separate ranges, A < B
        if (b0 == (a1 + 1)): # B continues right where a left off
            return True
        else:
            return False
    else: # there must be some overlap
        return True

# for two ranges with assumed overlap, return merge product
# for ranges without overlap, merge product will include the space between
def mergeRanges(rangeA, rangeB):
    a0 = rangeA[0]
    a1 = rangeA[1]
    b0 = rangeB[0]
    b1 = rangeB[1]
    new0 = min(a0,a1,b0,b1)
    new1 = max(a0,a1,b0,b1)
    return [new0, new1]

# input: list of ranges
# function: merge ranges where possible within the input list
def mergeRangeList(rangeList):
    #print(rangeList)
    iterA = 0
    iterB = 1
    while (iterA < iterB):
        #print(iterA, iterB, len(rangeList))
        mergeable = False
        if (iterB < len(rangeList)): # make sure to not be out of bound
            mergeable = mergePossible(rangeList[iterA], rangeList[iterB])
        if mergeable:
            rangeA = rangeList[iterA]
            rangeB = rangeList[iterB]
            mergeProd = mergeRanges(rangeA, rangeB) # merge current two ranges
            del rangeList[iterB]
            del rangeList[iterA]
            rangeList.append(mergeProd)
            # reset iterators
            iterA = 0
            iterB = 1
        # iterator handling to compare each pair of ranges
        else:
            if (iterB == len(rangeList)): # 2nd iterator reached end of list
                iterA += 1
                iterB = min(len(rangeList), iterA+1) # reset 2nd iterator
            else:
                iterB += 1
    print(rangeList)
    print(len(rangeList))


fixOrdering(freshnessLimits2)
mergeRangeList(freshnessLimits2)

sumFresh = 0
for limit in freshnessLimits2:
    sumFresh += (limit[1] - limit[0] + 1)
print(sumFresh)