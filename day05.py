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

print(countIntegersInRangeLists(ingredientList1, rangeList1))
print(countIntegersInRangeLists(ingredientList2, rangeList2))