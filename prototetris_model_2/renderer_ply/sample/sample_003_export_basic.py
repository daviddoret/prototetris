from plyfile import *
import numpy

# References:
# - https://github.com/dranjan/python-plyfile

vertex = numpy.array([(0, 0, 0),
                      (0, 1, 1),
                      (1, 0, 1),
                      (1, 1, 0)],
                     dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])

face = numpy.array([([0, 1, 2], 255, 255, 255),
                    ([0, 2, 3], 255,   0,   0),
                    ([0, 1, 3],   0, 255,   0),
                    ([1, 2, 3],   0,   0, 255)],
                   dtype=[('vertex_indices', 'i4', (3,)),
                          ('red', 'u1'), ('green', 'u1'),
                          ('blue', 'u1')])

el = PlyElement.describe(vertex, 'my_vertices')

e2 = PlyElement.describe(vertex, 'my_faces')


# el = PlyElement.describe(some_array, 'some_name',
#                          comments=['comment1',
#                                    'comment2'])

# el = PlyElement.describe(some_array, 'some_name',
#                          val_dtypes={'some_property': 'f8'},
#                          len_dtypes={'some_property': 'u4'})

# PlyData([el]).write('some_binary.ply')
PlyData([el, e2], text=True).write('sample_003.ply')
# PlyData([el], byte_order='>').write('some_big_endian_binary.ply')
