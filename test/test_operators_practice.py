import unittest


class MyTestCase(unittest.TestCase):

    def test_gt_equal_operator(self):
        self.assertTrue(3 >= 3)

    def test_lt_equal_operator(self):
        self.assertFalse(2 <= 1)


if __name__ == '__main__':
    unittest.main()
