from class_ModelBaseShape import ModelBaseShape
from class_ModelMapObject import ModelMapObject
from class_ModelFlat import ModelFlat
from fun_vtk_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle


"""floor class
"""


class ModelFloor(ModelMapObject, ModelBaseShape):

    def __init__(self, label="A floor", description="", altitude=0, height=0, *args, **kwargs):
        print("ModelFloor constructor")
        ModelMapObject.__init__(self, label, description, *args, **kwargs)
        ModelBaseShape.__init__(self, *args, **kwargs)
        self.altitude = altitude
        self.height = height

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def flat_list(self):
        return list(lambda x: isinstance(x, ModelFlat), ModelBaseShape.nested_shape_list)

    def append_flat(self, flat):
        ModelBaseShape.append_shape(self, flat)

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.shape, color=(150, 150, 150), altitude=self.altitude)

