from model_02.class_IrregularRightPrism import IrregularRightPrism
from model_02.class_Building import Building
from colorutils import *
from sympy import *

"""Plan class

The ground surface on which buildings may be built.
"""


class Plan(IrregularRightPrism):

    def __init__(
            self,
            label="Plan",
            description=None,
            circumscribed_shape=None,
            position=None,
            polygon_base=Polygon((0, 0), (100, 0), (100, 100), (0, 100), (0, 0)),
            height=10):
        IrregularRightPrism.__init__(
            self,
            label=label,
            description=description,
            circumscribed_shape=circumscribed_shape,
            position=position,
            surface_color=colorutils.Color((80, 150, 80)),
            polygon_base=polygon_base,
            height=height)

    @property
    def building_list(self):
        return list(lambda x: isinstance(x, Building), IrregularRightPrism.nested_shape_list)

    def append_building(self, building, position):
        IrregularRightPrism.append_shape(self, building, position)


