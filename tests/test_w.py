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

    def test_single_annot(self):
        data = [[1], [2], [3]]
        with self.assertRaises(ValueError):
            compute_w(data)

    def test_single_item(self):
        data = [[1, 1, 1]]
        with self.assertRaises(ValueError):
            compute_w(data)

    def test_diff_sublist_elem(self):
        data = [[1, 1, 1], [2, 2, 2], [3, 3]]
        with self.assertRaises(ValueError):
            compute_w(data)

    def test_warn_two_annot(self):
        data = [[1, 1], [2, 2], [3, 3], [4, 4]]
        with self.assertWarns(Warning):
            compute_w(data)

    def test_ranking(self):
        pass

if __name__ == '__main__':
    unittest.main()
