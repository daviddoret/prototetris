from prototetris_model_2.class_AbstractShape import AbstractShape
from .fun_polygon_to_irregular_right_prism import polygon_to_irregular_right_prism
from sympy import *
from colorutils import *


class IrregularRightPrism(AbstractShape):
    """A parametric irregular right prism architectural polygon_base

    Prism: two polygons linked by segments
    Irregular: the base polygons of the prism are irregular polygons
    Right: the two polygons are parallel / all linking segments have right angles in the z dimension
    Rationale: such prisms look like simple to manipulate yet very expressive.
    """

    def __init__(
            self,
            label="Irregular Right Prism",
            description=None,
            circumscribed_shape=None,
            position=Point3D(0, 0, 0),
            surface_color=Color((200, 200, 200)),
            polygon_base=Polygon((0, 0), (5, 0), (5, 5), (0, 5), (0, 0)),
            height=3,
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

    def get_polygons3d(self):
        """
        Returns the list of 3d polygons
        that represent the prism surfaces.
        """
        return polygon_to_irregular_right_prism(self.polygon_base, self.height)



