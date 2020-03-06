#************************FUNCTIONS*************************
def creat2DArray(row, col):
  #create a blank 2D array
  grid = []
  for i in range(row):
    grid.append([])
    
  for row in range(len(grid)):
    for column in range(col):
      #add a space to create a blank 2D array
      grid[row].append("")
  
  return grid

#******************************MAIN***************************
inFile = open("Prob08.txt", "r")

#read how many cases there are and convert the strng into an int
case = inFile.readline()
case = case.replace("\n", "")
case = int(case)

for c in range(case):
  grid = creat2DArray(20, 20)
  input = inFile.readline()

inFile.close()
