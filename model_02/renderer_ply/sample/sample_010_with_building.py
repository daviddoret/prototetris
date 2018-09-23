from sympy import *
from colorutils import *
from model_02.renderer_ply.fun_point_list_to_ply_vertices import point_list_to_ply_vertices
from model_02.renderer_ply.fun_ply_vertices_list_to_ply_vertices_element import ply_vertices_list_to_ply_vertices_element
from model_02.renderer_ply.fun_ply_face_list_to_ply_face_element import ply_face_list_to_ply_face_element
from model_02.renderer_ply.fun_polygon_list_to_ply_faces import polygon_list_to_ply_faces

from model_02 import *

point_index = 0
f1 = Flat(position=Point3D(0, 0, 0))
ply_vertices_list = point_list_to_ply_vertices(f1.get_point3d_list(), f1.surface_color, None)
print("polygons")
#print(f1.get_polygon_list_by_index(point_index_start=point_index))
ply_face_list = polygon_list_to_ply_faces(f1.get_polygon_list_by_index(point_index_start=point_index), f1.surface_color, None)
point_index = len(ply_vertices_list)

f2 = Flat(position=Point3D(10, 0, 0))
ply_vertices_list = point_list_to_ply_vertices(f2.get_point3d_list(), f2.surface_color, ply_vertices_list)
print("polygons")
#print(f2.get_polygon_list_by_index(point_index_start=point_index))
ply_face_list = polygon_list_to_ply_faces(f2.get_polygon_list_by_index(point_index_start=point_index), f2.surface_color, None)
point_index = len(ply_vertices_list)

ply_vertices_element = ply_vertices_list_to_ply_vertices_element(ply_vertices_list)
ply_face_element = ply_face_list_to_ply_face_element(ply_face_list)

print(ply_vertices_list)
#print(ply_vertices_element)
print(ply_face_list)
#print(len(ply_vertices_list))

PlyData([ply_vertices_element, ply_face_element], text=True).write('sample_010.ply')
