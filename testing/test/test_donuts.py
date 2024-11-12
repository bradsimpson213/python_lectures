import unittest
from code import enough_donuts
from random import randint
from inspect import getsource


class TestDonutFunction(unittest.TestCase):
    def test_donut_response_lowest(self):
        result_1 = enough_donuts(randint(0, 1))
        self.assertEqual(result_1, "Not enough donuts")
    # def test_donut_response_middle_1(self):
        result_2 = enough_donuts(randint(2, 4))
        self.assertEqual(result_2, "That's enough donuts")
        result_3 = enough_donuts(randint(5, 12))
        self.assertEqual(result_3, "That's a lot of donuts")
        result_4 = enough_donuts(randint(13, 50))
        self.assertEqual(result_4, "I hope you are sharing")


    def test_if_syntax_use(self):
        source_code = getsource(enough_donuts)
        print(source_code)
        is_if = source_code.find("if") > -1
        print('ISIF',is_if)
        self.assertTrue(is_if)
        is_elif = source_code.find("elif") > -1
        self.assertTrue(is_elif)
        is_else = source_code.find("else") > -1
        self.assertTrue(is_else)

 

    def test_edge_cases(self):
        result = enough_donuts(randint(-10, -1))
        # print(result)
        self.assertEqual(result, "No donuts on credit, we must use positive integers")