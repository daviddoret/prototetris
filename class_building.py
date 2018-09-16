from class_floor import Floor
from class_shape2d import Shape2D
from class_mapobject import MapObject
from fun_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle

"""Building class
"""


class Building(MapObject, Shape2D):

    def __init__(self, label="A building", description="", height=None, *args, **kwargs):
        print("Building constructor")
        MapObject.__init__(self, label, description, *args, **kwargs)
        Shape2D.__init__(self, *args, **kwargs)
        self.height = height

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def floor_list(self):
        return list(lambda x: isinstance(x, Floor), Shape2D.nested_shape_list)

    def append_floor(self, floor):
        Shape2D.append_shape(self, floor)

    def generate_floor(self, floor_number):
        """generate n additional floors in the building,
        providing there is still some available space"""
        if self.floor_height_total() == 0:
            raise ValueError("impossible to generate more floors because there is no space left")
        floor_height = self.free_height_total() / floor_number
        for i in range(floor_number):
            f = Floor()
            f.height = floor_height
            self.append_floor(f)

    @property
    def floor_height_total(self):
        """computes the total height of the building floors"""
        h = 0
        for f in self.floor_list:
            h += f.height
        return h

    @property
    def free_height_total(self):
        """computes the available free height"""
        return self.height - self.floor_height_total()

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.shape, color=(100, 100, 100), altitude=10)
