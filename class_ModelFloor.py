from class_ModelIrregularRightPrism import ModelIrregularRightPrism
from class_ModelAbstractShape import ModelAbstractShape
from class_ModelFlat import ModelFlat
from fun_vtk_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle


"""floor class
"""


class ModelFloor(ModelIrregularRightPrism):

    def __init__(self, label="A floor", description="", altitude=0, height=0, *args, **kwargs):
        ModelIrregularRightPrism.__init__(self, label, description, *args, **kwargs)
        self.altitude = altitude
        self.height = height

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def flat_list(self):
        return list(lambda x: isinstance(x, ModelFlat), ModelIrregularRightPrism.nested_shape_list)

    def append_flat(self, flat):
        ModelIrregularRightPrism.append_shape(self, flat)

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.shape, color=(150, 150, 150), altitude=self.altitude)

