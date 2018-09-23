from plyfile import *
import numpy
from colorutils import *


def point_list_to_ply_vertices(Point3D_list, color, ply_vertices_list):
    """
    References:
     - https://github.com/dranjan/python-plyfile
    """
    if ply_vertices_list is None:
        ply_vertices_list = list()
        print("list created")
    for p in Point3D_list:
        ply_tuple = (
            p.x, p.y, p.z,
            color.red, color.green, color.blue)
        ply_vertices_list.append(ply_tuple)
    # print(ply_vertices_list)
    return ply_vertices_list

