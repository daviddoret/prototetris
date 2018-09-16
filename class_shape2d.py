import vtk
from vtk.util.colors import tomato # The colors module defines various useful colors.
from sympy import Point, Polygon
import jsonpickle

"""Shape2D Class

Base class to represent 2 dimensional shapes.
Basically a wrapper class around sympy Polygon with glue code to make it architecturally friendly.
May be contained in a parent container shape.
May contain children nested shapes.
"""


class Shape2D(object):

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

    def to_vtk(self):
        # Setup four points
        points = vtk.vtkPoints()
        points_number = 0
        for p in self.shape.vertices:
            points_number += 1
            x = float(p.x)
            y = float(p.y)
            z = float(0)
            print("p({},{},{})".format(x, y, z))
            points.insertNextPoint(x, y, z)

        # Create the polygon
        polygon = vtk.vtkPolygon()
        polygon.GetPointIds().SetNumberOfIds(points_number)  # make a quad
        for i in range(0, points_number - 1):
            polygon.GetPointIds().SetId(i, i)

        # Add the polygon to a list of polygons
        polygons = vtk.vtkCellArray()
        polygons.InsertNextCell(polygon)

        # Create a PolyData
        polygonPolyData = vtk.vtkPolyData()
        polygonPolyData.SetPoints(points)
        polygonPolyData.SetPolys(polygons)

        # Create a mapper and actor
        mapper = vtk.vtkPolyDataMapper()
        if vtk.VTK_MAJOR_VERSION <= 5:
            mapper.SetInput(polygonPolyData)
        else:
            mapper.SetInputData(polygonPolyData)

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Visualize
        renderer = vtk.vtkRenderer()
        renderWindow = vtk.vtkRenderWindow()
        renderWindow.AddRenderer(renderer)
        renderWindowInteractor = vtk.vtkRenderWindowInteractor()
        renderWindowInteractor.SetRenderWindow(renderWindow)

        renderer.AddActor(actor)
        renderer.SetBackground(.5, .3, .31)  # Background color salmon

        renderWindow.Render()
        renderWindowInteractor.Start()