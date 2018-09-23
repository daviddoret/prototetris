import vtk
from sympy import Polygon
from model_02 import *
from colorutils import *


def irregular_right_prism_to_vtk_polydata(prism):
    """References:
    - https://cmake.org/Wiki/VTK/Examples/Python/GeometricObjects/Display/Polygon
    """

    sympy_polygon = prism.polygon_base
    surface_color = prism.surface_color
    base_p = prism.position

    vtk_polydata = vtk.vtkPolyData()

    # Setup four points
    points = vtk.vtkPoints()
    points_number = 0
    for p in sympy_polygon.vertices:
        points_number = points_number + 1
        x = float(p.x)
        y = float(p.y)
        z = float(base_p.z)
        points.InsertNextPoint(x, y, z)

    # Create the polygon
    polygon = vtk.vtkPolygon()
    polygon.GetPointIds().SetNumberOfIds(points_number)  # make a quad
    for i in range(0, points_number):
        polygon.GetPointIds().SetId(i, i)

    # Add the polygon to a list of polygons
    polygons = vtk.vtkCellArray()
    polygons.InsertNextCell(polygon)

    # Create a PolyData
    vtk_polydata.SetPoints(points)
    vtk_polydata.SetPolys(polygons)

    # setup colors (setting the name to "Colors" is nice but not necessary)
    vtk_colors = vtk.vtkUnsignedCharArray();
    vtk_colors.SetNumberOfComponents(3);
    vtk_colors.SetName("Colors");
    vtk_colors.InsertNextTuple3(surface_color.red, surface_color.green, surface_color.blue);

    vtk_polydata.GetCellData().SetScalars(vtk_colors);
    vtk_polydata.Modified()

    return vtk_polydata
