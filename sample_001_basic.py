from class_shape2d import Shape2D
from class_ground import Ground
from class_building import Building
from class_floor import Floor
from sympy import Polygon


g1 = Ground()
g1.shape = Polygon((0, 0), (100, 0), (100, 50), (0, 50))

b1 = Building()
g1.append_building(b1)

f1 = Floor()
b1.append_floor(f1)

f2 = Floor()
b1.append_floor(f2)