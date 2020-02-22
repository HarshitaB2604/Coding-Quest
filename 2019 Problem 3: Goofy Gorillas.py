#********************FUNCTIONS********************
def goofyGorrillas(array):
  #warns the zoo keeper if needed
  warn = []
  for i in range(len(array)):
    if(array[i] == "true false" or array[i] == "false true"):
      warn.append("false")
    else:
      warn.append("true")
      
  printAr(warn)

def removeChar(a):
  #removes the end line escape character
  for i in range(len(a)):
    a[i] = a[i].replace("\n", "")


def printAr(ar):
  #prints out the whole array
  for element in range(len(ar)):
    print(ar[element])


#********************MAIN************************
#open the file and convert to one array
filepath = "input.txt"
inFile = open(filepath, "r")

#convert text file to array
smile = []
line = inFile.readline()
while(line):
  smile.append(line)
  line = inFile.readline()

inFile.close()

#remove the extra escape characters
removeChar(smile)

#run warning function
goofyGorrillas(smile)
