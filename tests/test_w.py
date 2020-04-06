import unittest
from kendall_w import compute_w

class TestComputeW(unittest.TestCase):

    def setUp(self):
        self.perfect_agg = [[1,1,1], [2,2,2], [3,3,3]]
        self.perfect_disagg = [[1,2,3], [2,3,1], [3,1,2]]
    
    def tearDown(self):
        pass

    def test_perfect_result(self):
        self.assertEqual(compute_w(self.perfect_agg), 1)
    
    def test_worst_result(self):
        self.assertEqual(compute_w(self.perfect_disagg), 0)

    def test_input_types(self):
        pass

    def test_diff_list_elem(self):
        pass

    def test_diff_sublist_elem(self):
        pass

    def test_ranking(self):
        pass

if __name__ == '__main__':
    unittest.main()