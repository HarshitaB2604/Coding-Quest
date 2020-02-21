#*********************FUNTIONS***********************
def sumIt(num1, num2):
  if(num1 != num2):
    sum = num1 + num2
  else:
    sum = 2*(num1 + num2)

  return sum  

#************************MAIN**********************
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print(sumIt(x, y))
