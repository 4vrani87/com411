def escape_by(plan):
  if (plan == "jumping over"):
    print("\nWe cannot escape that way! The boulder is too big")
  elif ( plan == "runnig around"):
    print("\nWe cannot escape that way! the boulder is moving too fast")
  elif( plan == "going deeper"):
    print("\nThat might just work! Let's go deeper!")
  else:
    print("\nwe cannot escape that way! the boulder is in the way")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")