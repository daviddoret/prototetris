from class_mapobject import MapObject
from class_shape2d import Shape2D
from class_building import Building
from fun_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle

"""Ground class

The ground surface on which buildings may be built.
"""


class Ground(MapObject, Shape2D):

    def __init__(self, label="Ground", description="", *args, **kwargs):
        print("Ground constructor")
        MapObject.__init__(self, label, description, *args, **kwargs)
        Shape2D.__init__(self, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def building_list(self):
        return list(lambda x: isinstance(x, Building), Shape2D.nested_shape_list)

    def append_building(self, building, position):
        Shape2D.append_shape(self, building, position)

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.shape, color=(50, 150, 50), altitude=5)

