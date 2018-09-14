from class_shape2d import Shape2D
from class_mapobject import MapObject
from class_flat import Flat

"""floor class
"""


class Floor(MapObject, Shape2D):

    def __init__(self, label="A floor", description="", height=4, *args, **kwargs):
        print("Floor constructor")
        MapObject.__init__(self, label, description, *args, **kwargs)
        Shape2D.__init__(self, *args, **kwargs)
        self.height = height

    @property
    def flat_list(self):
        return list(lambda x: isinstance(x, Flat), Shape2D.nested_shape_list)

    def append_building(self, flat):
        Shape2D.append_shape(self, flat)


