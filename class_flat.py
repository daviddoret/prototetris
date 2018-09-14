from class_shape2d import Shape2D
from class_mapobject import MapObject
import jsonpickle

"""Flat class
"""


class Flat(MapObject, Shape2D):

    def __init__(self, label="A flat", description="", *args, **kwargs):
        print("Flat constructor")
        MapObject.__init__(self, label, description, *args, **kwargs)
        Shape2D.__init__(self, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)






