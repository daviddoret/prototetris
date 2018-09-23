from model_02.class_IrregularRightPrism import *
from sympy import *


p = IrregularRightPrism()
p.polygon_base = Polygon((0, 0), (10, 10), (20, 5))
p.height = 15

print(p.get_base_by_index())
print(p.get_top_by_index())
print(p.get_rectangle_by_index(0))
print(p.get_rectangle_by_index(1))
print(p.get_rectangle_by_index(2))
print(p.get_point3d_list())
print("****")
print(p.get_polygon_list_by_index())