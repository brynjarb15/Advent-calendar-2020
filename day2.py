f = open("day2.txt", "r")
lines = f.read().splitlines()


#Day 2 part 2
numberOfValidLines = 0
for line in lines:
  # Get the data from the line
  line = line.split(' ')
  lowerIndex, higherIndex = line[0].split('-')
  #The indexes are 1 based, not 0 based
  lowerIndex = int(lowerIndex)-1
  higherIndex = int(higherIndex)-1
  letter = line[1][0]
  password = line[2]
  # Check if the indexes are the letter we are looking for
  isLowerIndexLetter = password[lowerIndex] == letter
  isHigherIndexLetter = password[higherIndex] == letter
  # If lower index is to high then the higher is also to high and we just continue
  if lowerIndex > len(password):
    continue
  # If the higher index is out of range and lower index works the password is valid
  elif higherIndex > len(password) and password[lowerIndex] == letter:
    numberOfValidLines += 1
  # If the 2 values xor-ed are true the password is valid
  elif isLowerIndexLetter != isHigherIndexLetter: 
    numberOfValidLines += 1

print('Number of valid passwords:')
print(numberOfValidLines)

#Day 2 part 1
'''
numberOfValidLines = 0
for line in lines:
  line = line.split(' ')
  lowerLimit, higherLimit = line[0].split('-')
  lowerLimit = int(lowerLimit)
  higherLimit = int(higherLimit)
  letter = line[1][0]
  password = line[2]
  numberOfLettersInPassword = password.count(letter)

  #print('count', numberOfLettersInPassword)
  if numberOfLettersInPassword<=higherLimit and numberOfLettersInPassword>=lowerLimit:
    numberOfValidLines += 1
    #print(password)

print(numberOfValidLines)
'''

