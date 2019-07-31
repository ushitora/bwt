import unittest
import bwt.sbwt as sbwt

class TestBWT(unittest.TestCase):
    def test_bwt(self):
        self.assertEqual(sbwt.bwt('abraca'), ('caraab', 1))

    def test_bwt_inv(self):
        texts = [
            'abraca',
            'aabbaabb',
            'kjasdfjbasjkdfkajsbdkfjabsdflajsdfasd',
            'abaababaabaababaababaabaababaabaababaababaabaababaababaabaababaabaababaababaabaababaabaab',
        ]
        for w in texts:
            self.assertEqual(w, sbwt.bwt_inv(*sbwt.bwt(w)))
