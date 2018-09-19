from class_ModelIrregularRightPrism import ModelIrregularRightPrism
from class_ModelGround import ModelGround
from class_ModelBuilding import ModelBuilding
from class_ModelFloor import ModelFloor
from sympy import Point, Polygon
from class_ModelFlat import ModelFlat

# Create a ground surface
a_cool_place = ModelGround()
a_cool_place.shape = Polygon((0, 0), (100, 0), (100, 50), (0, 50))

# Build a building
my_building = ModelBuilding()
my_building.shape = Polygon((0, 0), (75, 0), (75, 40), (0, 40))
a_cool_place.append_building(my_building, position=Point(10, 15))

# Create a floor in the building
basement = ModelFloor()
my_building.append_floor(basement)

# Create another floor in building
first_floor = ModelFloor()
my_building.append_floor(first_floor)

# Create 2 flats on the second floor
flat1 = ModelFlat()
first_floor.append_flat(flat1)

flat2 = ModelFlat()
first_floor.append_flat(flat2)


