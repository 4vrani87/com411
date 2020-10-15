print("\n\nBeep is looking for his spare battery.")
print("\nWhere should I look?")
print("""
Answers to try:
-in the bedroom
-in the bathroom
-in the lab""")

answer = input()
if(answer.lower() == "in the bedroom"):
 print("Where in the bedroom should I look?")
 answer=input()
 if(answer.lower() == "under the bed"):
  print("Found some shoes but no battery")
 else:
   print("found some mess but no battery.")

elif(answer.lower() == "in the bathroom"):
  print("where in the bathroom should I look?")
  answer= input()
  if(answer.lower() == "in the bathtube"):
    print("Found a rubber duck but no battery")
  else:
    print("found a wet sourface but no battery")

elif(answer.lower() == "in the lab"):
  print("Where in the lab shoul I look?")
  answer = input()
  if(answer.lower() == "on the table"):
    print("Yes! I found my battery")
  else:
    print("Found some tools but no battery.")

else:
  print("I do not know where that is but I will keep looking")