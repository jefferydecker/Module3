import unittest
import unittest.mock as mock
from format_output import average_scores


class MyTestCase(unittest.TestCase):
def test_average(self):
    with mock.patch('builtins.input', side_effects=[85, 90, 90]):
        assert average_scores.average() == 90


if __name__ == '__main__':
    unittest.main()
