#**************************FUNCTION***********************
def speeding(speedAr, birthday):
  for t in range(len(speedAr)):
    #contranits for speed
    no = 60
    small = 61
    big = 81

    #add 5 to all contraints if it is thier birthday
    if(birthday == True):
      no += 5  
      small += 5
      big += 5
      print("added")

      
    #checks if the person gets no ticket
    if(speedAr[t] <= no):
      print("no ticket")
    
    #checks if the person gets a small ticket
    elif(speedAr[t] >= small and speedAr[t] < big):
      print("small ticket")

    #checks if the person gits a big ticket
    else:
      print("big ticket")

def removeChar(a):
  #removes the end line escape character
  for i in range(len(a)):
    a[i] = a[i].replace("\n", "")

def removeSpace(ar):
  #removes any spaces
  for i in range(len(ar)):
    ar[i] = ar[i].replace(" ", "")

def strToInt(array):
  #convert the numbers stored as strings to inergers
  for i in range(len(array)):
    array[i] = int(array[i])


#*************************MAIN***********************
#convert file into array
inFile = open("Prob04.txt", "r")
line = inFile.readline()

prob4 = []
while(line):
  prob4.append(line)
  line = inFile.readline()
inFile.close()

#code to process the array

#remove enline char and spaces in each element
removeChar(prob4)
removeSpace(prob4)

#spilit into two arrays
speed = []
birthday = []
for x in range(len(prob4)):
  speed.append(prob4[x][0] + prob4[x][1])
  
  #adding to the birthday array
  if(prob4[x][2] == "t"):
    birthday.append(True)
  else:
    birthday.append(False)

strToInt(speed)

speeding(speed, birthday)
