from prototetris_model_2.class_IrregularRightPrism import IrregularRightPrism
from sympy import Polygon


s1 = IrregularRightPrism()
s1.polygon_base = Polygon((0, 0), (100, 0), (100, 80), (0, 80))
print(s1)

s2 = IrregularRightPrism()
s2.polygon_base = Polygon((0, 0), (25, 0), (25, 50), (0, 50))
print(s2)

