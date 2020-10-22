def directions():
  
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions
def menu():
  print("Please select a direction!")
  dirs = directions()
  for index in range(len(dirs)):
    print("{} : {}" .format(index, dirs[index]))
  direction_index = int(input())
  return dirs[direction_index]

def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    direction = menu()
    route.append(direction)
  print("Escape route : {}".format(route))

run()
