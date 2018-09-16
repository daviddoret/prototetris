from sympy import Point, Polygon
from class_ground import Ground
from class_building import Building
from class_floor import Floor
import vtk
from fun_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
from fun_combine_vtk_polydata import combine_vtk_polydata
from fun_render_vtk_cleanpolydata import render_vtk_cleanpolydata

g = Ground("My land")
g.shape = Polygon((0, 0), (50, -10), (100, 00), (110, 50), (100, 100), (50, 110), (0, 100), (-10, 50), (0, 0))
b = Building("My house")
b.shape = Polygon((20, 20), (80, 20), (80, 80), (20, 80), (20, 20))
fb = Floor("Basement", altitude=20)
fb.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f1 = Floor("1st floor", altitude=40)
f1.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f2 = Floor("2nd floor", altitude=60)
f2.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))

p = []
p.append(g.to_vtk_polydata())
p.append(b.to_vtk_polydata())
p.append(fb.to_vtk_polydata())
p.append(f1.to_vtk_polydata())
p.append(f2.to_vtk_polydata())

p_conso = combine_vtk_polydata(p)

render_vtk_cleanpolydata(p_conso)
