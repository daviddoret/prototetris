from sympy import *


def polygon_to_prism_bottom(polygon2d, z, by_position=False):
    """
    Convert a sympy 2d polygon,
    to its 3d bottom polygon.
    """
    if not by_position:
        point3d_list = list()
        for v in polygon2d.vertices:
            p = Point3D(v.x, v.y, z=z)
            point3d_list.append(p)
        return point3d_list
    else:
        positions = list(range(len(polygon2d.vertices)))
        positions = [i + len(polygon2d.vertices) for i in positions]
        return positions
