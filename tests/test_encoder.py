import unittest
import bwt.encoder as encoder


class TestEncoder(unittest.TestCase):
    def test_runlength_encode(self):
        self.assertEqual(encoder.runlength_encode('abc', b=False), [1, 'a', 1, 'b', 1, 'c'])
        self.assertEqual(encoder.runlength_encode('aaabbbbccc', b=False), [3, 'a', 4, 'b', 3, 'c'])
        self.assertEqual(encoder.runlength_encode('a' * 255, b=False), [255, 'a'])
        self.assertEqual(encoder.runlength_encode('a' * 256, b=False), [255, 'a', 1, 'a'])
