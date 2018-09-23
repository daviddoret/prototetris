from plyfile import *
import numpy
from colorutils import *


def ply_face_list_to_ply_face_element(ply_face_list, vertices_number):
    print("ply_face_list")
    print(ply_face_list)
    ply_numpy_array = numpy.array(ply_face_list,
                           dtype=[('vertex_indices', 'i4', (vertices_number,)),
                                  ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])

    ply_element = PlyElement.describe(ply_numpy_array, 'face')
    return ply_element
