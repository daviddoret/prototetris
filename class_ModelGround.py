from class_ModelAbstractShape import ModelAbstractShape
from class_ModelIrregularRightPrism import ModelIrregularRightPrism
from class_ModelBuilding import ModelBuilding
from fun_vtk_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle

"""ModelGround class

The ground surface on which buildings may be built.
"""


class ModelGround(ModelIrregularRightPrism):

    def __init__(self, label="ModelGround", description="", *args, **kwargs):
        ModelIrregularRightPrism.__init__(self, label, description, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def building_list(self):
        return list(lambda x: isinstance(x, ModelBuilding), ModelIrregularRightPrism.nested_shape_list)

    def append_building(self, building, position):
        ModelIrregularRightPrism.append_shape(self, building, position)

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.shape, color=(50, 150, 50), altitude=5)

