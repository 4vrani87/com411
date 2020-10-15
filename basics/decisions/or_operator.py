print("What type of adventure should I have?")
print("""
-short
-scary
-safe
-long
""")
adventure_type = input()

if(adventure_type == "scary" or adventure_type == "short"):
  print("Taking the short route")
elif(adventure_type == "safe" or adventure_type == "long"):
  print("Taking the long route")
else:
  print("Not sure what type of adventure you want")