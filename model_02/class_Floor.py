from model_02.class_IrregularRightPrism import IrregularRightPrism
from model_02.class_Flat import Flat
from colorutils import *
from sympy import *

"""floor class
"""


class Floor(IrregularRightPrism):

    def __init__(
            self,
            label="Building",
            description=None,
            circumscribed_shape=None,
            position=Point3D(0, 0, 0),
            polygon_base=Polygon((0, 0), (49, 0), (49, 49), (0, 59), (0, 0)),
            height=5,
            *args,
            **kwargs):
        IrregularRightPrism.__init__(
            self,
            label=label,
            description=description,
            circumscribed_shape=circumscribed_shape,
            position=position,
            surface_color=colorutils.Color((80, 80, 150)),
            polygon_base=polygon_base,
            height=height,
            *args,
            **kwargs)

    @property
    def flat_list(self):
        return list(lambda x: isinstance(x, Flat), IrregularRightPrism.nested_shape_list)

    def append_flat(self, flat):
        IrregularRightPrism.append_shape(self, flat)


