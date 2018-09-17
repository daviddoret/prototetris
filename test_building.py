from unittest import TestCase
from class_ModelBuilding import ModelBuilding
from class_ModelFloor import ModelFloor


class TestBuilding(TestCase):
    def test_set_height(self):
        b = ModelBuilding("my building", 50)
        self.assertEqual(b.height, 50)
        b.set_height(100)
        self.assertEqual(b.height, 100)


class TestBuilding(TestCase):
    def test_generate_floor(self):
        b = ModelBuilding("my building", 100)
        self.assertEqual(b.floor_height_total(), 0)
        f1 = ModelFloor()
        f1.height = 20
        b.floor_list.append(f1)
        self.assertEqual(b.floor_height_total(), 20)
        b.generate_floor(8)
        self.assertEqual(b.floor_height_total(), 0)


