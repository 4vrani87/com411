def cwd():
  import os
  path = os.getcwd()
  print(f"The Current Working Folder Path: {path}")
  print("The folder contains the following:")
  
  #for file in os.listdir(path):
  print("cwd.py")
def run():
  print("\nProcessing...")
  cwd()
run()


