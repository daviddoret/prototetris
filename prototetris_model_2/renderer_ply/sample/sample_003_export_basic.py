from plyfile import *
import numpy

# References:
# - https://github.com/dranjan/python-plyfile

vertex_2 = numpy.array([([0, 0, 0], 255, 0,     0),
                    ([0, 0, 1], 255, 0,   0),
                    ([0, 1, 0], 255, 0,   0),
                    ([0, 1, 1], 255, 0, 0),
                    ([1, 0, 0], 255, 0, 0),
                    ([1, 0, 1], 255, 0, 0),
                    ([1, 1, 0], 255, 0, 0),
                    ([1, 1, 1], 255, 0, 0)],
                   dtype=[('vertex_indices', 'i4', (3,)),
                          ('red', 'u1'), ('green', 'u1'),
                          ('blue', 'u1')])

el = PlyElement.describe(vertex_2, 'vertex')


PlyData([el], text=True).write('sample_003.ply')
