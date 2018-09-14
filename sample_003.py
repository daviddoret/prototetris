from class_shape2d import Shape2D
from sympy import Polygon


s1 = Shape2D()
s1.shape = Polygon((0, 0), (100, 0), (100, 80), (0, 80))
print(s1)

s2 = Shape2D()
s2.shape = Polygon((0, 0), (25, 0), (25, 50), (0, 50))
print(s2)

