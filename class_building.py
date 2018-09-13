from class_floor import Floor

"""building class

blablabla
blablabla
blablabal
"""


class Building:

    def __init__(self, name="some building", height=120):
        self.name = name
        self.height = height
        self.floor_list = []

    """generate n additional floors in the building,
    providing there is still some available space"""
    def generate_floor(self, floor_number):
        if self.get_floor_height_total() == 0:
            raise ValueError("impossible to generate more floors because there is no space left")
        floor_height = self.get_free_height_total() / floor_number
        for i in range(floor_number):
            f = Floor()
            f.height = floor_height
            self.floor_list.append(f)

    """computes the total height of the building floors"""
    def get_floor_height_total(self):
        h = 0
        for f in self.floor_list:
            h += f.height
        return h

    """computes the available free height"""
    def get_free_height_total(self):
        return self.height - self.get_floor_height_total()
