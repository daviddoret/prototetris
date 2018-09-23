from sympy import *
from colorutils import *
from model_02.renderer_ply.fun_point_list_to_ply_vertices import point_list_to_ply_vertices
from model_02.renderer_ply.fun_ply_vertices_list_to_ply_vertices_element import ply_vertices_list_to_ply_vertices_element

l = list()
l.append(Point3D(0, 0, 0))
l.append(Point3D(0, 10, 0))
l.append(Point3D(0, 0, 30))

c1 = Color((10,10,10))
c2 = Color((255,10,10))

#print(l)

ply_vertices_list = point_list_to_ply_vertices(l, c1, None)
ply_vertices_list = point_list_to_ply_vertices(l, c2, ply_vertices_list)
ply_vertices_element = ply_vertices_list_to_ply_vertices_element(ply_vertices_list)

print(ply_vertices_list)
print(ply_vertices_element)
