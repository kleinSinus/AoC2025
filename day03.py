import math

#file = open("test03.txt")
file = open("input03.txt")

batteryBanks = []
for line in file:
    if (line[-1] == '\n'):
        batteryBanks.append(line[:-1]) # drop line break
    else:
        batteryBanks.append(line)

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

def findUnlimitedJoltage(bank):
    numBatteries = 12
    config = bank
    while len(config) > numBatteries:
        #print (config)
        candidates = []
        for i in range(len(config)):
            candidates.append(int(config[0:i] + config[i+1:])) # drop one battery
        config = str(max(candidates))
    #print(config + "\n")
    return int(config)

outputJoltage = 0
for bank in batteryBanks:
    outputJoltage += findJoltage(bank)
    #print(findJoltage(bank))

outputUnlimitedJoltage = 0
for bank in batteryBanks:
    outputUnlimitedJoltage += findUnlimitedJoltage(bank)
    #print(findUnlimitedJoltage(bank))

print(outputJoltage)
print(outputUnlimitedJoltage)