from model_02.class_Plan import Plan
from model_02.class_Building import Building
from model_02.class_Floor import Floor
from sympy import Point, Polygon
from model_02.class_Flat import Flat

# Create a ground surface
a_cool_place = Plan()
a_cool_place.polygon_base = Polygon((0, 0), (100, 0), (100, 50), (0, 50))

# Build a building
my_building = Building()
my_building.polygon_base = Polygon((0, 0), (75, 0), (75, 40), (0, 40))
a_cool_place.append_building(my_building, position=Point(10, 15))

# Create a floor in the building
basement = Floor()
my_building.append_floor(basement)

# Create another floor in building
first_floor = Floor()
my_building.append_floor(first_floor)

# Create 2 flats on the second floor
flat1 = Flat()
first_floor.append_flat(flat1)

flat2 = Flat()
first_floor.append_flat(flat2)


