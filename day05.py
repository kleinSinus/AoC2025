file1 = open("input/test05.txt")
file2 = open("input/input05.txt")


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

inputList1 = parseInput(file1)
inputList2 = parseInput(file2)

# split input into rangeLists and ingredientLists
# with day 5 input split is empty line
rangeList1 = []
rangeList2 = []
ingredientList1 = []
ingredientList2 = []

splitPassed = False
for i in range(len(inputList1)):
    if len(inputList1[i]) == 0:
        splitPassed = True
    elif splitPassed:
        ingredientList1.append(int(inputList1[i]))
    else:
        newRangeStrings = inputList1[i].split('-')
        newRange = [int(newRangeStrings[0]), int(newRangeStrings[1])]
        rangeList1.append(newRange)

splitPassed = False
for i in range(len(inputList2)):
    if len(inputList2[i]) == 0:
        splitPassed = True
    elif splitPassed:
        ingredientList2.append(int(inputList2[i]))
    else:
        newRangeStrings = inputList2[i].split('-')
        newRange = [int(newRangeStrings[0]), int(newRangeStrings[1])]
        rangeList2.append(newRange)

# Check whether an integer is within an inclusive range
def itemFoundInRange(item, range):
    start = range[0]
    end = range[1]
    if (start <= item) and (item <= end):
        return True
    else:
        return False

# Input: List of integers, List of ranges
# Output: number of integers found within the ranges
def countIntegersInRangeLists(integerList, rangeList):
    count = 0
    for number in integerList:
        for range in rangeList:
            if itemFoundInRange(number, range):
                count += 1
                break
    return count

print("Fresh produce counted in test data: " + str(countIntegersInRangeLists(ingredientList1, rangeList1)))
print("Fresh produce counted in data:      " + str(countIntegersInRangeLists(ingredientList2, rangeList2)) + "\n")

# Input: Integer ranges A and B given by start and end
# Output: Boolean on whether the ranges overlap (or touch = if second range starts right after first)
def rangesAreOverlapping(rangeA, rangeB):
    a0 = rangeA[0]
    a1 = rangeA[1]
    b0 = rangeB[0]
    b1 = rangeB[1]
    if a0 < b0: # range A comes before B
        if b0 > (a1+1): # there is a real gap between the ranges
            return False
        else:
            return True
    else:
        if a0 > (b1+1): # there is a real gap between the ranges
            return False
        else:
            return True

# Input: Ranges A and B
# Output: Range C merged from A and B
def mergeRanges(rangeA, rangeB):
    return [min(rangeA[0], rangeB[0]), max(rangeA[1], rangeB[1])]

# Input: A list of ranges and two indexes
# Output: void
# Merges the indexed ranges if possible, overwrites input list
def mergeRangesInList(rangeList, a, b):
    if (a >= len(rangeList) or b >= len(rangeList)):
        print("Index out of bounds. No merge executed.")
        return rangeList
    rangeA = rangeList[a]
    rangeB = rangeList[b]
    overlap = rangesAreOverlapping(rangeA, rangeB)
    identical = (rangeA[0] == rangeB[0]) and (rangeA[1] == rangeB[1]) and (a == b)
    mergeable = overlap and not identical
    if mergeable:
        newRange = mergeRanges(rangeA, rangeB)
        del rangeList[max(a, b)] # delete later entry first
        del rangeList[min(a, b)]
        rangeList.append(newRange)

# Compact a list of ranges by merging overlapping ones
def makeCompactRangeList(rangeList):
    compactList = rangeList.copy()
    mergesAreHappening = True # Assume merges happening
    while mergesAreHappening:
        mergesAreHappening = False # Reassume within lopp
        for a in range(len(compactList)):
            if mergesAreHappening: # If B-loop set the flag, list is shortened -> reset needed to stay within bounds
                break;
            for b in range(len(compactList)):
                #print(a, b, len(compactList))
                rangeA = compactList[a]
                rangeB = compactList[b]
                overlap = rangesAreOverlapping(rangeA, rangeB)
                identical = (rangeA[0] == rangeB[0]) and (rangeA[1] == rangeB[1]) and (a == b) # same entry, not only same content
                mergeable = overlap and not identical
                if mergeable:
                    mergesAreHappening = True # until proven wrong
                    #print("Merging " + str(rangeA) + " and " + str(rangeB))
                    mergeRangesInList(compactList, a, b)
                    break
    return compactList

compactList1 = makeCompactRangeList(rangeList1)
#print(len(compactList1))
compactList2 = makeCompactRangeList(rangeList2)
#print(len(compactList2))

count1 = 0
count2 = 0

for range in compactList1:
    first = range[0]
    last = range[1]
    size = last - first + 1
    count1 += size
for range in compactList2:
    first = range[0]
    last = range[1]
    size = last - first + 1
    count2 += size
print("Fresh integers counted in test data: " + str(count1))
print("Fresh integers counted in data:      " + str(count2))