#aproach 1 using sead
def search(file_name):
  print("Searching... ")
  with open(file_name) as file:
    lines = file.read().split('\n')
    for line in lines:
      print(f"Looked in {line}.")
    print("...Done!")
def run():
  search("data/files/txt/locations.txt")
run()

#aproach 2
def search(file_name):
  print("Searching... ")
  with open(file_name) as file:
    for line in file:
      end_character = line[:-1]

      if(end_character =='\n'):
        print(f"Looked in{line[:-1]}.")
      else:
        print(f"Looked in {line}.")

  print("...Done!")
  
def run():
  search("data/files/txt/locations.txt")
run()