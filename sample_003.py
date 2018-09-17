from class_ModelBaseShape import ModelBaseShape
from sympy import Polygon


s1 = ModelBaseShape()
s1.shape = Polygon((0, 0), (100, 0), (100, 80), (0, 80))
print(s1)

s2 = ModelBaseShape()
s2.shape = Polygon((0, 0), (25, 0), (25, 50), (0, 50))
print(s2)

