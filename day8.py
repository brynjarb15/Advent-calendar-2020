import copy
import pprint
pp = pprint.PrettyPrinter(indent=4)


def runCommand(position, accumalator, commands):
    nextCommand = commands[position][0]
    if nextCommand == 'nop':
        position += 1
    elif nextCommand == 'acc':
        accumalator += eval(commands[position][1])
        position += 1
    elif nextCommand == 'jmp':
        position += eval(commands[position][1])

    return position, accumalator


with open('input-day8.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


def checkIfSolution(commands):
    currentPosition = 0
    accumalator = 0
    seenPositions = {}
    loopFound = False
    while True:
        if currentPosition in seenPositions:
            loopFound = True
            break
        else:
            seenPositions[currentPosition] = 1
        currentPosition, accumalator = runCommand(currentPosition, accumalator, commands)
    if loopFound:
        return False
    else:
        print('currentPosition', currentPosition)
        print('accumalator', accumalator)
    
    
allCommands = []
for line in content:
    allCommands.append(line.split(' '))

currPos = 0
for cmd in allCommands:
    nextCommand = cmd[0]
    if nextCommand == 'nop':
        newAllCommands = copy.deepcopy(allCommands)
        newAllCommands[currPos][0] = 'jmp'
        checkIfSolution(newAllCommands)
    elif nextCommand == 'jmp':
        newAllCommands = copy.deepcopy(allCommands)
        newAllCommands[currPos][0] = 'nop'
        checkIfSolution(newAllCommands)
    currPos += 1