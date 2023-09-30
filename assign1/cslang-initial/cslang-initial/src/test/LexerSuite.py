import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1bc", "1,bc,<EOF>", 100))
    def test_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1 bc", "1,bc,<EOF>", 101))
    def test_3(self):
        """test INTEGER"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 102))
    def test_4(self):
        """test INTEGER"""
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 103))
    def test_5(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 104))
    def test_6(self):
        """test FLOAT"""
        self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 105))
    def test_7(self):
        """test bool"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 107))
    def test_8(self):
        """test blockcomment"""
        self.assertTrue(TestLexer.test("/*abc \nabc*/_a12", "_a12,<EOF>", 109))
    def test_9(self):
        """test blockcomment"""
        self.assertTrue(TestLexer.test("abc/*abc \tabc*/", "abc,<EOF>", 110))
    def test_10(self):
        """test blockcomment"""
        self.assertTrue(TestLexer.test("/*abc abc*/\nabcd", "abcd,<EOF>", 111))
    def test_11(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"", "This is a string containing tab \\t,<EOF>", 112))
    def test_12(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"This is a string\\\\\"", "This is a string\\\\,<EOF>", 113))
    def test_13(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 114))  
    def test_14(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[1,2,3,4,2]", "[,1,,,2,,,3,,,4,,,2,],<EOF>", 115))      
    def test_15(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[2.3, 4.2, 102e3]", "[,2.3,,,4.2,,,102e3,],<EOF>", 116))     
    def test_16(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[1.32,true,3,4,2]", "[,1.32,,,true,,,3,,,4,,,2,],<EOF>", 117)) 
    def test_17(self):
        """test aray"""
        self.assertTrue(TestLexer.test("[1.32,true,\"het cuu \",4,2]", "[,1.32,,,true,,,het cuu ,,,4,,,2,],<EOF>", 118))  
    def test_18(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\n", "<EOF>", 119))
    def test_19(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("a := 5;//this is a line comment\n", "a,:=,5,;,<EOF>", 120))
    def test_20(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("//abcd\nabc", "abc,<EOF>", 121))
    def test_21(self):
        """test float"""
        self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 122))
    def test_22(self):
        """test float"""
        self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 123))
    def test_23(self):
        """test float"""
        self.assertTrue(TestLexer.test(".12", ".,12,<EOF>", 124))        
    def test_24(self):
        """test float"""
        self.assertTrue(TestLexer.test("143e ", "143,e,<EOF>", 125))
    def test_25(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"", "Unclosed String: He asked me: \\\"Where is John?\\\"", 126))
    def test_26(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("\"This is a error string \n", "Unclosed String: This is a error string ", 127))
    def test_27(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("a : \" Pham Trong Son \n", "a,:,Unclosed String:  Pham Trong Son ", 128))
    def test_28(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("_mynameisson:=\"I got skill issue \b", "_mynameisson,:=,Unclosed String: I got skill issue ", 129))
    def test_29(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("\"using operate on string\" ^ \"this is a wrong string\'\\\\\\try to write a comment", "using operate on string,^,Unclosed String: this is a wrong string'\\\\\\try to write a comment", 130))
    def test_30(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test("@son= \"this string is at the end of the file", "@son,=,Unclosed String: this string is at the end of the file", 131))
    def test_31(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("\"this is a illegal escape\\", "Illegal Escape In String: this is a illegal escape\\", 132))
    def test_32(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("a : \" Pham Trong Son \o", "a,:,Illegal Escape In String:  Pham Trong Son \o", 133))
    def test_33(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("_mynameisson:=\"I got skill issue \ ", "_mynameisson,:=,Illegal Escape In String: I got skill issue \ ", 134))
    def test_34(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("\"using operate on string\" ^ \"this is a wrong string \\a \\\\try to write a comment", "using operate on string,^,Illegal Escape In String: this is a wrong string \\a", 135))
    def test_35(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test("\"This is illegal, dont escape me: \\g", "Illegal Escape In String: This is illegal, dont escape me: \\g", 136))
    def test_36(self):
        """test separator"""
        self.assertTrue(TestLexer.test("( ) [ ] . , ; : { }", "(,),[,],.,,,;,:,{,},<EOF>", 137))
    def test_37(self):
        """test separator"""
        self.assertTrue(TestLexer.test(".,.,....,.", ".,,,.,,,.,.,.,.,,,.,<EOF>", 138))
    def test_38(self):
        """test separator"""
        self.assertTrue(TestLexer.test("{{][#]}}", "{,{,],[,Error Token #", 139))
    def test_39(self):
        """test separator"""
        self.assertTrue(TestLexer.test("::=:==",":,:=,:=,=,<EOF>" , 140)) 
    def test_40(self):
        """test separator"""
        self.assertTrue(TestLexer.test("{{][]}}", "{,{,],[,],},},<EOF>", 141))
    def test_41(self):
        """test linecomment"""
        
        self.assertTrue(TestLexer.test("@as23", "@as23,<EOF>", 142))
    def test_42(self):
        """test linecomment"""
        input = """class Program {func main():  void {
            const x, y: int = 2, 3,3;
        }
}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,const,x,,,y,:,int,=,2,,,3,,,3,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))
    def test_43(self):
        """test linecomment"""
        input = """class Program {func main():  void {
            const x, y,z: int = 2, 3;
        }
}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,const,x,,,y,,,z,:,int,=,2,,,3,;,},},<EOF>"
        
        self.assertTrue(TestLexer.test(input, expect, 144))
    def test_44(self):
        """test linecomment"""
        input = """class Program {func main():  void {
           var  x, y, z: string = int, int, int ;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,const,x,,,y,,,z,:,int,=,2,,,3,;,},},<EOF>"

        self.assertTrue(TestLexer.test("a\r", "a,<EOF>", 145))
    def test_45(self):
        """test linecomment"""
        input = """class Program {func main():  void {
           var a: [5+5]int;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,var,a,:,[,5,+,5,],int,;,},},<EOF>"
        
        self.assertTrue(TestLexer.test(input, expect, 146))
    def test_46(self):
        """test linecomment"""
        input = """class Program {func main():  void {
           var a: [10]int;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,var,a,:,[,10,],int,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))
    def test_47(self):
        """test linecomment"""
        input = """class Program {func main():  void {
            const x, y: int = 2, 3;
            var a: [10]int;
            n := 5+2+3;
            c:= 5;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,const,x,,,y,:,int,=,2,,,3,;,var,a,:,[,10,],int,;,n,:=,5,+,2,+,3,;,c,:=,5,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))
    def test_48(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("b@c", "b,@c,<EOF>", 149))
    def test_49(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("\"Invalid \\z \\q\"", "Illegal Escape In String: Invalid \z", 150))
    def test_50(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("\"Hello\nWorld\"", "Unclosed String: Hello", 151))
    def test_51(self):
        """test linecomment"""
        self.assertTrue(TestLexer.test("\"Hello\\nWorld\"", "Hello\\nWorld,<EOF>", 152))
    def test_52(self):
        """test linecomment"""
        input = """class Program {
            func @main():int {
                @isSth := !a.x[1] && b [2];
            }
        }
        """
        expect = "class,Program,{,func,@main,(,),:,int,{,@isSth,:=,!,a,.,x,[,1,],&&,b,[,2,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))
    def test_53(self):
        """test linecomment"""
        input = """class Program {
            func @main():int {
                @text := !(a && b);
            }
        }
        """
        expect = "class,Program,{,func,@main,(,),:,int,{,@text,:=,!,(,a,&&,b,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))
    def test_54(self):
        """test linecomment"""
        input = """class A <- B{func X(): int {a[3+x.foo(2)] := a[b[2]] +3;}}
        """
        expect = "class,A,<-,B,{,func,X,(,),:,int,{,a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))
    def test_55(self):
        """test linecomment"""
        input = """class Program {func main():void {
            const a: int = 3;
            const b: int = 4;
            var c: int = b % a + 4;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,const,a,:,int,=,3,;,const,b,:,int,=,4,;,var,c,:,int,=,b,%,a,+,4,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))
    def test_56(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,double,(,lst,:,int,),:,int,{,if,@len,(,lst,),==,0,{,return,null,;,},var,i,:,int,=,lst,[,0,],;,return,(,[,a,],+,self,.,double,(,lst,[,12,],),),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))
    def test_57(self):
        """test linecomment"""
        input = """class Program {func main():void {
            a[3+x.foo(2)] := a[b[2]] +3;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))
    def test_58(self):
        """test linecomment"""
        input = """class Program {const a: int = 4;
        func main(): void {
            a := true || false && true;
        }}
        """
        expect = "class,Program,{,const,a,:,int,=,4,;,func,main,(,),:,void,{,a,:=,true,||,false,&&,true,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))
    def test_59(self):
        """test linecomment"""
        input = """class Program {
        func @main(): void {
            var a : [5]float;
            a[44 && 5 + 1] := ["DF",1,2];
        }}
        """
        expect = "class,Program,{,func,@main,(,),:,void,{,var,a,:,[,5,],float,;,a,[,44,&&,5,+,1,],:=,[,DF,,,1,,,2,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))
    def test_60(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if true {a := a + 1;}
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,true,{,a,:=,a,+,1,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
    def test_61(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if true {a := a + 1;}
            else {a := a - 1;}
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,true,{,a,:=,a,+,1,;,},else,{,a,:=,a,-,1,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))
    def test_62(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,==,1,{,return,a,==,1,;,},else,{,return,a,==,1,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))
    def test_63(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,+,4,==,5,{,return,a,+,1,;,},else,{,if,a,+,1,==,3,{,return,a,+,1,;,},return,a,+,2,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))
    def test_64(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,>,4,{,return,a,+,1,;,},if,a,>,3,{,return,12,;,},if,a,==,1,{,return,5,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))
    def test_65(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if else a = 3 ;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,else,a,=,3,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))
    def test_66(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if a <= 1
                {a := 1;}
            return 0;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,<=,1,{,a,:=,1,;,},return,0,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))
    def test_67(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            for i := 0; i < 10; i := i + 1 {
            io.@writeInt(i);
            }
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,for,i,:=,0,;,i,<,10,;,i,:=,i,+,1,{,io.,@writeInt,(,i,),;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))
    def test_68(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            for i := 0; i + 1; {
                io.@writeInt(i);
            }
        }}

        """
        expect = "class,Program,{,func,main,(,),:,void,{,for,i,:=,0,;,i,+,1,;,{,io.,@writeInt,(,i,),;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))
    def test_69(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            for a := 1; 10; a:=i + 2{
                io.@writeInt(i);
            }
        }}"""
        expect = "class,Program,{,func,main,(,),:,void,{,for,a,:=,1,;,10,;,a,:=,i,+,2,{,io.,@writeInt,(,i,),;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))
    def test_70(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            var a: [2] int;
            for index := 0; index < 10; index:= index + 1 {
                if a[index] == i
                   { break ; }
        }}}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,var,a,:,[,2,],int,;,for,index,:=,0,;,index,<,10,;,index,:=,index,+,1,{,if,a,[,index,],==,i,{,break,;,},},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))
    def test_71(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            var a: [2] int;
            for index := 0; index < 10; index:=index + 1 {
                a[index] := 5;
            }
            break;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,var,a,:,[,2,],int,;,for,index,:=,0,;,index,<,10,;,index,:=,index,+,1,{,a,[,index,],:=,5,;,},break,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))
    def test_72(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if a == i {
                    continue gogo;
            }
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,==,i,{,continue,gogo,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))
    def test_73(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if a == i {
                    continue;
            }
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,==,i,{,continue,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))
    def test_74(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if a == i {
                continue;
                continue;
            }
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,==,i,{,continue,;,continue,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))
    def test_75(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
            if a == i {
                continue;
                break;
            }
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,if,a,==,i,{,continue,;,break,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))
    def test_76(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
             return metquadithoi;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,return,metquadithoi,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))
    def test_77(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
             return int;
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,return,int,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 178))
    def test_78(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
             return @foo(3 + x, 4.0 / y);
        }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,return,@foo,(,3,+,x,,,4.0,/,y,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))
    def test_79(self):
        """test linecomment"""
        input = """ class Program {
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,var,test,:,int,=,1,;,return,test,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180))
    def test_80(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int ;
            a[1]:=2;
            a[2]:="why";
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "class,Program,{,var,a,:,[,2,],int,;,a,[,1,],:=,2,;,a,[,2,],:=,why,;,func,main,(,),:,void,{,var,test,:,int,=,1,;,return,test,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))
    def test_81(self):
        """test linecomment"""
        input = """class Program {
            func @main():int {
                @text := "Hello" ^ 1;
            }
        }
        """
        expect = "class,Program,{,func,@main,(,),:,int,{,@text,:=,Hello,^,1,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))
    def test_82(self):
        """test linecomment"""
        input = """class Program {
        func main(): void {
                var test: void = 1;
                return test;
            }}
        """
        expect = "class,Program,{,func,main,(,),:,void,{,var,test,:,void,=,1,;,return,test,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))
    def test_83(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int = 2,"why not";
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "class,Program,{,var,a,:,[,2,],int,=,2,,,why not,;,func,main,(,),:,void,{,var,test,:,int,=,1,;,return,test,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
    def test_84(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,thieuDusk,(,n,:,niga,),:,void,{,@text,:=,@text,+,nian,;,for,i,:=,0,;,i,<,@thieuSuzu,(,),;,i,:=,i,+,1,{,if,{,@x,:=,0,;,},_test,>,i,{,_test,:=,_test,-,@_,;,},else,{,@_,:=,@_,+,1,;,},},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))
    def test_85(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
        func main(): void {
                var test: int = 1;
                return test;
            }}
        """
        expect = "class,Program,{,var,a,:,[,2,],int,=,[,2,,,why not,],;,func,main,(,),:,void,{,var,test,:,int,=,1,;,return,test,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 186))
    def test_86(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2];
        }}
        """
        expect = "class,Program,{,var,a,:,[,2,],int,=,[,2,,,why not,],;,func,@main,(,),:,void,{,a,[,1,],,,a,[,2,],:=,[,1,,,2,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))
    def test_87(self):
        """test linecomment"""
        input = """class Program {
            var a: [2][2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2] ,[2,3];
        }}
        """
        expect = "class,Program,{,var,a,:,[,2,],[,2,],int,=,[,2,,,why not,],;,func,@main,(,),:,void,{,a,[,1,],,,a,[,2,],:=,[,1,,,2,],,,[,2,,,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))
    def test_88(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2] ,[2,3];
        }}
        """
        expect = "class,Program,{,var,a,:,[,2,],int,=,[,2,,,why not,],;,func,@main,(,),:,void,{,a,[,1,],,,a,[,2,],:=,[,1,,,2,],,,[,2,,,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))
    def test_89(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[a[2]] := [1,2] ,[2,3];
        }}"""
        expect = "class,Program,{,var,a,:,[,2,],int,=,[,2,,,why not,],;,func,@main,(,),:,void,{,a,[,a,[,2,],],:=,[,1,,,2,],,,[,2,,,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))
    def test_90(self):
        """test linecomment"""
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[a[2]] := [2,3];
        }}
        """
        expect = "class,Program,{,var,a,:,[,2,],int,=,[,2,,,why not,],;,func,@main,(,),:,void,{,a,[,a,[,2,],],:=,[,2,,,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))
    def test_91(self):
        """test linecomment"""
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
        expect = "class,Program,{,var,a,:,[,2,],int,=,[,2,,,why not,],;,func,@main,(,),:,void,{,a,[,a,[,2,],],:=,[,2,,,3,],;,},},class,toidaudon,<-,Program,{,func,@main,(,),:,void,{,x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))
    def test_92(self):
        """test linecomment"""
        input = """class toidaudon <- Program{
                func @main():void{
                a[3+x.foo(2)] := a[b[2]] +3;
                }
            }
        """
        expect = "class,toidaudon,<-,Program,{,func,@main,(,),:,void,{,a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))
    def test_93(self):
        """test linecomment"""
        input = """class @toidaudon <- Program{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "class,@toidaudon,<-,Program,{,func,@main,(,),:,void,{,x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))
    def test_94(self):
        """test linecomment"""
        input = """class toidaudon <- @Program{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "class,toidaudon,<-,@Program,{,func,@main,(,),:,void,{,x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))
    def test_95(self):
        """test linecomment"""
        input = """class toidaudon <- Program, Nworld{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "class,toidaudon,<-,Program,,,Nworld,{,func,@main,(,),:,void,{,x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))
    def test_96(self):
        """test linecomment"""
        input = """class toidaudon <- Program <- Nworld{
                func @main():void{
                x.b[2] := x.m()[3];}
            }
        """
        expect = "class,toidaudon,<-,Program,<-,Nworld,{,func,@main,(,),:,void,{,x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))
    def test_97(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,railfence,(,ciphertext,:,string,,,key,:,integer,),:,string,{,if,key,<=,1,{,return,ciphertext,;,},var,matrix,:,[,15,],string,;,for,i,:=,0,;,i,<,15,;,i,:=,i,+,1,{,var,matrix_a,:,[,15,],string,;,},var,dir,:,bool,=,true,;,var,row,,,col,:,int,=,0,,,0,;,for,i,:=,0,;,i,<,@length,(,ciphertext,),;,i,:=,i,+,1,{,if,row,==,0,{,dir,:=,true,;,},if,row,==,key,-,1,{,dir,:=,false,;,},rail,[,row,],:=,null,;,col,:=,col,+,1,;,if,dir,{,row,:=,row,+,1,;,},else,{,row,:=,row,-,1,;,},},var,index,:,int,=,0,;,for,i,:=,0,;,i,<,key,;,i,:=,i,+,1,{,for,j,:=,0,;,j,<,a,.,length,(,ciphertext,),;,j,:=,j,+,1,{,if,matrix,[,i,],==,null,&&,(,index,<,as,.,length,(,ciphertext,),),{,matrix,[,i,],:=,ciphertext,[,index,],;,index,:=,index,+,1,;,},},row,:=,0,;,col,:=,0,;,var,result,:,string,;,for,i,:=,0,;,i,<,@length,(,ciphertext,),;,i,:=,i,+,1,{,if,row,==,0,{,dir,:=,true,;,},if,row,==,key,-,1,{,dir,:=,false,;,},if,rail,[,row,],!=,*,{,result,:=,result,.,rail,[,col,],;,},col,:=,col,+,1,;,if,dir,{,row,:=,row,+,1,;,},else,{,row,:=,row,-,1,;,},},return,result,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))
    def test_98(self):
        """test linecomment"""
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
        expect = "class,Program,{,func,railfence,(,plain,:,string,,,key,:,integer,),:,string,{,if,key,<=,1,{,return,plain,;,},var,matrix,:,[,15,],string,;,var,row,,,dir,:,int,=,0,,,-,1,;,for,i,:=,0,;,i,<,@length,(,plain,),;,i,:=,i,+,1,{,if,(,j,==,key,-,1,),||,(,j,==,0,),{,dir,:=,dir,*,-,1,;,},matrix,[,j,],:=,plain,[,i,],;,if,dir,==,1,{,j,:=,j,+,1,;,},else,{,j,:=,j,-,1,;,},},var,ciphertext,:,string,;,for,i,:=,0,;,i,<,key,;,i,:=,i,+,1,{,ciphertext,:=,ciphertext,.,matrix,[,i,],;,},return,ciphertext,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
    def test_99(self):
        """test linecomment"""
        input = """class Program {
        func jowd(): string {
            if true  {
                a[5] := a[1] + 2;
                b[9] := b[5] || false;
            } else;
        }
            }
        """
        expect = "class,Program,{,func,jowd,(,),:,string,{,if,true,{,a,[,5,],:=,a,[,1,],+,2,;,b,[,9,],:=,b,[,5,],||,false,;,},else,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 100))
    def test_missing_one(self):
        """test linecomment"""
        input = """class Program <- test{
            var x: int = 65;
            func @fact(n: int):void {
                (new X("sd"^"w")).haha()[2]:=(new X("sd"^"w")).haha()[2];
            }
        }
        """
        expect = "class,Program,<-,test,{,var,x,:,int,=,65,;,func,@fact,(,n,:,int,),:,void,{,(,new,X,(,sd,^,w,),),.,haha,(,),[,2,],:=,(,new,X,(,sd,^,w,),),.,haha,(,),[,2,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 400))
