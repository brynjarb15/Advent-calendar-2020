from collections import OrderedDict as odict, Counter

with open('input-day10.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
numbers = sorted(content)
numbers.append(numbers[-1] + 3)

joltCounts ={ 1: 0, 2: 0, 3: 0}
#print(numbers)
lastNumber = 0
for n in numbers:
    diff = n - lastNumber
    if diff < 1 or diff > 3:
        continue
    joltCounts[diff] += 1
    lastNumber = n
print(joltCounts[1]*joltCounts[3]) # 2516


def checkAdapters(adapters):
    if len(adapters) == 1:
        return 1
    else:
        checkAdapters(adapters[1:])

sum = 0
for n in numbers:
    counter = 0
    for i in numbers:
        if i < n or i > n+3:
            continue
    




# 2407 is to low


