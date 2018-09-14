from class_mapobject import MapObject
from class_shape2d import Shape2D
from class_building import Building

"""Ground class

The ground surface on which buildings may be built.
"""


class Ground(MapObject, Shape2D):

    def __init__(self, label="Ground", description="", *args, **kwargs):
        print("Ground constructor")
        MapObject.__init__(self, label, description, *args, **kwargs)
        Shape2D.__init__(self, *args, **kwargs)

    @property
    def building_list(self):
        return list(lambda x: isinstance(x, Building), Shape2D.nested_shape_list)

    def append_building(self, building):
        Shape2D.append_shape(self, building)


