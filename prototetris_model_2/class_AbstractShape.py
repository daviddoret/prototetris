import jsonpickle
from sympy import Point3D
from colorutils import Color


class AbstractShape(object):
    """The abstract class representing an arbitrary polygon_base in an architectural model.

    This class implement members that are universal to architectural model shapes,
    without any assumption made on how the polygon_base will "look like".
    Sub-classes inheriting from this class are expected to enrich this abstraction
    with a parametric implementation of how the polygon_base "looks like".
    This abstraction layer opens the door to future extensions
    with different shapes than the basic prisms we intend to implement first.
    """

    def __init__(
            self,
            label="Shape",
            description=None,
            circumscribed_shape=None,
            inscribed_shape_list=[],
            position=Point3D(0, 0, 0),
            surface_color=Color((200, 200, 200)),
            *args,
            **kwargs):

        self.label = label
        self.description = description
        self.circumscribed_shape = circumscribed_shape
        self.inscribed_shape_list = inscribed_shape_list
        self.position = position
        self.surface_color = surface_color

    def __repr__(self):
        return jsonpickle.encode(self)

    # We will add here methods to translate, rotate, (and possibly resize?) the polygon_base.
    # We should also implement constraints, such as:
    # - an inscribed polygon_base can't move out of its circumscribed polygon_base.
    # - some shapes should not be allowed to collision (overlap).

    def append_shape(self, shape, position=Point3D(0, 0, 0)):
        """It is mandatory to use this method to append shapes on parent shapes,
        to guarantee proper referential integrity between parents and children.
        """
        shape.container_shape = self
        shape.position = position
        self.inscribed_shape_list.append(shape)
