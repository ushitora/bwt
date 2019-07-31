import unittest
import bwt.bwt as bwt

class TestBWT(unittest.TestCase):
    def test_bwt(self):
        self.assertEqual(bwt('abraca'), ('caraab', 1))

    def test_bwt_inv(self):
        # TODO
        pass