from plyfile import *
import numpy
from colorutils import *


def polygon_list_to_ply_faces(polygon_list, color, ply_face_list):
    """
    References:
     - https://github.com/dranjan/python-plyfile
    """
    if ply_face_list is None:
        ply_face_list = list()
        print("list created")
    for p in polygon_list:
        ply_tuple = (
            list(p),
            color.red, color.green, color.blue)
        ply_face_list.append(ply_tuple)
    # print(ply_face_list)
    return ply_face_list
