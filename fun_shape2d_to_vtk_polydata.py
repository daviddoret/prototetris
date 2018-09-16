import vtk
from sympy import Polygon
from class_ground import Ground


def sympy_polygon_to_vtk_polydata(sympy_polygon, vtk_polydata=None):
    """References:
    - https://cmake.org/Wiki/VTK/Examples/Python/GeometricObjects/Display/Polygon

    :param sympy_polygon:
    :param vtk_polydata:
    :return:
    """

    if vtk_polydata is None:
        # If the VTK Polydata object was not provided,
        # we assume this is the first object to be created
        # so we instanciate the polydata object.
        vtk_polydata = vtk.vtkPolyData()

    # Setup four points
    points = vtk.vtkPoints()
    points_number = 0
    for p in sympy_polygon.vertices:
        points_number = points_number + 1
        x = float(p.x)
        y = float(p.y)
        z = float(0.0)
        points.InsertNextPoint(x, y, z)

    # Create the polygon
    polygon = vtk.vtkPolygon()
    polygon.GetPointIds().SetNumberOfIds(points_number)  # make a quad
    for i in range(0, points_number - 1):
        polygon.GetPointIds().SetId(i, i)

    # Add the polygon to a list of polygons
    polygons = vtk.vtkCellArray()
    polygons.InsertNextCell(polygon)

    # Create a PolyData
    vtk_polydata.SetPoints(points)
    vtk_polydata.SetPolys(polygons)

    return vtk_polydata
