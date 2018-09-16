from sympy import Point, Polygon
from class_building import Building
import vtk

b = Building()
b.shape = Polygon((0, 0), (10, 0), (15, 10), (30, 30), (20, 30), (0, 0))
b.to_vtk()
