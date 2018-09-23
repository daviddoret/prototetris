from sympy import *
from model_02 import *
from model_02.renderer_ply.fun_shape_to_ply_text import *
from model_02.renderer_ply.fun_shape_to_ply_file import *

my_plan = Plan("My land", height=2000)
my_plan.polygon_base = Polygon((0, 0), (7000, 0), (7000, 7000), (0, 7000), (0, 0))
print("my_plan.position: {}".format(my_plan.position))

my_building = Building("My house", height=1000)
my_building.polygon_base = Polygon((0, 0), (6000, 0), (6000, 6000), (0, 6000), (0, 0))
my_plan.append_shape(my_building, position=Point3D(500, 500, 0))
print("my_building.position: {}".format(my_building.position))

floor_basement = Floor("Basement", height=300)
floor_basement.polygon_base = Polygon((0, 0), (5000, 0), (5000, 5000), (0, 5000), (0, 0))
my_building.append_shape(floor_basement, position=Point3D(500, 500, 50))
print("floor_basement.position: {}".format(floor_basement.position))

h = 300

for i in range(1, 50):
    floor_x = Floor("1st floor", height=300)
    floor_x.polygon_base = Polygon((0, 0), (5000, 0), (5000, 5000), (0, 5000), (0, 0))
    my_building.append_shape(floor_x, position=Point3D(500, 500, 350 + i * h))

#my_plan.get_flattened_shape_list()

print(shape_to_ply_text(my_plan))
shape_to_ply_file(my_plan, "sample_012.ply")