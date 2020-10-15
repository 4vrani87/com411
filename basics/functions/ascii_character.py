print("Program Started!")
print("please enter a number between 32 - 126: ")
number = abs(int(input()))

if(number >= 32 and number <= 126):
 ascii_letter = chr(number)
 print("The character represented by the ASCII code {} is {}. " .format( number, ascii_letter))
else:
 print("invalid input")

print("\n\nPROGRAM ENDED!")