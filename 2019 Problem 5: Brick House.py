#*********************************FUNCTIONS*********************************
def possibleHouse(shortBrick, longBrick, targetLen):
  #find if building the wall is possible

  for possible in range(len(targetLen)):
    #each short brick is 1 in
    shortBrickLen = 1*shortBrick[possible]
    #each long brick is 5 in
    longBrickLen = 5*longBrick

    totalLen = shortBrickLen + longBrickLen
    if(totalLen > targetLen or totalLen < targetLen):
      print("false")
    else: 
      print("true")

def removeChar(a, character):
  #replaces a certian character in a string
  for i in range(len(a)):
    a[i] = a[i].replace(character, "")    


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
removeChar(prob05, "\n")

#divides the main array into 3 arrays
shortBrick = []
longBrick = []
wallLenght = []

for i in range(len(prob05)):
  #find the two breaking points
  longBrickBreak = prob05[i].find(" ")
  wallLenBreak = prob05[i].find(" ", longBrickBreak + 1, len(prob05))
  shortBreak = longBrickBreak - 1 
  #add to the three parallel arrays
  temp = prob05[i]
  tempShort = temp[ :shortBreak]
  print(tempShort)
  '''
  tempLong =

  shortBrick.append(prob05[i][0])    
  longBrick.append(prob05[longBrickApen + 1])    
  wallLenght.append(prob05[wallLenApen + 1])
 
possibleHouse(shortBrick, longBrick, wallLenght)
'''
