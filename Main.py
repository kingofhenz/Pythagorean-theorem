while True:
  print("Pythagorean Theorum:")
  solve = input("Would you like to solve for 'a', 'b', or 'c'? ")

  if solve == "a" or solve == "A":
      b = float(input("Input 'b' value: "))
      c = float(input("Input 'c' value: "))
      print("a = ", ((c**2 - b**2)**(1/2)))

    if solve == "b" or solve == "B":
        a = float(input("Input 'a' value: "))
        c = float(input("Input 'c' value: "))
        print("b = ", ((c**2 - a**2)**(1/2)))

    if solve == "c" or solve == "C":
        a = float(input("Input 'a' value: "))
        b = float(input("Input 'b' value: "))
        print("c = ", ((a**2 + b**2)**(1/2)))

    if solve != "a" and solve != "A" and solve_for != "b" and solve_for != "B" and solve_for != "c" and solve_for != "C":
        print("error")
