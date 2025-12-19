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

print("The grand total in the test data is " + str(problemSum1) + ".")
print("The grand total in the challenge is " + str(problemSum2) + ".")