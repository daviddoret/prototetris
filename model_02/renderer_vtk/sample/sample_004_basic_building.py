from sympy import *
from model_02 import *
from model_02.renderer_vtk import *


g = Plan("My land")
g.polygon_base = Polygon((0, 0), (50, -10), (100, 00), (110, 50), (100, 100), (50, 110), (0, 100), (-10, 50), (0, 0))
b = Building("My house")
b.polygon_base = Polygon((20, 20), (80, 20), (80, 80), (20, 80), (20, 20))
fb = Floor("Basement", position=Point3D(0, 0, 20))
fb.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f1 = Floor("1st floor", position=Point3D(0, 0, 40))
f1.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f2 = Floor("2nd floor", position=Point3D(0, 0, 60))
f2.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))

p = []
p.append(irregular_right_prism_to_polydata(g))
p.append(irregular_right_prism_to_polydata(b))
p.append(irregular_right_prism_to_polydata(fb))
p.append(irregular_right_prism_to_polydata(f1))
p.append(irregular_right_prism_to_polydata(f2))
p_conso = combine_polydata(p)

render_cleanpolydata(p_conso)
