import unittest

from ddt import ddt,data

@ddt
class Parameterized(unittest.TestCase):
    def setUp(self) -> None:
        data_source =