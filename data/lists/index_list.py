def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    
    return path
    
def run():
    print("Moving...")
    path = movements()
    #methode without for loop
    #print("{} for {} steps". format(path[0], path[1]))
    #print("{} for {} steps". format(path[2], path[3]))
    #print("{} for {} steps". format(path[4], path[5]))
    #print("{} for {} steps". format(path[6], path[7]))
    for index in range(0, len(path), 2):
     print("{} for {} steps". format(path[index], path[index+1]))
    
run()