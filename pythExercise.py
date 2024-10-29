import math
c1 = 3
c2 = 5

h = ((3**2) + (5**2))**0.5

print(f"the output that doesn't use the math class is {round(h, 3)}")

h = math.sqrt((c1**2) + (c2**2))
print(f"the output using the math class is {round(h, 3)}")