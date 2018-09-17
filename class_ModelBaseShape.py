from sympy import Point, Polygon
import jsonpickle

"""ModelBaseShape Class

Base class to represent 2 dimensional shapes.
Basically a wrapper class around sympy Polygon with glue code to make it architecturally friendly.
May be contained in a parent container shape.
May contain children nested shapes.
"""


class ModelBaseShape(object):

    def __init__(self, circumscribed_shape=None, position=None, *args, **kwargs):
        print("Shape2d constructor")
        self.circumscribed_shape = circumscribed_shape
        self.shape = None
        self.inscribed_shape_list = []
        self.position = position

    def __repr__(self):
        return jsonpickle.encode(self)

    # We will add here methods to translate, rotate, resize, split segments, move polygon points, etc.
    # The wrapper class will be useful to apply constraints on the shape,
    # ie if a shape is contained within a shape container, it can't move out of the container,
    # and if collisions are not allowed with sibling shapes, then they are not allowed.

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

