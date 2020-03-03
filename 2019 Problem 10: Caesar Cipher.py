#************************FUNCTIONS*************************
def removeChar(a, character):
  #replaces a certian character in a string
  for i in range(len(a)):
    a[i] = a[i].replace(character, "")

def strToFloat(ar):
  #convert string to ints
  for i in range(len(ar)):
    ar[i] = float(ar[i])

#def decode(code):

#******************************MAIN***************************
inFile = open("Prob10.txt", "r")

#read how many cases there are and convert the strng into an int
case = inFile.readline()
case = case.replace("\n", "")
case = int(case)

for c in range(case):
  #find the shift in the cypher
  shift = inFile.readline()
  shift = shift.replace("\n", "")
  shift = int(shift)
  code = inFile.readline()
  code = code.replace("\n", "")

  
  for i in range(len(code)):
    #only if the character in that position is not a space change it to its ascii number and remove the shift
    if(code[i] != " "):
      decrypt = ord(code[i]) - shift
    else:
      decrypt = " "
    
    decryptCode = decryptCode + decrypt
  

inFile.close()
