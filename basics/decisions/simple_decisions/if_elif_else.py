print("Towards which direction should I paint (up, down, left or right)?")

response =input()

if( response.lower() == "up"):
 print("I am painting in the upward direction")
elif(response.lower() == "down"):
 print("I am painting in the downward direction")
elif(response.lower() == "left"):
 print("I am painting in the leftward direction")
elif(response.lower() =="right"):
 print("I am painting in the rightward direction")
else:
  print("Invalid input")