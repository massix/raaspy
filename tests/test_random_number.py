import unittest
from api_number import random
from model import NumberObject


class TestRandomNumber(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def test_random_number(cls):
        n = NumberObject.deserialize(**random.get(1, 100))
        assert n.result in range(1, 100)

    @classmethod
    def test_random_number_boundaries(cls):
        n = NumberObject.deserialize(**random.get(800, 810))
        assert n.result in range(800, 810)
