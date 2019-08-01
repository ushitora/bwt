import unittest
import bwt.utils as utils

class TestUtils(unittest.TestCase):
    def test_cyclic_group(self):
        self.assertEqual(list(utils.cyclic_group('abcd')), ['abcd', 'dabc', 'cdab', 'bcda'])
