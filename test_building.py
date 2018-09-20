from unittest import TestCase
from prototetris_model_2.class_Building import Building
from prototetris_model_2.class_Floor import Floor


class TestBuilding(TestCase):
    def test_set_height(self):
        b = Building("my building", 50)
        self.assertEqual(b.height, 50)
        b.set_height(100)
        self.assertEqual(b.height, 100)


class TestBuilding(TestCase):
    def test_generate_floor(self):
        b = Building("my building", 100)
        self.assertEqual(b.floor_height_total(), 0)
        f1 = Floor()
        f1.height = 20
        b.floor_list.append(f1)
        self.assertEqual(b.floor_height_total(), 20)
        b.generate_floor(8)
        self.assertEqual(b.floor_height_total(), 0)


