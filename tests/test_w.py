import unittest
from kendall_w.kendall_w import compute_w

class TestComputeW(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_(self):
        self.assertEqual(compute_w([[1,1,1], [2,2,2], [3,3,3]]), 1)


if __name__ == '__main__':
    unittest.main()