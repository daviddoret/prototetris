from sympy import Polygon


"""Shape2D Class

Base class to represent 2 dimensional shapes.
Basically a wrapper class around sympy Polygon with glue code to make it architecturally friendly.
May be contained in a parent container shape.
May contain children nested shapes.
"""


class Shape2D(object):

    def __init__(self, *args, **kwargs):
        print("Shape2d constructor")
        self.container_shape = None
        self.shape = None
        self.nested_shape_list = []

    # We will add here methods to translate, rotate, resize, split segments, move polygon points, etc.
    # The wrapper class will be useful to apply constraints on the shape,
    # ie if a shape is contained within a shape container, it can't move out of the container,
    # and if collisions are not allowed with sibling shapes, then they are not allowed.

    def append_shape(self, shape):
        """It is mandatory to use this method to append shapes on parent shapes,
        to guarantee proper referential integrity between parents and children.
        :param shape:
        :return:
        """
        shape.container_shape = self
        self.nested_shape_list.append(shape)
