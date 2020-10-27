def observed():
  obeservations = []
  for count in range(7):
    print("Please enter an observation:")
    item = input()
    obeservations.append(item)
  
  return obeservations
  
def run():
  print("Counting observation...")
  observations = observed()
  observations_set  = set()

  for observation in observations:
    occurrences = observations.count(observation)
    observations_set.add((observation, occurrences))

  for key, value in observations_set:
    print(f"{key} observed {occurrences} times. ")

run()