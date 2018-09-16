from sympy import Point, Polygon
from class_ground import Ground
from class_building import Building
from class_floor import Floor
import vtk
from fun_shape2d_to_vtk_polydata import sympy_polygon_to_vtk_polydata
from fun_combine_vtk_polydata import combine_vtk_polydata
from fun_render_vtk_cleanpolydata import render_vtk_cleanpolydata

g = Ground("My land")
g.shape = Polygon((0, 0), (50, -10), (100, 00), (110, 50), (100, 100), (50, 100), (50, 110), (0, 100), (-10, 50), (0,0))
b = Building("My house")
b.shape = Polygon((20, 20), (80, 20), (80, 80), (20, 80), (20, 20))
f = Floor("Basement")
f.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))

p1 = sympy_polygon_to_vtk_polydata(g.shape)
p2 = sympy_polygon_to_vtk_polydata(b.shape)
p3 = sympy_polygon_to_vtk_polydata(f.shape)

p_conso = combine_vtk_polydata(p1, p2, p3)

render_vtk_cleanpolydata(p_conso)
