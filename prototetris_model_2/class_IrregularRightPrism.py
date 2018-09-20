from prototetris_model_2.class_AbstractShape import AbstractShape


class IrregularRightPrism(AbstractShape):
    """A parametric irregular right prism architectural polygon_base

    Prism: two polygons linked by segments
    Irregular: the base polygons of the prism are irregular polygons
    Right: the two polygons are parallel / all linking segments have right angles in the z dimension
    Rationale: such prisms look like simple to manipulate yet very expressive.
    """

    def __init__(self, label, description, circumscribed_shape=None, position=None, *args, **kwargs):
        AbstractShape.__init__(self, label, description, circumscribed_shape, position, *args, **kwargs)
        self.polygon_base = None

    # We will implement here methods to manipulate the prism, e.g.:
    # - split segments,
    # - remove vertices (merge segments),
    # - move points,
    # etc.
    # We will also implement constraints, such as:
    # - polygon segments may not cross each other.
