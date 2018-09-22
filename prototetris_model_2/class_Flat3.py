from prototetris_model_2.class_Flat import Flat
from sympy import *


class Flat2(Flat):
    def __init__(
            self,
            label=None,
            circumscribed_shape=None,
            position=Point3D(0, 0, 0),
            *args,
            **kwargs):

        Flat.__init__(
            self,
            label=label,
            description="3 rooms flat",
            circumscribed_shape=circumscribed_shape,
            position=position,
            polygon_base=Polygon((0, 0), (10000, 0), (10000, 600), (0, 600), (0, 0)),
            height=300,  # TODO: WIll be linked to the parent floor's height
            *args,
            **kwargs)