# SOURCE: https://cmake.org/Wiki/VTK/Examples/Python/GeometricObjects/Display/Polygon

import vtk
from sympy import Polygon
from class_ground import Ground


s = Polygon((0, 0), (1, 0), (2, 1), (2, 2), (0, 1))
g = Ground("My land")

# Setup four points
points = vtk.vtkPoints()
points_number = 0
for p in s.vertices:
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