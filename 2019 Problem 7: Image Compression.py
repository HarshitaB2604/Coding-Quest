import math

#************************FUNCTIONS*************************
def convert(input1, minAr, maxAr):
  print("Input: " + str(input1))
  output = ((input1-minAr)/(maxAr-minAr))*255
  output = math.ceil(output)
  print(output)

def removeChar(a, character):
  #replaces a certian character in a string
  for i in range(len(a)):
    a[i] = a[i].replace(character, "")

def strToInt(ar):
  #convert string to ints
  for i in range(len(ar)):
    ar[i] = float(ar[i])

#******************************MAIN***************************
inFile = open("C:\\Users\\mukta\\OneDrive\\Desktop\\honey\\hackathon\\VSC\\Prob07file.txt", "r")

#read how many cases there are and convert the strng into an int
case = inFile.readline()
case = case.replace("\n", "")
case = int(case)

#reading the file and adding to the list
for c in range(case):
  linesInTest = inFile.readline()
  linesInTest = linesInTest.replace("\n", "")
  linesInTest = int(linesInTest)

  nums = [] #contains values that need to be converted
  
  #add the numbers to a list
  for val in range(linesInTest):
    num = inFile.readline()
    nums.append(num)
  
  removeChar(nums, "\n")
  strToInt(nums)
  #print(nums)
  
  #convert the numbers
  minNum = min(nums)
  maxNum = max(nums)
  for x in range(0, linesInTest):
    print("Lines in test: " + str(linesInTest))
    print("X: " + str(x))
    print(nums[x])
    #convert(nums[i], minNum, maxNum)
  
inFile.close()
