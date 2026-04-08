import unittest
from Mathematics import mathematics
import random

class MathematicsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mathsIns = mathematics()

    def setUp(self):
        self.first_num = random.randint(1, 100)
        self.second_num = random.randint(1, 100)
        self.sum = self.first_num + self.second_num

    def test_add(self):
        sum = self.mathsIns.addition(self.first_num, self.second_num)
        print(self.sum)
        self.assertEqual(sum, self.sum)

    def test_addition(self):
        sum = self.mathsIns.addition(self.first_num, self.second_num)
        print(self.sum)
        self.assertEqual(sum, self.sum)

if __name__=="__main__":
    unittest.main()