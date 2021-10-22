import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

def getAllChildBags(line):
    matches = re.findall(r'([0-9]+?) ([a-z]+ [a-z]+) bag', line)
    return matches

def countBagsInBag(childrenBags):
    if len(childrenBags) == 0:
        return 1
    totalBags = 0
    for bag in childrenBags: 
        totalBags += countBagsInBag(bagTypes[bag[1]])*int(bag[0])
    return totalBags
    

with open('input-day7.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

bagTypes = {}
for line in content:
    currentBag = ' '.join(line.split(' ')[0:2])
    if 'no other bags' in line:
        bagTypes[currentBag] = []
    else:
        bagTypes[currentBag] = getAllChildBags(line)

pp.pprint(bagTypes)

print(countBagsInBag([('1', 'shiny gold')]))



'''
somethingChanged = True
while somethingChanged:
    somethingChanged = False
    for bag in bagTypes:
        if bagTypes[bag] == True:
            continue
        if 'shiny gold' in bagTypes[bag]:
            bagTypes[bag] = True  # Shiny gold is a child bag
            somethingChanged = True
        else:
            for childBag in bagTypes[bag]:
                if bagTypes[childBag] == True:
                    bagTypes[bag] = True # Shiny gold is a child bag of current child
                    somethingChanged = True



total = 0
for bag in bagTypes:
    if bagTypes[bag] == True:
        total += 1
print(total)
'''




