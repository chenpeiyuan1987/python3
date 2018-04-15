import unittest

class TestCase4(unittest.TestCase):

    def test1(self):
        for i in [2, 4, 6]:
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    @unittest.expectedFailure
    def test2(self):
        self.fail()
