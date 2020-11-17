import matplotlib.pyplot as plt

def coordinates():
  print("Please enter an X value!")
  x = int(input())
  print("Please enter an Y value!")
  y = int(input())
  return (x, y)

def path():
  print("Retrieving path...")
  x_value = []
  y_value = []
  for count in range(4):
    data = coordinates()
    x_value.append(data[0])
    y_value.append(data[1])
  return(x_value, y_value)

def run():
  values = path()
  plt.plot(values[0], values[1], "r--o")
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.show()
  
run()
