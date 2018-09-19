from class_ModelAbstractShape import ModelAbstractShape
from sympy import Point, Polygon
import jsonpickle


class ModelIrregularRightPrism(ModelAbstractShape):
    """A parametric irregular right prism architectural shape

    Prism: two polygons linked by segments
    Irregular: the base polygons of the prism are irregular polygons
    Right: the two polygons are parallel / all linking segments have right angles in the z dimension
    Rationale: such prisms look like simple to manipulate yet very expressive.
    """

    def __init__(self, label, description, circumscribed_shape=None, position=None, *args, **kwargs):
        ModelAbstractShape.__init__(self, label, description, circumscribed_shape, position, *args, **kwargs)
        self.shape = None

    # We will implement here methods to manipulate the prism, e.g.:
    # - split segments,
    # - remove vertices (merge segments),
    # - move points,
    # etc.
    # We will also implement constraints, such as:
    # - polygon segments may not cross each other.
