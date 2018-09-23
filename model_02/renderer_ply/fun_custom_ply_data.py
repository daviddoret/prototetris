from plyfile import *
import numpy
from colorutils import *

from model_02.renderer_ply.fun_point_list_to_ply_vertices import point_list_to_ply_vertices
from model_02.renderer_ply.fun_ply_vertices_list_to_ply_vertices_element import ply_vertices_list_to_ply_vertices_element
from model_02.renderer_ply.fun_ply_face_list_to_ply_face_element import ply_face_list_to_ply_face_element
from model_02.renderer_ply.fun_polygon_list_to_ply_faces import polygon_list_to_ply_faces
from model_02 import *


def custom_ply_data(prism_list):
    """
    References:
     - https://github.com/dranjan/python-plyfile
    """

    point_list = list()
    polygon_list = list()

    ply_point_text = ""
    ply_polygon_text = ""

    for prism in prism_list:
        point_index = len(point_list)
        prism_point_list = prism.get_point3d_list()
        prism_polygon_list = prism.get_polygon_list_by_index(point_index)

        for prism_point in prism_point_list:
            ply_line = "\n{} {} {} {} {} {}".format(prism_point.x, prism_point.y, prism_point.z,
                                                    prism.surface_color.red, prism.surface_color.green, prism.surface_color.blue)
            ply_point_text = ply_point_text + ply_line

        point_list = point_list + prism_point_list

        for prism_polygon in prism_polygon_list:
           ply_line = "\n{}".format(len(prism_polygon_list)) # The first number in PLY is the number of vertices in the polygon
           for prism_polygon_point_index in prism_polygon:
               ply_line = "{} {}".format(ply_line, prism_polygon_point_index)
           ply_polygon_text = ply_polygon_text + ply_line

        polygon_list = polygon_list + prism_polygon_list

    ply_header = """ply
format ascii 1.0
element vertex {}
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
element face {}
property list uchar int vertex_indices
property uchar red
property uchar green
property uchar blue
end_header""".format(len(point_list), len(polygon_list))

    return ply_header + ply_point_text + ply_polygon_text
