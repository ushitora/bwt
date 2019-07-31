import unittest
import bwt.bbwt as bbwt

class TestBBWT(unittest.TestCase):
    def test_bijective_bwt(self):
        self.assertEqual(bbwt.bijective_bwt('a'), 'a')
        self.assertEqual(bbwt.bijective_bwt('abbababa'), 'abbbaaba')
        self.assertEqual(bbwt.bijective_bwt('abababaaababababa'), 'ababbbabbbaaaaaaa')

    def test_bijective_bwt_inv(self):
        texts = [
            'abraca',
            'aabbaabb',
            'kjasdfjbasjkdfkajsbdkfjabsdflajsdfasd',
            'abaababaabaababaababaabaababaabaababaababaabaababaababaabaababaabaababaababaabaababaabaab',
        ]
        for w in texts:
            self.assertEqual(bbwt.bijective_bwt_inv(bbwt.bijective_bwt(w)), w)
