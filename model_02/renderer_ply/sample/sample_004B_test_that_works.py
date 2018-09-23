from plyfile import *
import numpy

# References:
# - https://github.com/dranjan/python-plyfile

vertex = numpy.array([(0, 0, 0, 255, 0, 0),
                       (0, 1, 1, 255, 0, 0),
                       (1, 0, 1, 255, 0, 0),
                       (1, 1, 0, 255, 0, 0)],
                      dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
                             ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])

face = numpy.array(
    [
        ([0, 1, 2, 3], 255, 0,     0),
        ([4, 5, 6, 7], 255, 0,   0)
    ],
                   dtype=[('vertex_indices', 'i4', (4,)),
                          ('red', 'u1'), ('green', 'u1'),
                          ('blue', 'u1')])

face2 = numpy.array(
    [
        ([0, 1, 2], 255, 255,     0),
        ([4, 5, 6], 255, 255,   0)
    ],
                   dtype=[('vertex_indices', 'i4', (3,)),
                          ('red', 'u1'), ('green', 'u1'),
                          ('blue', 'u1')])


#face3 = numpy.append(face, ([0, 1, 2], 255, 255,     0))
el = PlyElement.describe(vertex, 'vertex')
e2 = PlyElement.describe(face2, 'face')
#e3 = PlyElement.describe()

PlyData([el, e2], text=True).write('sample_004.ply')

print("PLYDATA")
print(PlyData([el, e2], text=True))