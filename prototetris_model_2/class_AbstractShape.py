import jsonpickle


class AbstractShape(object):
    """The abstract class representing an arbitrary polygon_base in an architectural model.

    This class implement members that are universal to architectural model shapes,
    without any assumption made on how the polygon_base will "look like".
    Sub-classes inheriting from this class are expected to enrich this abstraction
    with a parametric implementation of how the polygon_base "looks like".
    This abstraction layer opens the door to future extensions
    with different shapes than the basic prisms we intend to implement first.

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)
    """

    def __init__(
            self,
            label=None,
            description=None,
            circumscribed_shape=None,
            inscribed_shape_list=[],
            position=None,
            *args,
            **kwargs):

        self.label = label
        self.description = description
        self.circumscribed_shape = circumscribed_shape
        self.inscribed_shape_list = inscribed_shape_list
        self.position = position

    def __repr__(self):
        return jsonpickle.encode(self)

    # We will add here methods to translate, rotate, (and possibly resize?) the polygon_base.
    # We should also implement constraints, such as:
    # - an inscribed polygon_base can't move out of its circumscribed polygon_base.
    # - some shapes should not be allowed to collision (overlap).

    def append_shape(self, shape, position=None):
        """It is mandatory to use this method to append shapes on parent shapes,
        to guarantee proper referential integrity between parents and children.
        :param shape:
        :param position:
        :return:
        """
        if position is None:
            position = Point(0, 0)
        shape.container_shape = self
        shape.position = position
        self.inscribed_shape_list.append(shape)
