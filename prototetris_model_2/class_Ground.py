from prototetris_model_2.class_IrregularRightPrism import IrregularRightPrism
from prototetris_model_2.class_Building import Building
from prototetris_renderer_vtk.fun_vtk_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle

"""Ground class

The ground surface on which buildings may be built.
"""


class Ground(IrregularRightPrism):

    def __init__(self, label="Ground", description="", *args, **kwargs):
        IrregularRightPrism.__init__(self, label, description, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def building_list(self):
        return list(lambda x: isinstance(x, Building), IrregularRightPrism.nested_shape_list)

    def append_building(self, building, position):
        IrregularRightPrism.append_shape(self, building, position)

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.polygon_base, color=(50, 150, 50), altitude=5)

