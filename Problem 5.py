def divide(mainArray):
  shortBrick = []
  longBrick = []
  wallLenght = []

  for i in range(len(mainArray)):
    shortBrick.append(mainArray[i][0])
    
    longBrickApen = mainArray[i].find(n)
    longBrick.append(longBrickApen + 1)

    
    wallLenght.append(mainArray[i][2])

def removeChar_Replace(a):
  #removes the end line escape character at the end and replaces any spaces with n
  for i in range(len(a)):
    a[i] = a[i].replace("\n", "")
    a[i] = a[i].replace(" ", "n")    
