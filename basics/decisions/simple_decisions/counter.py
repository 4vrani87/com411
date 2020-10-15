print("Please enter the first whole number!")
firstNumber = int(input())

print("Please enter the second whole number!")
secondNumber = int(input())

print("please enter the third whole number!")
thirdNumber = int(input())

num_even = 0
num_odd = 0

if(firstNumber %2 ==0):
  num_even += 1
else:
  num_odd += 1

if(secondNumber %2 ==0):
  num_even += 1
else:
  num_odd += 1

if(thirdNumber %2 ==0):
  num_even += 1
else:
  num_odd += 1

print("There were {} even and {} odd numbers." .format(num_even, num_odd))