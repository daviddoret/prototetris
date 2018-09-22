from sympy import *


def polygon_to_point3d_list(polygon2d, z):
    """
    Convert a sympy 2d polygon,
    to a list of 3d points.
    """
    point3d_list = list()
    for v in polygon2d.vertices:
        p = Point3D(v.x, v.y, z)
        point3d_list.append(p)
    return point3d_list
