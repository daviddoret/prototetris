from model_02.class_Flat import Flat
from sympy import *


class Flat1(Flat):
    def __init__(
            self,
            label="Flat",
            description=None,
            circumscribed_shape=None,
            position=None):

        Flat.__init__(
            self,
            label=label,
            description=description,
            circumscribed_shape=circumscribed_shape,
            position=position,
            polygon_base=Polygon((0, 0), (500, 0), (500, 600), (0, 600), (0, 0)),
            height=300)
