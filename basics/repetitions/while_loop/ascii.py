print("how many bars should be charged?")

bars = int(input())
charged_bars = 1

while(charged_bars <= bars):
  print("charging: ", "█" * charged_bars)
  charged_bars += 1

print("The battery is fully charged")