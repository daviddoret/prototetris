from sympy import Polygon
from prototetris_model_2.class_Ground import Ground
from prototetris_model_2.class_Building import Building
from prototetris_model_2.class_Floor import Floor
from prototetris_renderer_vtk.fun_vtk_combine_polydata import vtk_combine_polydata
from prototetris_renderer_vtk.fun_vtk_render_cleanpolydata import vtk_render_cleanpolydata


g = Ground("My land")
g.polygon_base = Polygon((0, 0), (50, -10), (100, 00), (110, 50), (100, 100), (50, 110), (0, 100), (-10, 50), (0, 0))
b = Building("My house")
b.polygon_base = Polygon((20, 20), (80, 20), (80, 80), (20, 80), (20, 20))
fb = Floor("Basement", altitude=20)
fb.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f1 = Floor("1st floor", altitude=40)
f1.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
f2 = Floor("2nd floor", altitude=60)
f2.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))

p = []
p.append(g.to_vtk_polydata())
p.append(b.to_vtk_polydata())
p.append(fb.to_vtk_polydata())
p.append(f1.to_vtk_polydata())
p.append(f2.to_vtk_polydata())

p_conso = vtk_combine_polydata(p)

vtk_render_cleanpolydata(p_conso)
