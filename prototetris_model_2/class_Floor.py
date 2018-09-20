from prototetris_model_2.class_IrregularRightPrism import IrregularRightPrism
from prototetris_model_2.class_Flat import Flat
from prototetris_renderer_vtk.fun_vtk_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle


"""floor class
"""


class Floor(IrregularRightPrism):

    def __init__(self, label="A floor", description="", altitude=0, height=0, *args, **kwargs):
        IrregularRightPrism.__init__(self, label, description, *args, **kwargs)
        self.altitude = altitude
        self.height = height

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def flat_list(self):
        return list(lambda x: isinstance(x, Flat), IrregularRightPrism.nested_shape_list)

    def append_flat(self, flat):
        IrregularRightPrism.append_shape(self, flat)

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.polygon_base, color=(150, 150, 150), altitude=self.altitude)

