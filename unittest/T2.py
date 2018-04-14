import unittest

class Test2(unittest.TestCase):

    def setUpClass():
        pass

    def tearDownClass():
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        pass

    def test2(self):
        pass

    @unittest.skip('skip test3')
    def test3(self):
        pass

    @unittest.expectedFailure
    def test4(self):
        self.assertEqual(1, 2)

    def test5(self):
        print(self.id())

if __name__ == '__main__':
    unittest.main()
