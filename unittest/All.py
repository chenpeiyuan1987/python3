import unittest
from T2 import Test2
from TestDemo import TestDemo

if __name__ == '__main__':
    suite = unittest.TestSuite()

    for case in [Test2, TestDemo]:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(case))

    runner = unittest.TextTestRunner();
    runner.run(suite)
