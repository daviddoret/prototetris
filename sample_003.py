from class_ModelIrregularRightPrism import ModelIrregularRightPrism
from sympy import Polygon


s1 = ModelIrregularRightPrism()
s1.shape = Polygon((0, 0), (100, 0), (100, 80), (0, 80))
print(s1)

s2 = ModelIrregularRightPrism()
s2.shape = Polygon((0, 0), (25, 0), (25, 50), (0, 50))
print(s2)

