from plyfile import *
import numpy
from colorutils import *


def ply_vertices_list_to_ply_vertices_element(ply_vertices_list):
    ply_numpy_array = numpy.array(ply_vertices_list,
                          dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
                                 ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])
    ply_element = PlyElement.describe(ply_numpy_array, 'vertex')
    return ply_element
