import unittest
from api_string import random


class TestRandomString(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def test_random_string_generation(cls):
        print(random.get_random_string(32))
