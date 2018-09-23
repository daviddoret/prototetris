from sympy import *
from .fun_polygon_to_point3d_list import polygon_to_point3d_list


def polygon_to_irregular_right_prism(polygon2d, height):
    """
    Convert a sympy 2d polygon,
    to a list of surfaces defined by 3-dimensional points,
    that represent an irregular right prism of the desired height.
    """

    z_base = 0
    z_zop = height

    polygons_3d = list()
    # Add the base
    polygons_3d.append(polygon_to_point3d_list(polygon2d, z=z_base))
    # Add the top
    polygons_3d.append(polygon_to_point3d_list(polygon2d, z=z_zop))
    # Add the side rectangles
    for i in range(len(polygon2d.vertices)):
        vertex_a = polygon2d.vertices[i]
        vertex_b = None
        if i == len(polygon2d.vertices) - 1:
            # The last rectangle links back the last vertex with the first vertex.
            vertex_b = polygon2d.vertices[0]
        else:
            vertex_b = polygon2d.vertices[i + 1]
        rectangle3d = list()
        rectangle3d.append(Point3D(vertex_a.x, vertex_a.y, z_base))
        rectangle3d.append(Point3D(vertex_a.x, vertex_a.y, z_zop))
        rectangle3d.append(Point3D(vertex_b.x, vertex_b.y, z_zop))
        rectangle3d.append(Point3D(vertex_b.x, vertex_b.y, z_base))
        rectangle3d.append(Point3D(vertex_a.x, vertex_a.y, z_base))
        polygons_3d.append(rectangle3d)

    return polygons_3d
