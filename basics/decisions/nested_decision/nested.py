print("What type of cover does the book have, hard or soft?")
cover_type = input()

if(cover_type.lower() == "soft"):
  print("\nIs it perfect bound (yes/no)?")
  response = input()
  if(response.lower() =="yes"):
    print("\nSoft cover, perfect bound books are very popular!")
  elif (response.lower() == "no"):
    print("\nSoft covers with coils or stitches are great for short books")
  else:
    print("\nNot shure what you mean")
elif(cover_type.lower() == "hard"):
  print("\nBooks with hard covers can be more expensive!")