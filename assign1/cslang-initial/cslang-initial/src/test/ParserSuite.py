import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """program"""
        expect = "Error on line 1 col 0: program"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_simple_program_1(self):
        """simple test"""
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
    def test_simple_program_4(self):
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
        class Shape <- Retangle {
        func getArea():int {
        return self.length * self.width;
        }
        }
        class Program {
        func @main():void {
        io.@writeInt(Shape.@numOfShape);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_simple_program_5(self):
        """class Test"""
        input = """
                class Shape {
        var @numOfShape: int = 0;
        const immutableAttribute: int = 0;
        var length, width: int;
        func @getNumOfShape():int {
        return @numOfShape;
        }
        class Shape <- Retangle {
        func getArea():int {
        return self.length * self.width;
        }
        }
        class Program {
        func @main():void {
        io.@writeInt(Shape.@numOfShape);
        }
        }
        """
        expect = "Error on line 9 col 8: class"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_simple_program_6(self):
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
        class Shape <- Retangle {
        func getArea():int {
        return self.length * self.width
        }
        }
        class Program {
        func @main():void {
        io.@writeInt(Shape.@numOfShape);
        }
        }
        """
        expect = "Error on line 13 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_simple_program_7(self):
        """class Test"""
        input = """
        class Shape {{
        var @numOfShape: int = 0;
        const immutableAttribute: int = 0;
        var length, width: int;
        func @getNumOfShape():int {
        return @numOfShape;
        }
        }
        class Shape <- Retangle {
        func getArea():int {
        return self.length * self.width;
        }
        }
        class Program {
        func @main():void {
        io.@writeInt(Shape.@numOfShape);
        }
        }
        """
        expect = "Error on line 2 col 21: {"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_simple_program_8(self):
        """class Test"""
        input = """
    class RandomClass {
        func constructor (num : int) {
            number := num;
        }

        func getNumber():int {
            return number;
        }

        func setNumber(num : int):void {
            number := num;
        }

        func printNumber():void {
        }
        
    };
        """
        expect = "Error on line 18 col 5: ;"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_simple_program_9(self):
        """class Test"""
        input = """class A{var delta: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_simple_program_10(self):
        """class Test"""
        input = """class Program{ const a, b, c: int = 3, 4, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_simple_program_12(self):
        """class Test"""
        input = """class Program{var  a, b, c, d: int = 3, 4, 6;}"""
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_simple_program_13(self):
        """class Test"""
        input = """class Program {func @main():int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_simple_program_14(self):
        """class Test"""
        input = """class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_simple_program_15(self):
        """simple program test"""
        input = """
    func main(): void {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_simple_program_16(self):
        """simple program test"""
        input = """
    a: float = 3.;
    func main(): void {}
        """
        expect = "Error on line 2 col 4: a"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_simple_program_17(self):
        """simple program test"""
        input = """
    func main(n: int, s: string): int {
            return s[n];}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_simple_program_18(self):
        """simple test"""
        input = """func main(n: lmao, s: string): int {
            return s[n];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_simple_program_19(self):
        """simple test lmao is new type (class lmao???)"""
        input = """func main(n: int, s: string): money int {
            return s[n];
        }
        """
        expect = "Error on line 1 col 36: int"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_simple_program_20(self):
        """Simple program"""
        input = """const x: float = 3.0"""
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_simple_program_21(self):
        """simple test"""
        input = """func main(n:int , s: string): int {
            foo(r);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_simple_program_22(self):
        """simple test"""
        input = """
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_simple_program_23(self):
        """simple test"""
        input = """func r(): int {}
        const f: string = "For fun";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_simple_program_24(self):
        """simple test"""
        input = """func r(): int {bedge = 1;}
        """
        expect = "Error on line 1 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_simple_program_25(self):
        """simple test"""
        input = """func r(): int  {} func _r_1 ():  void {}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_simple_program_26(self):
        """simple test"""
        input = """
            continue;
        """
        expect = "Error on line 2 col 12: continue"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_simple_program_27(self):
        """simple test"""
        input = """
            func deez(nut: int): float {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_simple_program_28(self):
        """simple test"""
        input = """
            func main(n: int, s: string, const f: float) {}
        """
        expect = "Error on line 2 col 41: const"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_simple_program_29(self):
        """simple test"""
        input = """
            func main(n: true):void {}
        """
        expect = "Error on line 2 col 25: true"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_simple_program_30(self):
        """simple test"""
        input = """
        func main(n: bool): void {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_simple_program_31(self):
        """simple test"""
        input = """func main(n, s, t):void {}

        """
        expect = "Error on line 1 col 17: )"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_simple_program_32(self):
        """simple test"""
        input = """func main(n: string,,):void {}

        """
        expect = "Error on line 1 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_simple_program_33(self):
        """simple test"""
        input = """func main(n):void {}

        """
        expect = "Error on line 1 col 11: )"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_simple_program_34(self):
        """simple test"""
        input = """func main(): void {}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_simple_program_35(self):
        """simple test"""
        input = """
        func main(): void {
           var  x: float = 2.3e2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_simple_program_36(self):
        """simple test"""
        input = """func main():  void {
            const x, y: int = 2, 3;
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_simple_program_37(self):
        """simple test"""
        input = """func main():  void {
            const x, y: int = 2, 3,3;
        }

        """
        expect = "Error on line 2 col 34: ,"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_simple_program_38(self):
        """simple test"""
        input = """func main():  void {
            const x, y,z: int = 2, 3;
        }

        """
        expect = "Error on line 2 col 36: ;"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_simple_program_39(self):
        """Simple program"""
        input = """func main():  void {
           var  x, y, z: string = int, int, int ;
        }
       
        """
        expect = "Error on line 2 col 34: int"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_simple_program_40(self):
        """simple test"""
        input = """func main():  void {
           var a: [5+5]int;
        }
        """
        expect = "Error on line 2 col 20: +"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_simple_program_41(self):
        """simple test"""
        input = """func main():  void {
        var a: [n]int;
        }
        """
        expect = "Error on line 2 col 16: n"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_simple_program_42(self):
        """simple test"""
        input = """func main():  void {
           var a: [10]int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_simple_program_43(self):
        """simple test"""
        input = """func main():  void {
            const x, y: int = 2, 3;
            var a: [10]int;
            n := 5+2+3;
            c:= 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_simple_program_44(self):
        """simple test"""
        input = """func main():  void {
            var n :int = 5;
            var a :[n]A;
            var c : string = "why the var is the wrong one when I put n in to the BRACKET!";
        }
        """
        expect = "Error on line 3 col 20: n"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_simple_program_45(self):
        """class as new type"""
        input = """class Program {
            const a: [5]A;

            func X(): Abc {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_simple_program_46(self):
        """simple test"""
        input = """class Program {
            func @main():int {
                @text := a[x.m()[5]];
            }
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 248))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 249))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 250))
    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 251))
    # def test_simple_program_1(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 252))
    # def test_simple_program_2(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 253))
    # def test_simple_program_3(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 254))
    # def test_simple_program_4(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 255))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 256))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 257))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 258))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 259))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 260))
    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 261))
    # def test_simple_program_1(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 262))
    # def test_simple_program_2(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 263))
    # def test_simple_program_3(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 264))
    # def test_simple_program_4(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 265))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 266))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 267))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 268))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 269))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 270))
    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 271))
    # def test_simple_program_1(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 272))
    # def test_simple_program_2(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 273))
    # def test_simple_program_3(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 274))
    # def test_simple_program_4(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 275))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 276))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 277))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 278))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 279))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 280))
    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 281))
    # def test_simple_program_1(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 282))
    # def test_simple_program_2(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 283))
    # def test_simple_program_3(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 284))
    # def test_simple_program_4(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 285))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 286))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 287))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 288))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 289))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 290))
    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 291))
    # def test_simple_program_1(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 292))
    # def test_simple_program_2(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 293))
    # def test_simple_program_3(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 294))
    # def test_simple_program_4(self):
    #     """simple test"""
    #     input = """
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 295))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 296))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 297))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 298))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 299))
    # def test_simple_program_5(self):
    #     """simple test"""
    #     input = """

    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 200))
