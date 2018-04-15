import unittest

class TestCase3(unittest.TestCase):

    @unittest.skip('skip test1')
    def test1(self):
        pass

    @unittest.skipIf(1 > 0, '1 > 0')
    def test2(self):
        pass

    @unittest.skipUnless(0 > 1, '0 > 1')
    def test3(self):
        pass

    @unittest.expectedFailure
    def test4(self):
        self.assertTrue(False)
