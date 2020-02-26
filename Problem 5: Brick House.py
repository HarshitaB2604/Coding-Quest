#*********************************FUNCTIONS*********************************
def divide(mainArray):
  shortBrick = []
  longBrick = []
  wallLenght = []

  for i in range(len(mainArray)):
    #find the two breaking points
    longBrickBreak = mainArray[i].find("n")
    wallLenBreak = mainArray[i].find("n", longBrickApen + 1, len(mainArray))
    
    #add to the three parallel arrays
    for i in range()
    shortBrick.append(mainArray[i][0])    
    longBrick.append(mainArray[longBrickApen + 1])    
    wallLenght.append(mainArray[wallLenApen + 1])

  print(longBrick)


def removeChar_Replace(a):
  #removes the end line escape character at the end and replaces any spaces with n
  for i in range(len(a)):
    a[i] = a[i].replace("\n", "")
    a[i] = a[i].replace(" ", "n")    


#************************************MAIN**********************************
#convert file to array
inFile = open("Prob05.txt", "r")
line = inFile.readline()

prob05 = []
while(line):
  prob05.append(line)
  line = inFile.readline()

inFile.close()

#processing the array
removeChar_Replace(prob05)
divide(prob05)
