def likelihood():
  likelihoods = (50,38,27,99,4)
  return min(likelihoods), max(likelihoods)

def run():
   risk_values = likelihood()
   
   print("Minimum likelihood of falling: {}% ".format(risk_values[0]))
   print("Maximum likelihood of falling: {}%".format(risk_values[1]))
 
run()
