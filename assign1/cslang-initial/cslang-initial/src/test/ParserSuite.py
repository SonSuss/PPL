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
        input = """class Program {
    func main(): void {}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_simple_program_16(self):
        """simple program test"""
        input = """class Program {
    a: float = 3.;
    func main(): void {}}
        """
        expect = "Error on line 2 col 4: a"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_simple_program_17(self):
        """simple program test"""
        input = """class Program {
    func main(n: int, s: string): int {
            return s[n];}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_simple_program_18(self):
        """simple test"""
        input = """class Program {func main(n: lmao, s: string): int {
            return s[n];
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_simple_program_19(self):
        """simple test lmao is new type (class lmao???)"""
        input = """class Program {func main(n: int, s: string): money int {
            return s[n];
        }}
        """
        expect = "Error on line 1 col 51: int"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_simple_program_20(self):
        """Simple program"""
        input = """class Program {const x: float = 3.0}"""
        expect = "Error on line 1 col 35: }"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_simple_program_21(self):
        """simple test"""
        input = """class Program {func main(n:int , s: string): int {
            @foo(r);
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_simple_program_22(self):
        """simple test"""
        input = """class Program {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_simple_program_23(self):
        """simple test"""
        input = """class Program {func r(): int {}
        const f: string = "For fun";}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_simple_program_24(self):
        """simple test"""
        input = """class Program {func r(): int {bedge = 1;}}
        """
        expect = "Error on line 1 col 36: ="
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_simple_program_25(self):
        """simple test"""
        input = """class Program {func r(): int  {} func _r_1 ():  void {}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_simple_program_26(self):
        """simple test"""
        input = """class Program {
            continue;}
        """
        expect = "Error on line 2 col 12: continue"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_simple_program_27(self):
        """simple test"""
        input = """class Program {
            func deez(nut: int): float {}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_simple_program_28(self):
        """simple test"""
        input = """class Program {
            func main(n: int, s: string, const f: float) {}}
        """
        expect = "Error on line 2 col 41: const"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_simple_program_29(self):
        """simple test"""
        input = """class Program {
            func main(n: true):void {}}
        """
        expect = "Error on line 2 col 25: true"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_simple_program_30(self):
        """simple test"""
        input = """class Program {
        func main(n: bool): void {}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_simple_program_31(self):
        """simple test"""
        input = """class Program {func main(n, s, t):void {}}

        """
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_simple_program_32(self):
        """simple test"""
        input = """class Program {func main(n: string,,):void {}
}
        """
        expect = "Error on line 1 col 35: ,"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_simple_program_33(self):
        """simple test"""
        input = """class Program {func main(n):void {}
}
        """
        expect = "Error on line 1 col 26: )"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_simple_program_34(self):
        """simple test"""
        input = """class Program {func main(): void {}}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_simple_program_35(self):
        """simple test"""
        input = """class Program {
        func main(): void {
           var  x: float = 2.3e2;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_simple_program_36(self):
        """simple test"""
        input = """class Program {func main():  void {
            const x, y: int = 2, 3;
        }}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_simple_program_37(self):
        """simple test"""
        input = """class Program {func main():  void {
            const x, y: int = 2, 3,3;
        }
}
        """
        expect = "Error on line 2 col 34: ,"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_simple_program_38(self):
        """simple test"""
        input = """class Program {func main():  void {
            const x, y,z: int = 2, 3;
        }
}
        """
        expect = "Error on line 2 col 36: ;"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_simple_program_39(self):
        """Simple program"""
        input = """class Program {func main():  void {
           var  x, y, z: string = int, int, int ;
        }}
       
        """
        expect = "Error on line 2 col 34: int"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_simple_program_40(self):
        """simple test"""
        input = """class Program {func main():  void {
           var a: [5+5]int;
        }}
        """
        expect = "Error on line 2 col 20: +"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_simple_program_41(self):
        """simple test"""
        input = """class Program {func main():  void {
        var a: [n]int;}
        }
        """
        expect = "Error on line 2 col 16: n"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_simple_program_42(self):
        """simple test"""
        input = """class Program {func main():  void {
           var a: [10]int;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_simple_program_43(self):
        """simple test"""
        input = """class Program {func main():  void {
            const x, y: int = 2, 3;
            var a: [10]int;
            n := 5+2+3;
            c:= 5;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_simple_program_44(self):
        """simple test"""
        input = """class Program {func main():  void {
            var n :int = 5;
            var a :[n]A;
            var c : string = "why the var is the wrong one when I put n in to the BRACKET!";
        }}
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
    def test_simple_program_47(self):
        """simple test"""
        input = """class Program {func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
            }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_simple_program_48(self):
        """simple test"""
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
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_simple_program_49(self):
        """simple test"""
        input = """class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape():int {
                return @numOfShape;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_simple_program_50(self):
        """Simple program"""
        input = """class Program <- test{
            var a : [12]int;
            func @fact(n: bool):void {
                a[3] :=1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_simple_program_51(self):
        """simple test"""
        input = """class Program <- test{
            var tepm:string = "string";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_simple_program_52(self):
        """simple test"""
        input = """class Program <- test{
            var x: int = 65;
            func @fact(n: int):void {
                (new X("sd"^"w")).haha()[2]:=(new X("sd"^"w")).haha()[2];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_simple_program_53(self):
        """simple test"""
        input = """class Program {
             func main(): int{
                a := x.m()[3];
             }
             }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_simple_program_54(self):
        """simple test"""
        input = """class Program {
            func @main():int {
                @text := !(a && b);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_simple_program_55(self):
        """simple test"""
        input = """class A <- B{func X(): int {a[3+x.foo(2)] := a[b[2]] +3;}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_simple_program_56(self):
        """simple test"""
        input = """class Program {func main():void {
            const a: int = 3;
            const b: int = 4;
            var c: int = b % a + 4;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_simple_program_57(self):
        """simple test"""
        input = """class Program {
            func double(lst: int): int {
                if @len(lst) == 0 {
                    return null;
                }
                var i:int = lst[0];
                return ([a] + self.double(lst[12]));
            }
        }

        """
        expect = "Error on line 7 col 25: a"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_simple_program_58(self):
        """simple test"""
        input = """class Program {func main():void {
            a[3+x.foo(2)] := a[b[2]] +3;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_simple_program_59(self):
        """simple test"""
        input = """class Program {const a: int = 4;
        func main(): void {
            a := true || false && true;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_simple_program_60(self):
        """Simple program"""
        input = """class Program {
        func @main(): void {
            var a : [5]float;
            a[44 && 5 + 1] := ["DF",1,2];
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_simple_program_61(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if true {a := a + 1;}
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_simple_program_62(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if true {a := a + 1;}
            else {a := a - 1;}
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_simple_program_63(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a == 1 {
                return a == 1;
            }
            else {
                return a == 1;
            }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_simple_program_64(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a + 4 == 5 {
                return a + 1;
            }
            else {
                if a + 1 == 3 {
                    return a + 1;
                }
                return a + 2;
            }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_simple_program_65(self):
        """simple test"""
        input = """class Program {
        func main(): void {
             if a > 4 {
                return a + 1;
            }
            if a > 3
                {return 12;}
            if a == 1
               { return 5;}
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_simple_program_66(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if else a = 3 ;
        }}
        """
        expect = "Error on line 3 col 15: else"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_simple_program_67(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a <= 1
                {a := 1;}
            return 0;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_simple_program_68(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            for i := 0; i < 10; i := i + 1 {
            io.@writeInt(i);
            }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_simple_program_69(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            for i := 0; i + 1; {
                io.@writeInt(i);
            }
        }}

        """
        expect = "Error on line 3 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_simple_program_70(self):
        """Simple program"""
        input = """class Program {
        func main(): void {
            for a := 1; 10; a:=i + 2{
                io.@writeInt(i);
            }
        }}"""
        expect = "Error on line 3 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_simple_program_71(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            var a: [2] int;
            for index := 0; index < 10; index:= index + 1 {
                if a[index] == i
                   { break ; }
        }}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_simple_program_72(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            var a: [2] int;
            for index := 0; index < 10; index:=index + 1 {
                a[index] := 5;
            }
            break;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_simple_program_73(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a == i {
                    continue gogo;
            }
        }}
        """
        expect = "Error on line 4 col 29: gogo"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_simple_program_74(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a == i {
                    continue;
            }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_simple_program_75(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a == i {
                continue;
                continue;
            }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_simple_program_76(self):
        """simple test"""
        input = """class Program {
        func main(): void {
            if a == i {
                continue;
                break;
            }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_simple_program_77(self):
        """simple test"""
        input = """class Program {
        func main(): void {
             return metquadithoi;
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_simple_program_78(self):
        """simple test"""
        input = """class Program {
        func main(): void {
             return int;
        }}
        """
        expect = "Error on line 3 col 20: int"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_simple_program_79(self):
        """simple test"""
        input = """class Program {
        func main(): void {
             return @foo(3 + x, 4.0 / y);
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_simple_program_80(self):
        """Simple program"""
        input = """ class Program {
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_simple_program_81(self):
        """simple test"""
        input = """class Program {
            var a: [2]int ;
            a[1]:=2;
            a[2]:="why";
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "Error on line 3 col 12: a"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_simple_program_82(self):
        """simple test"""
        input = """class Program {
            func @main():int {
                @text := "Hello" ^ 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_simple_program_83(self):
        """simple test"""
        input = """class Program {
        func main(): void {
                var test: void = 1;
                return test;
            }}
        """
        expect = "Error on line 3 col 26: void"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_simple_program_84(self):
        """simple test"""
        input = """class Program {
            var a: [2]int = 2,"why not";
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "Error on line 2 col 29: ,"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_simple_program_85(self):
        """simple test"""
        input = """class Program {
            func thieuDusk (n: niga): void {
            @text := @text + nian;
            for i:=0; i<@thieuSuzu(); i:=i+1 {
                //comment 1
                if {@x := 0;} _test > i
                {
                    _test := _test - @_;
                }
                else
                {
                    @_ := @_ + 1;
                }
            }
            }}

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_simple_program_86(self):
        """simple test"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_simple_program_87(self):
        """simple test"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2];
        }}
        """
        expect = "Error on line 4 col 16: ,"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_simple_program_88(self):
        """simple test"""
        input = """class Program {
            var a: [2][2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2] ,[2,3];
        }}
        """
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_simple_program_89(self):
        """simple test"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2] ,[2,3];
        }}
        """
        expect = "Error on line 4 col 16: ,"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_simple_program_90(self):
        """Simple program"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[a[2]] := [1,2] ,[2,3];
        }}"""
        expect = "Error on line 4 col 29: ,"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_simple_program_91(self):
        """simple test"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[a[2]] := [2,3];
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_simple_program_92(self):
        """simple test"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[a[2]] := [2,3];
        }}
            class toidaudon <- Program{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_simple_program_93(self):
        """simple test"""
        input = """class toidaudon <- Program{
                func @main():void{
                a[3+x.foo(2)] := a[b[2]] +3;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_simple_program_94(self):
        """simple test"""
        input = """class @toidaudon <- Program{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "Error on line 1 col 6: @toidaudon"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_simple_program_95(self):
        """simple test"""
        input = """class toidaudon <- @Program{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "Error on line 1 col 19: @Program"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_simple_program_96(self):
        """simple test"""
        input = """class toidaudon <- Program, Nworld{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_simple_program_97(self):
        """simple test"""
        input = """class toidaudon <- Program <- Nworld{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "Error on line 1 col 27: <-"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_simple_program_98(self):
        """simple test"""
        input = """class Program{
            func railfence(ciphertext: string, key: integer):string {
            if key <= 1
                {return ciphertext;}
            
            var matrix: [15] string;
            for i:=0 ; i<15 ; i:=i+1 {
                var matrix_a: [15]string;
            }
            /* 
                15 for each row
                maxium 15 rows
            */

            var dir: bool = true;
            // true for down, false for up

            var row, col: int= 0, 0;

            for i := 0; i < @length(ciphertext); i:=i + 1 {
                if row == 0 {dir := true;}
                if row == key - 1 {dir := false;}
                rail[row] := null;
                
                col := col + 1;
                if dir
                    {row := row + 1;}
                else {row := row - 1;}
            }

            var index: int = 0;
            for i := 0; i < key; i:=i + 1 {
                for j := 0; j < a.length(ciphertext);j:= j + 1{
                    if matrix[i] == null && (index < as.length(ciphertext)) {
                        matrix[i] := ciphertext[index];
                        index := index + 1;
                    }}
            
            row := 0; col := 0;
            var result: string;
            for i:=0; i< @length(ciphertext);i:= i + 1 
            {
                // check the direction of flow
                if row == 0
                    {dir := true;}
                if row == key - 1
                    {dir := false;}
 
                // place the marker
                if rail[row] != "*"
                    {result := result.rail[col];}
                col := col + 1;
 
                // find the next row using direction flag
                if dir
                    {row := row + 1;}
                else {row := row - 1;}
            }
            return result;
        }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test_simple_program_99(self):
        """simple test"""
        input = """class Program {
        func railfence(plain: string, key: integer): string {
            if key <= 1
                {return plain;}
            var matrix: [15] string; // 15 is the maximum number of rows
            var row, dir: int = 0, -1;

            for i := 0; i < @length(plain); i:=i + 1 {
                if (j == key - 1) || (j == 0)
                    {dir := dir * -1;}
                matrix[j] := plain[i];
                if dir == 1
                    {j := j + 1;}
                else
                    {j := j - 1;}
            }

            var ciphertext : string;
            for i := 0; i < key; i:=i + 1 {
                ciphertext := ciphertext.matrix[i];
            }
            return ciphertext;
        }
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_simple_program_missing_one(self):
        """simple test"""
        input = """class Program {
        func jowd(a:int): string {
            if true  {
                a[5] := a[1] + 2;
                b[9] := b[5] || false;
            } else;
        }
            }
        """
        expect = "Error on line 6 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 300))
