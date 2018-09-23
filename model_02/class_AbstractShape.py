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

        self.circumscribed_shape = None
        if circumscribed_shape is not None:
            circumscribed_shape.append_shape(self)

        self.inscribed_shape_list = list()
        if inscribed_shape_list is not None:
            for inscribed_shape in inscribed_shape_list:
                self.append_shape(inscribed_shape)

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
        shape.circumscribed_shape = self
        shape.position = position
        self.inscribed_shape_list.append(shape)

    def get_flattened_shape_list(self):
        """Returns a list containing this shape
        + all its inscribed shapes
        + all their inscribed shapes
        + ... until there are no more shapes left."""
        flattened_shape_list = list()
        flattened_shape_list.append(self)
        for inscribed_shape in self.inscribed_shape_list:
            flattened_shape_list = flattened_shape_list + inscribed_shape.get_flattened_shape_list()
        return flattened_shape_list

    def get_flattened_point3d_list_with_polygon_by_index_list(self):
        """Returns a dictionary with 2 components:
        - point3d_list: an ordered list of vertices (Point3D) with standard index from 0 to n
        - polygon_by_index_list: a list of polygons composed a list of n tuples whose value correspond to the point3d index above
        Assumption: the .get_point3d_list() method must be implemented by all children classes.
        This "flattened" with polygons "by index" data structure may be useful
        to simplify exportation of data in certain 3d formats, such as PLY."""

        flattened_shape_list = self.get_flattened_shape_list()

        point3d_list = list()
        polygon_by_index_list = list()

        for prism in flattened_shape_list:
            point_index = len(point3d_list)
            prism_point_list = prism.get_point3d_list()
            prism_polygon_list = prism.get_polygon_list_by_index(point_index)
            point3d_list = point3d_list + prism_point_list
            polygon_by_index_list = polygon_by_index_list + prism_polygon_list

        output_structure = dict(
            point3d_list=point3d_list,
            polygon_by_index_list=polygon_by_index_list)

        return output_structure
