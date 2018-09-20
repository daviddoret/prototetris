import vtk
from sympy import Polygon


def sympy_polygon_to_vtk_polydata(sympy_polygon, color=None, altitude=None, height=None):
    """References:
    - https://cmake.org/Wiki/VTK/Examples/Python/GeometricObjects/Display/Polygon

    :param sympy_polygon:
    :param vtk_polydata:
    :param color:
    :return:
    """

    vtk_polydata = vtk.vtkPolyData()

    # Setup four points
    points = vtk.vtkPoints()
    points_number = 0
    for p in sympy_polygon.vertices:
        points_number = points_number + 1
        x = float(p.x)
        y = float(p.y)
        z = float(altitude)
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
    vtk_colors.InsertNextTuple3(color[0], color[1], color[2]);

    vtk_polydata.GetCellData().SetScalars(vtk_colors);
    vtk_polydata.Modified()

    return vtk_polydata
