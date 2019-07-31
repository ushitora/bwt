import unittest
import bwt.lyndon as lyndon
from bwt.lyndon import is_lyndon

class TestLyndon(unittest.TestCase):
    def test_lyndon_factorize(self):
        self.assertEqual(list(lyndon.lyndon_factorize('abb')), ['abb'])
        self.assertEqual(list(lyndon.lyndon_factorize('abbababba')), ['abb', 'ababb', 'a'])
        self.assertEqual(list(lyndon.lyndon_factorize('bcdeafgfed')), ['bcde', 'afgfed'])

    def test_is_lyndon(self):
        self.assertTrue(lyndon.is_lyndon('ababb'))

    def test_longest_lyndon_prefix(self):
        self.assertEqual(lyndon.longest_lyndon_prefix('abbaa'), (3, 1))
        self.assertEqual(lyndon.longest_lyndon_prefix('abbabb'), (3, 2))
