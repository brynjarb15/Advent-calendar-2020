import copy
import pprint
pp = pprint.PrettyPrinter(indent=4)

a = [1,2,3,4,5,6,7,8,9,10]

with open('input-day9.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

def checkNumber(previous25Numbers, currentNumber):
    for first in previous25Numbers:
        for second in previous25Numbers:
            if first == second:
                continue
            if first + second == currentNumber:
                return True
    return False

def findSum(numbers, total):
    sum = 0
    startPosition = 0
    currentPosition = 0
    while True:
        for number in numbers[startPosition:]:
            sum += number
            currentPosition += 1
            if sum == total:
                print('startPosition', startPosition)
                print('currentPosition', currentPosition)
                print('sum', sum)
            if sum > total:
                startPosition += 1
                sum = 0
                currentPosition = startPosition
                break
                



currentPosition = 25
'''
while True:
    nextPrevNumbers = content[currentPosition-25:currentPosition]
    currentNumber = content[currentPosition]
    if checkNumber(nextPrevNumbers, currentNumber):
        currentPosition += 1
    else:
        print(currentNumber)
        currentPosition += 1
'''

print(min(content[442:459]))
print(max(content[442:459]))
answer = 69316178
         
#findSum(content, answer)

print(content[442:459])


[3205921, 
 2845855, 
 2834836, 
 3083482, 
 3881565, 
 3840097, 
 4254961, 
 3652975, 
 3613632, 
 6516690, 
 4237730, 
 6045330, 
 3830685, 
 3832810, 
 4303716,
 4114745, 
 5221148]