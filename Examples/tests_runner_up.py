import unittest

from Examples.RunnerUp import get_runner_up


class TestIsRunnerUp(unittest.TestCase):
    # inline test
    def test_is_runner_up_true(self):
        self.assertEqual(get_runner_up(n=5, arr=[2, 3, 6, 6, 5]), 5)
    # O(n) test
    # future implementation


if __name__ == '__main__':
    unittest.main()
