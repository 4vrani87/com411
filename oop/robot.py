class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"
   # class Attribute
  
  MAX_ENERGY = 100

  # A static method

  def the_laws():
    print(Robot.laws)

  
  # An initialiser (special instance method)
  def __init__(self, name = 'Robot', age = 0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = Robot.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}), energy = {self.energy}'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old and my energy is {self.energy}.'
  
if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  Robot.the_laws()
  print(robot)
  print(repr(robot))