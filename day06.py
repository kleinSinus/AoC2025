file1 = open("input/test06.txt")
file2 = open("input/input06.txt")

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

def identifyProblemsFromInput(inputList):
    problems = []
    for lineIndex in range(len(inputList)):
        line = inputList[lineIndex]
        problemIndex = -1
        lastCharacter = ' '
        for character in line:
            if not (character == ' '): # currently no space character
                if (lastCharacter == ' '): # previously space character
                    problemIndex += 1
                    if lineIndex == 0:
                        problems.append([]) # init problems in first line
                    problems[problemIndex].append("")
                problems[problemIndex][lineIndex] += character
            lastCharacter = character
    return problems

problemList1 = identifyProblemsFromInput(input1)
problemList2 = identifyProblemsFromInput(input2)

# Determines the sum of an input list of numbers given as strings
def listSum(inputList):
    sum = 0
    for number in inputList:
        sum += int(number)
    return sum

# Determines the product of an input list of numbers given as strings
def listProd(inputList):
    prod = 1
    for number in inputList:
        prod = prod * int(number)
    return prod

# Solves one problem from the lists
def solveProblem(problem):
    opSym = problem[-1]
    sol = 0
    if opSym == '+':
        sol = listSum(problem[:-1])
    elif opSym == '*':
        sol = listProd(problem[:-1])
    else:
        print("List appears to not be a problem to solve.")
    return sol

problemSum1 = 0
for problem in problemList1:
    problemSum1 += solveProblem(problem)
problemSum2 = 0
for problem in problemList2:
    problemSum2 += solveProblem(problem)

print("The grand total in the test data is " + str(problemSum1))
print("The grand total in the challenge is " + str(problemSum2) + "\n")

def parseCephalopodProblem(inputList):
    outputList = [[]]
    outIndex = 0
    lineLength = len(inputList[0])
    for i in range(lineLength):
        currIndex = lineLength - i - 1
        currNum = ''
        currSym = ''
        for line in inputList:
            if not (line[currIndex] == ' '): #if not space
                if not ((line[currIndex] == '*') or (line[currIndex] == '+')): # and not operator
                    currNum += line[currIndex] # add character to current Number
                else: # if operator
                    currSym = line[currIndex]
        if (currNum == '' and currSym == ''):
            outIndex += 1
            outputList.append([])
        elif not (currSym == ''):
            outputList[outIndex].append(currNum)
            outputList[outIndex].append(currSym)
        else:
            outputList[outIndex].append(currNum)
    return outputList

cephProblemList1 = (parseCephalopodProblem(input1))
cephProblemList2 = (parseCephalopodProblem(input2))

cephProblemSum1 = 0
for cephProblem in cephProblemList1:
    cephProblemSum1 += solveProblem(cephProblem)
cephProblemSum2 = 0
for cephProblem in cephProblemList2:
    cephProblemSum2 += solveProblem(cephProblem)

print("The grand total in the cephalopod test data is " + str(cephProblemSum1))
print("The grand total in the cephalopod challenge is " + str(cephProblemSum2))