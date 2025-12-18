#file = open("input/test05.txt")
file = open("input/input05.txt")

def parseInput(inputFile):
    inputList = []
    for line in inputFile:
        if(line[0] == '\n'): # keep empty lines as empty strings
            inputList.append("")
        elif(line[-1] == '\n'): # remove line break from line
            inputList.append(line[:-1])
        else:
            inputList.append(line) # last line has no line break

