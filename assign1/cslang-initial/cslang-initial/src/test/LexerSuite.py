import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_bc", "_bc,<EOF>", 101))

    def test_integer_case_0(self):
        """test INTEGER"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 102))
    def test_integer_case_1(self):
        """test INTEGER"""
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 103))
    def test_float_case_0(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("1.1290", "1.1290,<EOF>", 104))
    def test_float_case_1(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("1.1e+290", "1.1e+290,<EOF>", 105))
    def test_float_case_2(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test(".1290", ".1290,<EOF>", 106))
    def test_bool_case_0(self):
        """test bool"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 107))
    

    

    
