from model_02.class_IrregularRightPrism import IrregularRightPrism
from colorutils import *
from sympy import *

"""Flat class
"""


class Flat(IrregularRightPrism):

    def __init__(
            self,
            label="Flat",
            description=None,
            circumscribed_shape=None,
            position=Point3D(0, 0, 0),
            polygon_base=Polygon((0, 0), (10, 0), (10, 10), (0, 10), (0, 0)),
            height=4,
            *args,
            **kwargs):
        IrregularRightPrism.__init__(
            self,
            label=label,
            description=description,
            circumscribed_shape=circumscribed_shape,
            position=position,
            surface_color=colorutils.Color((150, 80, 80)),
            polygon_base=polygon_base,
            height=height,
            *args,
            **kwargs)







