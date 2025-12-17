import math

#file = open("test03.txt")
file = open("input03.txt")

batteryBanks = []
for line in file:
    batteryBanks.append(line[:-1]) # drop line break

def findJoltage(bank):
    prime = 0
    second = 0
    index = 0
    for i in range(len(bank)-1):
        if prime < int(bank[i]):
            prime = int(bank[i])
            index = i
    for j in range(index+1, len(bank)):
        if second < int(bank[j]):
            second = int(bank[j])
    return 10 * prime + second

outputJoltage = 0
for bank in batteryBanks:
    outputJoltage += findJoltage(bank)
    #print(findJoltage(bank))

print(outputJoltage)