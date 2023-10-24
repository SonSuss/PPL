import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """class Program {
             func main(): int{
                self.aPI := 3.14;
             }
             }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
