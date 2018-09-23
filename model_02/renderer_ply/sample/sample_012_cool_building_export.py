from sympy import *
from model_02 import *
from model_02.renderer_ply.fun_shape_to_ply import *

my_plan = Plan("My land")
my_plan.polygon_base = Polygon((0, 0), (50, -10), (100, 00), (110, 50), (100, 100), (50, 110), (0, 100), (-10, 50), (0, 0))

my_building = Building("My house")
my_building.polygon_base = Polygon((20, 20), (80, 20), (80, 80), (20, 80), (20, 20))
my_plan.append_shape(my_building)

floor_basement = Floor("Basement", position=Point3D(0, 0, 20))
floor_basement.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
my_building.append_shape(floor_basement)

floor_1 = Floor("1st floor", position=Point3D(0, 0, 40))
floor_1.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
my_building.append_shape(floor_1)

floor_2 = Floor("2nd floor", position=Point3D(0, 0, 60))
floor_2.polygon_base = Polygon((30, 30), (70, 30), (70, 70), (30, 70), (30, 30))
my_building.append_shape(floor_2)

#my_plan.get_flattened_shape_list()

print(shape_to_ply(my_plan))
