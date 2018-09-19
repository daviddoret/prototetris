from class_ModelFloor import ModelFloor
from class_ModelIrregularRightPrism import ModelIrregularRightPrism
from class_ModelAbstractShape import ModelAbstractShape
from fun_vtk_sympy_polygon_to_vtk_polydata import sympy_polygon_to_vtk_polydata
import jsonpickle

"""ModelBuilding class
"""


class ModelBuilding(ModelIrregularRightPrism):

    def __init__(self, label="A building", description="", height=None, *args, **kwargs):
        ModelIrregularRightPrism.__init__(self, label, description, *args, **kwargs)
        self.height = height

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def floor_list(self):
        return list(lambda x: isinstance(x, ModelFloor), ModelIrregularRightPrism.nested_shape_list)

    def append_floor(self, floor):
        ModelIrregularRightPrism.append_shape(self, floor)

    def generate_floor(self, floor_number):
        """generate n additional floors in the building,
        providing there is still some available space"""
        if self.floor_height_total() == 0:
            raise ValueError("impossible to generate more floors because there is no space left")
        floor_height = self.free_height_total() / floor_number
        for i in range(floor_number):
            f = ModelFloor()
            f.height = floor_height
            self.append_floor(f)

    @property
    def floor_height_total(self):
        """computes the total height of the building floors"""
        h = 0
        for f in self.floor_list:
            h += f.height
        return h

    @property
    def free_height_total(self):
        """computes the available free height"""
        return self.height - self.floor_height_total()

    def to_vtk_polydata(self):
        return sympy_polygon_to_vtk_polydata(self.shape, color=(100, 100, 100), altitude=10)
