print([0]*5)
print(23*19*13*17)

print(100000000/96577)
print(100000000//96577 - 1)
import numpy as np
print(np.prod([0,1,0]))



print(type([0]) == list)
print(type(0) == list)

print(type(0) == int)
print(type([0]) == int)

try:
  print([0,0,0][3])
except IndexError:
  print("unavailable")

print(list("a"))

try:
  x = [0,1,2][1]
except IndexError:
  print("Hi")

print(x)
x = 1
print([x])

print("aaa" + "aaa")