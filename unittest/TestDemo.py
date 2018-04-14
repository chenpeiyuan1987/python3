import unittest

class TestDemo(unittest.TestCase):

    def setUpClass():
        print('setUpClass');

    def tearDownClass():
        print('tearDownClass')

    def setUp(self):
        print('setUp');

    def tearDown(self):
        print('tearDown');

    def test_1(self):
        print('test_1');
        # self.assertEqual('foo'.title(), 'Foo')

    def test_2(self):
        print('test_2');


if __name__ == '__main__':
    unittest.main()
