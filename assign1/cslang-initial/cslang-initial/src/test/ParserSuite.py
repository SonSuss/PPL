import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """program"""
        expect = "Error on line 1 col 7: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_simple_program_1(self):
        """class Test"""
        input = """
        class Shape {
        var @numOfShape: int = 0;
        const immutableAttribute: int = 0;
        var length, width: int;
        func @getNumOfShape():int {
        return @numOfShape;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_program_2(self):
        """class Test"""
        input = """
        class Shape <- Retangle {
        func getArea():int {
        return self.length * self.width;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_simple_program_3(self):
        """class Test"""
        input = """
        class Program {
        func @main():void {
        io.@writeInt(Shape.@numOfShape);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))