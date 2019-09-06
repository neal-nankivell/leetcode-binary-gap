import solution
import unittest


class Test_TestBinaryGap(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_binaryGap22(self):
        self.assertEqual(self.sut.binaryGap(22), 2)

    def test_binaryGap5(self):
        self.assertEqual(self.sut.binaryGap(5), 2)

    def test_binaryGap6(self):
        self.assertEqual(self.sut.binaryGap(6), 1)

    def test_binaryGap8(self):
        self.assertEqual(self.sut.binaryGap(8), 0)


if __name__ == '__main__':
    unittest.main()
