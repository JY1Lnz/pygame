from vector_2d import vector
import math

p1 = vector.Vector(20, 15)
p2 = vector.Vector(0, 0)

p3 = p1 - p2

print(p3)
print(p1.int())
p1 = p1.unit()
print(p1)
