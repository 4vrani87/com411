print("how many live cables should I avoid?\n")
response = int(input())

cables_avoided = 1
while(cables_avoided <= response):
  print("Avoiding...Done! {} live cables avoided" .format(cables_avoided) )
  cables_avoided += 1

print("\nAll live cables have been avoided")