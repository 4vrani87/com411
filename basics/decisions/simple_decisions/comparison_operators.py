print("Please enter the first number!")
firstNumber = int(input())
print("Please enter the second number!")
secondNumber = int(input())

if(firstNumber < secondNumber):
  print("{} is smaller than {}" .format(firstNumber, secondNumber))
elif(firstNumber > secondNumber):
  print("{} is smaller than {}" . format(secondNumber, firstNumber))
else:
  print("Both are equal!")