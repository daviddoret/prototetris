from prototetris_model_2.class_Floor import Floor
from prototetris_model_2.class_IrregularRightPrism import IrregularRightPrism
from colorutils import *
from sympy import *

"""Building class
"""


class Building(IrregularRightPrism):

    def __init__(
            self,
            label="Building",
            description=None,
            circumscribed_shape=None,
            position=Point3D(0, 0, 0),
            polygon_base=Polygon((0, 0), (50, 0), (50, 50), (0, 50), (0, 0)),
            height=100,
            *args,
            **kwargs):
        IrregularRightPrism.__init__(
            self,
            label=label,
            description=description,
            circumscribed_shape=circumscribed_shape,
            position=position,
            surface_color=colorutils.Color((100, 100, 100)),
            polygon_base=polygon_base,
            height=height,
            *args,
            **kwargs)

    @property
    def floor_list(self):
        return list(lambda x: isinstance(x, Floor), IrregularRightPrism.nested_shape_list)

    def append_floor(self, floor):
        IrregularRightPrism.append_shape(self, floor)

    def generate_floor(self, floor_number):
        """generate n additional floors in the building,
        providing there is still some available space"""
        if self.floor_height_total() == 0:
            raise ValueError("impossible to generate more floors because there is no space left")
        floor_height = self.free_height_total() / floor_number
        for i in range(floor_number):
            f = Floor(
                label="f" + i,
                position=Point3D(0, 0, i * floor_height)
            )
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
