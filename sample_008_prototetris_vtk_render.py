from sympy import Point, Polygon
from class_ModelGround import ModelGround
from class_ModelBuilding import ModelBuilding
from class_ModelFloor import ModelFloor
from fun_vtk_combine_polydata import vtk_combine_polydata
from fun_vtk_render_cleanpolydata import vtk_render_cleanpolydata

g = ModelGround("My land")
g.shape = Polygon((0, 0), (50, -10), (100, 00), (110, 50), (100, 100), (50, 110), (0, 100), (-10, 50), (0, 0))
b = ModelBuilding("My house")
b.shape = Polygon((20, 20), (80, 20), (80, 80), (20, 80), (20, 20))
fb = ModelFloor("Basement", altitude=20)
fb.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f1 = ModelFloor("1st floor", altitude=40)
f1.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f2 = ModelFloor("2nd floor", altitude=60)
f2.shape = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))

p = []
p.append(g.to_vtk_polydata())
p.append(b.to_vtk_polydata())
p.append(fb.to_vtk_polydata())
p.append(f1.to_vtk_polydata())
p.append(f2.to_vtk_polydata())

p_conso = vtk_combine_polydata(p)

vtk_render_cleanpolydata(p_conso)
