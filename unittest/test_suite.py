import unittest
from test_case_1 import TestCase1

class TestSuite(unittest.TestSuite):

    def __init__(self):
        loader = unittest.defaultTestLoader
        classes = [TestCase1]
        for case in classes:
            addTests(loader.loadTestsFromTestCase(case))
