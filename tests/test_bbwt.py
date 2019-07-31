import unittest
import bwt.bbwt as bbwt

class TestBBWT(unittest.TestCase):
    def test_bijective_bwt(self):
        self.assertEqual(bbwt.bijective_bwt('a'), 'a')
        self.assertEqual(bbwt.bijective_bwt('abbababa'), 'abbbaaba')
        self.assertEqual(bbwt.bijective_bwt('abababaaababababa'), 'ababbbabbbaaaaaaa')


    def test_bijective_bwt_inv(self):
        # TODO
        pass