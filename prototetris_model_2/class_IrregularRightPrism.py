from prototetris_model_2.class_AbstractShape import AbstractShape
from sympy import *


class IrregularRightPrism(AbstractShape):
    """A parametric irregular right prism architectural polygon_base

    Prism: two polygons linked by segments
    Irregular: the base polygons of the prism are irregular polygons
    Right: the two polygons are parallel / all linking segments have right angles in the z dimension
    Rationale: such prisms look like simple to manipulate yet very expressive.
    """

    def __init__(
            self,
            label="Prism",
            description=None,
            circumscribed_shape=None,
            position=Point3D(0, 0, 0),
            surface_color=None,
            polygon_base=Polygon((0, 0), (5, 0), (5, 5), (0, 5), (0, 0)),
            height=None,
            *args,
            **kwargs):
        AbstractShape.__init__(
            self,
            label=label,
            description=description,
            circumscribed_shape=circumscribed_shape,
            position=position,
            surface_color=surface_color,
            *args,
            **kwargs)
        self.polygon_base = polygon_base
        self.height = height

    # We will implement here methods to manipulate the prism, e.g.:
    # - split segments,
    # - remove vertices (merge segments),
    # - move points,
    # etc.
    # We will also implement constraints, such as:
    # - polygon segments may not cross each other.
