#file = open("test01.txt") # file with smaller test input
file = open("input01.txt")

dial = 50 # initialize dial at value 50
zeroCount = 0 # initialize zero count
zeroPassCount = 0


print("Dial starts by pointing at " + str(dial))
for line in file:
    print("Dial rotates " + line[:-1] + ".")
    if line[0] == 'R':
        dial += int(line[1:])
        while dial > 99:
            dial -= 100
            zeroPassCount += 1
    elif line[0] == 'L':
        startedWithZero = False
        if dial == 0:
            startedWithZero = True
        dial -= int(line[1:])
        while dial < 0:
            dial += 100
            zeroPassCount += 1
        if startedWithZero:
            zeroPassCount -= 1
    print("Dial now points at " + str(dial))
    if dial == 0:
        zeroCount += 1
        if line[0] == 'L':
            zeroPassCount += 1
print('')
print(zeroCount)
print(zeroPassCount)