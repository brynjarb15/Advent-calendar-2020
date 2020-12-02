f = open("day1.1.txt", "r")
numbers = f.read().splitlines()

i = 0
for n in numbers:
  numbers[i] = int(n)
  i += 1

numbersDict = {}
for n in numbers:
  numbersDict[n] = n
print(numbersDict)
  

#Day 1 Part 1
'''
for n in numbers:
  rest = 2020-n
  if rest in numbersDict.keys():
    print('n: ' + str(n) + ' * rest: ' + str(rest) + ' = ' + str(n*rest))
  #print(rest)

'''

#Day 1 part 2

for n in numbers:
  for m in numbers:
    rest = 2020-n-m
    if rest in numbersDict.keys():
      print('n + m + rest = 2020')
      print(str(n) + ' + ' + str(m) + ' + ' + str(rest) + ' = ' + str(n+m+rest))
      print('n * m * rest = ')
      print(str(n) + ' * ' + str(m) + ' * ' + str(rest) + ' = ' + str(n*m*rest))





print('end')