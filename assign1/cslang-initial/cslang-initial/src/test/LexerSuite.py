import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_bc", "_bc,<EOF>", 101))

    def test_identifier_case_0(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc 123", "abc 123,<EOF>", 102))
    def test_keyword_case_0(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("string _1290", "string _1290,<EOF>", 103))

    

    
