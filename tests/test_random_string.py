import unittest
from api_string import random
from model import StringObject
import re


class TestRandomString(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def test_random_string_upper(cls):
        s = StringObject.deserialize(**random.get_random_string(32, 'capitol_letters'))
        assert s.result.__len__() == 32
        assert re.fullmatch(r'[A-Z]{32}', s.result)

    @classmethod
    def test_random_string_lower(cls):
        s = StringObject.deserialize(**random.get_random_string(16, 'letters'))
        assert s.result.__len__() == 16
        assert re.fullmatch(r'[a-z]{16}', s.result)
