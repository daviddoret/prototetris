from prototetris_model_2.class_AbstractShape import AbstractShape
from .fun_polygon_to_irregular_right_prism import polygon_to_irregular_right_prism
from .fun_polygon_to_point3d_list import polygon_to_point3d_list
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

    def get_polygon3d_list(self):
        """
        Returns the list of 3d polygons
        that represent the prism surfaces.
        """
        return polygon_to_irregular_right_prism(self.polygon_base, self.height)

    def get_base_by_position(self):
        return polygon_to_point3d_list(self.polygon_base, z=self.position.z)

    def get_top_by_position(self):
        return polygon_to_point3d_list(self.polygon_base, z=self.position.z + self.height)

    def get_base_by_index(self):
        return list(range(0, len(self.polygon_base.vertices)))

    def get_top_by_index(self):
        return list(range(len(self.polygon_base.vertices), 2 * len(self.polygon_base.vertices)))

    def get_rectangle_by_index(self, rectangle_index):
        if rectangle_index < len(self.polygon_base.vertices) - 1:
            return (rectangle_index,
                    rectangle_index + 1,
                    rectangle_index + 1 + len(self.polygon_base.vertices),
                    rectangle_index + len(self.polygon_base.vertices),
                    rectangle_index)
        elif rectangle_index == len(self.polygon_base.vertices) - 1:
            return (rectangle_index,
                    0,
                    len(self.polygon_base.vertices),
                    2 * len(self.polygon_base.vertices) - 1,
                    rectangle_index)

    def get_polygon_list_by_index(self):
        polygon_list = list()
        polygon_list.append(self.get_base_by_index())
        polygon_list.append(self.get_top_by_index())
        for rectangle_index in range(0, len(self.polygon_base.vertices)):
            polygon_list.append(self.get_rectangle_by_index(rectangle_index))
        return polygon_list


    def get_point3d_list(self):
        """Returns a list of unique 3d points"""
        return self.get_base_by_position() + self.get_top_by_position()

    def get_polygon3d_by_position_list(self):
        """Returns the 3d polygons by point position references,
        this is the format required by vtk."""

        # Add the base
        polygons_3d.append(list(range(0, len(self.polygon_base))))
        # Add the top
        polygons_3d.append(list(range(0, len(self.polygon_base))))
        # Add the side rectangles
        for i in range(len(polygon2d.vertices)):
            vertex_a = polygon2d.vertices[i]
            vertex_b = None
            if i == len(polygon2d.vertices) - 1:
                # The last rectangle links back the last vertex with the first vertex.
                vertex_b = polygon2d.vertices[0]
            else:
                vertex_b = polygon2d.vertices[i + 1]
            rectangle3d = list()
            rectangle3d.append(Point3D(vertex_a.x, vertex_a.y, z_base))
            rectangle3d.append(Point3D(vertex_a.x, vertex_a.y, z_zop))
            rectangle3d.append(Point3D(vertex_b.x, vertex_b.y, z_zop))
            rectangle3d.append(Point3D(vertex_b.x, vertex_b.y, z_base))
            rectangle3d.append(Point3D(vertex_a.x, vertex_a.y, z_base))
            polygons_3d.append(rectangle3d)

