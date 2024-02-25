def planet_disctance():
  Planets = ["Mercury", "Venus", "Earth", "Mars", "jupiter", "Saturn", "Uranus", "Neptune"]
  disctances = [0.39, 0.72, 1.0 , 1.52 , 5.20 , 9.58, 19.18, 30.07]
  for i in range(len(Planets)):
    print(f"{Planets[i]} is {disctances[i]} Astronimical Unit(AU) from the sun")

planet_disctance()
