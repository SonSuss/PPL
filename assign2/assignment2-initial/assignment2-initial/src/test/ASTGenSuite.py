import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {
            var a :int;
            }"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_case_03(self):
        input = """class vardecl {
            var a,b:int;
        }
        """
        expect=str(Program([ClassDecl(Id("vardecl"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_case_04(self):
        input = """class vardecl {
            var a,b,c:int;
            var d:float;
        }
        """
        expect=str(Program([ClassDecl(Id("vardecl"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("d"),FloatType()))])]))
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_case_05(self):
        """test const declarations """
        input = """class main{
            const a:int;
        }
        """
        expect=str(Program([ClassDecl(Id("main"),[AttributeDecl(ConstDecl(Id("a"),IntType(),None))])]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_case_06(self):
        """test case """
        input ="""class main {
            var a:float = 1;
        }
        """
        expect =str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),FloatType(),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_case_07(self):
        input = """class main {
            var a,b,c:int = 1,2,3;
        }
        """
        expect=str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(1))),AttributeDecl(VarDecl(Id("b"),IntType(),IntLiteral(2))),AttributeDecl(VarDecl(Id("c"),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_case_08(self):
        input = """class main {
            var a :int;
            var a,b:int=1,d;
            const c:string="konbanwa";
        }
        """
        expect=str(Program([ClassDecl(Id("main"),
        [AttributeDecl(VarDecl(Id("a"),IntType())),
        AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(1))),
        AttributeDecl(VarDecl(Id("b"),IntType(),Id("d"))),
        AttributeDecl(ConstDecl(Id("c"),StringType(),StringLiteral("konbanwa"))),
        ])]))
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_case_09(self):
        input = """class object<-main { 
        const x, y, z: int = 1, 2, 3;
        var a, b: float;
        }"""
        expect=str(Program([ClassDecl(Id("main"),[AttributeDecl(ConstDecl(Id("x"),IntType(),IntLiteral(1))),AttributeDecl(ConstDecl(Id("y"),IntType(),IntLiteral(2))),AttributeDecl(ConstDecl(Id("z"),IntType(),IntLiteral(3))),AttributeDecl(VarDecl(Id("a"),FloatType())),AttributeDecl(VarDecl(Id("b"),FloatType()))],
                                      Id("object"))]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_case_10(self):
        input = """class main{ func a(): void {}}"""
        expect=str(Program([ClassDecl(Id("main"),
                                    [MethodDecl(Id("a"),
                                                [],
                                                VoidType(),
                                                Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_case_11(self):
        input = """class main{
        func foo  (a: int, b: float):void {}
        func @main():void{
            io.printInt(4);
        }}
        """
        expect=str(Program([ClassDecl(Id("main"),
                                      [MethodDecl(Id("foo"),
                                                  [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],
                                                  VoidType(),
                                                  Block([])),
                                       MethodDecl(Id("@main"),[],VoidType(),
                                                  Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,311))    
    
    def test_case_12(self):
        input = """
        """
        expect=str(Program([]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_case_13(self):
        input = """class Shape {
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
        expect=str(Program([ClassDecl(Id("Shape"),
                                      [AttributeDecl(VarDecl(FieldAccess(None,Id("@numOfShape")),
                                                             IntType(),
                                                             IntLiteral(0))),
                                       AttributeDecl(ConstDecl(Id("immutableAttribute"),
                                                               IntType(),
                                                               IntLiteral(0))),
                                       AttributeDecl(VarDecl(Id("length"),
                                                             IntType())),
                                       AttributeDecl(VarDecl(Id("width"),
                                                               IntType())),
                                       MethodDecl(Id("@getNumOfShape"),
                                                  [],
                                                  IntType(),Block([Return(FieldAccess(None,Id("@numOfShape")))])
                                            )]),
                            ClassDecl(Id("Retangle"),
                                      [MethodDecl(Id("getArea"),
                                                  [],
                                                  IntType(),
                                                  Block([Return(BinaryOp("*",
                                                                         FieldAccess(SelfLiteral(),Id("length")),
                                                                         FieldAccess(SelfLiteral(),Id("width"))))]))],
                                      Id("Shape")),
                            ClassDecl(Id("Program"),
                                         [MethodDecl(Id("@main"),[],VoidType(),
                                                     Block([CallStmt(Id("io"),
                                                                     Id("@writeInt"),
                                                                     [FieldAccess(Id("Shape"),Id("@numOfShape"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_case_14(self):
        input = """class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape(): int {
            return @numOfShape;
            }
            }
        """
        expect=str(Program([ClassDecl(Id("Shape"),
                                      [AttributeDecl(VarDecl(FieldAccess(None,Id("@numOfShape")),
                                                             IntType(),
                                                             IntLiteral(0))),
                                       AttributeDecl(ConstDecl(Id("immutableAttribute"),
                                                               IntType(),
                                                               IntLiteral(0))),
                                       AttributeDecl(VarDecl(Id("length"),
                                                             IntType())),
                                       AttributeDecl(VarDecl(Id("width"),
                                                               IntType())),
                                       MethodDecl(Id("@getNumOfShape"),
                                                  [],
                                                  IntType(),Block([Return(FieldAccess(None,Id("@numOfShape")))])
                                            )])]))
        self.assertTrue(TestAST.test(input,expect,314))
        
    def test_case_15(self):
        input = """
                    class Shape <- Retangle {
            func getArea():int {
            return self.length * self.width ;
            }
            }
        """
        expect=str(Program([ClassDecl(Id("Retangle"),
                                      [MethodDecl(Id("getArea"),
                                                  [],
                                                  IntType(),
                                                  Block([Return(BinaryOp("*",
                                                                         FieldAccess(SelfLiteral(),Id("length")),
                                                                         FieldAccess(SelfLiteral(),Id("width"))))]))],
                                      Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_case_16(self):
        input = """class Program {
            func @main():void {
            io.@writeInt(Shape.@numOfShape);
            }
            }
        """
        expect=str(Program([ClassDecl(Id("Program"),
                                         [MethodDecl(Id("@main"),[],VoidType(),
                                                     Block([CallStmt(Id("io"),
                                                                     Id("@writeInt"),
                                                                     [FieldAccess(Id("Shape"),Id("@numOfShape"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,316))
        
    def test_case_17(self):
        input = """class Program {
            func main(): void{
                a := [1,3,4,5];
            }
            }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#1,3,4,5
                                                                [],
                                                                VoidType(),
                                                                Block([
                                                                    Assign(Id("a"),ArrayLiteral([IntLiteral(1),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_case_18(self):
        input = """class Program {
             func main(): void{
                 var a : [5]int;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),
                                                                [],
                                                                VoidType(),
                                                                Block([VarDecl(Id("a"),ArrayType(5,IntType()))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_case_19(self):
        input = """class Program {
             func main(): void{
                 var a,b : [5]int = [1],[2];
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),
                                                                [],
                                                                VoidType(),
                                                                Block([VarDecl(Id("a"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1)])),
                                                                       VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(2)]))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,319))
    
    
    def test_case_20(self):
        input = """class Program {
             func main(): int{
                var a : [5]int = b;
                const a : string = 10;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#var a : [5]int = b;const a : string = 10;
                                                                [],
                                                                IntType(),
                                                                Block([VarDecl(Id("a"),ArrayType(5,IntType()),Id("b")),
                                                                       ConstDecl(Id("a"),StringType(),IntLiteral(10))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,320))
        
    def test_case_21(self):
        input = """class Program {
             func main(): int{
                var a : a = new a();
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#var a : [5]int = b;const a : string = 10;
                                                                [],
                                                                IntType(),
                                                                Block([VarDecl(Id("a"),ClassType(Id("a")),NewExpr(Id("a"),[])),
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,321))
        
    def test_case_22(self):
        input = """class Program {
             func main(): int{
                a := @a;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := @a;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),FieldAccess(None,Id("@a")))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_case_23(self):
        input = """class Program {
             func main(): int{
                a := a.@a;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a.@a;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),FieldAccess(Id("a"),Id("@a")))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_case_24(self):
        input = """class Program {
             func main(): int{
                a := @a(123,a);
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := @a(123,a);
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),CallExpr(None,Id("@a"),[IntLiteral(123),Id("a")]))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_case_25(self):
        input = """class Program {
             func main(): int{
                a := a.@a(123,a);
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a.@a(123,a);
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),CallExpr(Id("a"),Id("@a"),[IntLiteral(123),Id("a")]))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_case_26(self):
        input = """class Program {
             func main(): int{
                a := @a(1,2).b ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := @a(1,2).b ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),FieldAccess(CallExpr(None,Id("@a"),[IntLiteral(1),IntLiteral(2)]),
                                                                                               Id("b")))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_case_27(self):
        input = """class Program {
             func main(): int{
                a := a.@a(1,2).b ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := @a(1,2).b ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),FieldAccess(CallExpr(Id("a"),Id("@a"),[IntLiteral(1),IntLiteral(2)]),
                                                                                               Id("b")))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,327))
    
    def test_case_29(self):
        input = """class Program {
             func main(): int{
                a := d.c.b.a(1,2).b ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a := d.c.b.a(1,2).b ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),FieldAccess(CallExpr(FieldAccess(FieldAccess(Id("d"),Id("c")),Id("b")),Id("a"),[IntLiteral(1),IntLiteral(2)]),
                                                                                               Id("b")))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,329))
        
    def test_case_30(self):
        input = """class Program {
             func main(): int{
                a := @a(1,2).b() ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := @a(1,2).b() ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),CallExpr(CallExpr(None,Id("@a"),[IntLiteral(1),IntLiteral(2)]),Id("b"),[]))
                                                                       ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_case_31(self):
        input = """class Program {
             func main(): int{
                a := a[b] ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a[b[1+2+3]] ; a := a[b] ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),ArrayCell(Id("a"),Id("b"))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_case_32(self):
        input = """class Program {
             func main(): int{
                a := a[b[c]] ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a[b[1+2+3]] ;  a := a[b[c]] ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("b"),Id("c")))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test_case_33(self):
        input = """class Program {
             func main(): int{
                a := a[b[c]] ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a[b[1+2+3]] ;  a := a[b[c]] ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("b"),Id("c")))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,333))
        
    def test_case_34(self):
        input = """class Program {
             func main(): int{
                a := a[b[1+2+3]] ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a[b[1+2+3]] ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("b"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3))))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_case_35(self):
        input = """class Program {
             func main(): int{
                a := x.m()[3];
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := x.m()[3];
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(3))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,335))
    
    def test_case_36(self):
        input = """class Program {
             func main(): int{
                a := @a(1,2,3)[3];
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# @a(1,2,3)[3];
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),ArrayCell(CallExpr(None,Id("@a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),IntLiteral(3))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_case_37(self):
        input = """class Program {
             func main(): int{
                a := -1;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := -1;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),UnaryOp("-",IntLiteral(1))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,337))
        
    def test_case_38(self):
        input = """class Program {
             func main(): int{
                a := ----2;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := ----2;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(2)))))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_case_39(self):
        input = """class Program {
             func main(): int{
                a := --a[1+1];
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := --a[1+1];
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),UnaryOp("-",UnaryOp("-",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1)))))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_case_40(self):
        input = """class Program {
             func main(): int{
                a := !a ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := !a ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),UnaryOp("!",Id("a"))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_case_41(self):
        input = """class Program {
             func main(): int{
                a := !!a ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := !!a ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),UnaryOp("!",UnaryOp("!",Id("a")))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,341))
        
    def test_case_42(self):
        input = """class Program {
             func main(): int{
                a := !!-a.a(1)[1] ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := !!-a.a(1)[1] ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),UnaryOp("!",UnaryOp("!",UnaryOp("-",ArrayCell(CallExpr(Id("a"),Id("a"),[IntLiteral(1)]),IntLiteral(1)))))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_case_43(self):
        input = """class Program {
             func main(): int{
                a := 1*1/2;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := 1*1/2;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("/",BinaryOp("*",IntLiteral(1),IntLiteral(1)),IntLiteral(2))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_case_44(self):
        input = """class Program {
             func main(): int{
                a := 1.*1/2;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := 1*1/2;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("/",BinaryOp("*",FloatLiteral(1.),IntLiteral(1)),IntLiteral(2))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_case_45(self):
        input = """class Program {
             func main(): int{
                a := 1.2* 3 + 1 - 2%3 + a.@a;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a := 1.2* 3 + 1 - 2%3 + a.@a;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("+",
                                                                                               BinaryOp("-",
                                                                                                        BinaryOp("+",
                                                                                                                 BinaryOp("*",
                                                                                                                          FloatLiteral(1.2),IntLiteral(3)),
                                                                                                                 IntLiteral(1)),
                                                                                                        BinaryOp("%",
                                                                                                                 IntLiteral(2),
                                                                                                                 IntLiteral(3))),
                                                                                               FieldAccess(Id("a"),Id("@a")))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,345))
    
    def test_case_46(self):
        input = """class Program {
             func main(): int{
                a :=  a || b ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a := a ||b ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("||",Id("a"),Id("b"))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,346))
    
    def test_case_47(self):
        input = """class Program {
             func main(): int{
                a :=  1 <= 2 ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a :=  1 <= 2 ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("<=",IntLiteral(1),IntLiteral(2))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_case_48(self):
        input = """class Program {
             func main(): int{
                a :=  a || 1==2 ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a :=  a || 1==2 ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("==",BinaryOp("||",Id("a"),IntLiteral(1)),IntLiteral(2))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_case_49(self):
        input = """class Program {
             func main(): int{
                a :=  (a.abc != 1) + 2 ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a :=  (a.abc != 1) + 2 ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("+",
                                                                                               BinaryOp("!=",
                                                                                                        FieldAccess(Id("a"),Id("abc")),
                                                                                                        IntLiteral(1)),
                                                                                               IntLiteral(2))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_case_50(self):
        input = """class Program {
             func main(): int{
                a :=  a.abc != 1 + 2 ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a :=  a.abc != 1 + 2 ;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("!=",
                                                                                               FieldAccess(Id("a"),Id("abc")),
                                                                                               BinaryOp("+",IntLiteral(1),IntLiteral(2)))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_case_51(self):
        input = """class Program {
             func main(): int{
                a :=  "thangmlbanso1" ^ "monvkl,cothecammomduockhong";
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a :=  "thangmlbanso1" ^ "monvkl,cothecammomduockhong";
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("^",StringLiteral("thangmlbanso1"),StringLiteral("monvkl,cothecammomduockhong"))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_case_52(self):
        input = """class Program {
             func main(): int{
                a :=  a.a(1,a + (2+3) *4 && 7) ^ "monvkl,cothecammomduockhong";
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a :=  a.a(1,a + (2+3) *4 && 7) ^ "monvkl,cothecammomduockhong";
                                                                [],
                                                                IntType(),
                                                                Block([Assign(Id("a"),BinaryOp("^",CallExpr(Id("a"),Id("a"),[IntLiteral(1),BinaryOp("&&",BinaryOp("+",Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),IntLiteral(4))),IntLiteral(7))]),
                                                                                               StringLiteral("monvkl,cothecammomduockhong"))
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_case_53(self):
        input = """class Program {
             func main(): int{
                @a := 1;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# @a := 1;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(FieldAccess(None,Id("@a")),IntLiteral(1)
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_case_54(self):
        input = """class Program {
             func main(): int{
                a.a[3] := 1;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a.a[3] := 1;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(ArrayCell(FieldAccess(Id("a"),Id("a")),IntLiteral(3)),IntLiteral(1)
                                                                       )])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_case_55(self):
        input = """class Program {
             func main(): int{
                io.@writeInt(1+2);
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  io.@writeInt(1+2);
                                                                [],
                                                                IntType(),
                                                                Block([CallStmt(Id("io"),
                                                                                Id("@writeInt"),
                                                                                [BinaryOp("+",IntLiteral(1),IntLiteral(2))])])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,355))
        
    def test_case_56(self):
        input = """class Program {
             func main(): int{
                @a() ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# @a() ;
                                                                [],
                                                                IntType(),
                                                                Block([CallStmt(None,Id("@a"),[])
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_case_57(self):
        input = """class Program {
             func main(): int{
                a.@a(1,2) ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# a.@a(1,2) ;
                                                                [],
                                                                IntType(),
                                                                Block([CallStmt(Id("a"),Id("@a"),[IntLiteral(1),IntLiteral(2)])
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_case_58(self):
        input = """class Program {
             func main(): int{
                @a(1,2) ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# @a(1,2) ;
                                                                [],
                                                                IntType(),
                                                                Block([CallStmt(None,Id("@a"),[IntLiteral(1),IntLiteral(2)])
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_case_59(self):
        input = """class Program {
             func main(): int{
                a[1].b();
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#a[1].b();
                                                                [],
                                                                IntType(),
                                                                Block([CallStmt(ArrayCell(Id("a"),IntLiteral(1)),Id("b"),[])
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_case_60(self):
        input = """class Program {
             func main(): int{
                a[1].b()[2].a();
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a[1].b()[2].a();
                                                                [],
                                                                IntType(),
                                                                Block([CallStmt(ArrayCell(CallExpr(ArrayCell(Id("a"),IntLiteral(1)),
                                                                                                   Id("b"),[]),
                                                                                          IntLiteral(2)),
                                                                                Id("a"),[])
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_case_61(self):
        input = """class Program {
             func main(): int{
                a[1].b := 2;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a[1].b := 2;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(FieldAccess(ArrayCell(Id("a"),IntLiteral(1)),Id("b")),IntLiteral(2))
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,361))
        
    def test_case_62(self):
        input = """class Program {
             func main(): int{
                a[1].a().b[2] := 2;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a[1].a().b[2] := 2;
                                                                [],
                                                                IntType(),
                                                                Block([Assign(ArrayCell(FieldAccess(CallExpr(ArrayCell(Id("a"),IntLiteral(1)),Id("a"),[]),Id("b")),IntLiteral(2))
                                                                              ,IntLiteral(2))
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_case_63(self):
        input = """class Program {
             func main(): int{
                break;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  a[1].a().b[2] := 2;
                                                                [],
                                                                IntType(),
                                                                Block([Break()
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,363))
        
    def test_case_64(self):
        input = """class Program {
             func main(): int{
                return "alo";
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  return "alo";
                                                                [],
                                                                IntType(),
                                                                Block([Return(StringLiteral("alo"))
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_case_65(self):
        input = """class Program {
             func main(): int{
                return a.b() + 2 * 3;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  return a.b() + 2 * 3;
                                                                [],
                                                                IntType(),
                                                                Block([Return(BinaryOp("+",CallExpr(Id("a"),Id("b"),[]),BinaryOp("*",IntLiteral(2),IntLiteral(3))))
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_case_66(self):
        input = """class Program {
             func main(): int{
                return ;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  return ;
                                                                [],
                                                                IntType(),
                                                                Block([Return(None)
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_case_67(self):
        input = """class Program {
             func main(): int{
                continue;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  return ;
                                                                [],
                                                                IntType(),
                                                                Block([Continue()
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,367))
        
    def test_case_68(self):
        input = """class Program {
             func main(): int{
                for a:=0 ; a <1 ; a:=a+1 {}
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  for a:=0 ; a <1 ; a:=a+1 {}
                                                                [],
                                                                IntType(),
                                                                Block([For(Assign(Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(1)),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([]))
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_case_69(self):
        input = """class Program {
             func main(): int{
                for a:=0 ; a <1 ; a:=a+1 {
                    a[1].b := 2;
                    a := !a ;
                    @a(1,2) ;
                }
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),#  for a:=0 ; a <1 ; a:=a+1 {}
                                                                [],
                                                                IntType(),
                                                                Block([For(Assign(Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(1)),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Assign(FieldAccess(ArrayCell(Id("a"),IntLiteral(1)),Id("b")),IntLiteral(2)),
                                                                                                                                                                                                        Assign(Id("a"),UnaryOp("!",Id("a"))),
                                                                                                                                                                                                        CallStmt(None,Id("@a"),[IntLiteral(1),IntLiteral(2)])
                                                                    
                                                                ]))
                                                                    ])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_case_70(self):
        input = """class Program {
             func main(): int{
                if a < 1 {}
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# if a < 1 {}
                                                                [],
                                                                IntType(),
                                                                Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([]))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_case_71(self):
        input = """class Program {
             func main(): int{
                if a < 1 {} else {}
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# if a < 1 {} else {}
                                                                [],
                                                                IntType(),
                                                                Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([]),None,Block([]))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_case_72(self):
        input = """class Program {
             func main(): int{
                if {} a < 1 {} else {}
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# if {} a < 1 {} else {}
                                                                [],
                                                                IntType(),
                                                                Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([]),Block([]),Block([]))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_case_73(self):
        input = """class Program {
             func main(): int{
                var r, s: tnt;
                r := 2.0;
                var a, b: [5]int;
                s := r * r * self.myPI;
                a[0] := s;
             }
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),# var r, s: tnt; r := 2.0; var a, b: [5]int; 
                                                                [], #s := r * r * self.myPI; a[0] := s;
                                                                IntType(),
                                                                Block([VarDecl(Id("r"),ClassType(Id("tnt"))),
                                                                       VarDecl(Id("s"),ClassType(Id("tnt"))),
                                                                       Assign(Id("r"),FloatLiteral(2.0)),
                                                                       VarDecl(Id("a"),ArrayType(5,IntType())),
                                                                       VarDecl(Id("b"),ArrayType(5,IntType())),
                                                                       Assign(Id("s"),BinaryOp("*",BinaryOp("*",Id("r"),Id("r")),FieldAccess(SelfLiteral(),Id("myPI")))),
                                                                       Assign(ArrayCell(Id("a"),IntLiteral(0)),Id("s"))])),
                                                     ])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_case_74(self):
        input = """class Program {
             func main(): int{}
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],IntType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_case_75(self):
        input = """class Program {
             func @main(a:int,b:float): int{}
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],IntType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,375))
    
    def test_case_76(self):
        input = """class Program {
             func @main(a,b,c : int): int{}
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],IntType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,376))
        
    def test_case_77(self):
        input = """class Program {
             func constructor() {}
             }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("constructor"),[],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_case_78(self):
        input = """class Program {
            func constructor(a,b:int, c,d:Shape){}
        }
        """
        expect=str(Program([ClassDecl(Id("Program"),[MethodDecl(Id("constructor"), # a,b:int, c,d:Shape
                                                                [VarDecl(Id("a"),IntType()),
                                                                 VarDecl(Id("b"),IntType()),
                                                                 VarDecl(Id("c"),ClassType(Id("Shape"))),
                                                                 VarDecl(Id("d"),ClassType(Id("Shape")))],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,378))
        
    def test_case_79(self):
        input = """class main {
            func @test(a, b:int,t:[5]string):void{
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("@test"),
                    [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                        VarDecl(Id("t"),ArrayType(5,StringType()))
                    ],
                    VoidType(),
                    Block([])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_case_80(self):
        input = """class main {
            var a:string = t < 5;
            var b:string = t <= 5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp("<",Id("t"),IntLiteral(5))
                )),
                AttributeDecl(VarDecl(
                    Id("b"),
                    StringType(),
                    BinaryOp("<=",Id("t"),IntLiteral(5))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_case_81(self):
        input = """class main {
            var a:string = t > 5;
            var b:string = t >= 5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    BinaryOp(">",Id("t"),IntLiteral(5))
                )),
                AttributeDecl(VarDecl(
                    Id("b"),
                    StringType(),
                    BinaryOp(">=",Id("t"),IntLiteral(5))
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,381))


    def test_case_82(self):
        input = """class main {
            var a:string = a[2].t(1,2);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    CallExpr(
                        ArrayCell(
                            Id("a"),
                            IntLiteral(2)
                        ),
                        Id("t"),
                        [
                            IntLiteral(1),
                            IntLiteral(2)
                        ]
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_case_83(self):
        input = """class main {
            var a:string = Shape.@a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    FieldAccess(
                        Id("Shape"),
                        Id("@a")
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_case_84(self):
        input = """class main {
            var a:string = @a(2,5,6);
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    CallExpr(
                        None,
                        Id("@a"),
                        [
                            IntLiteral(2),
                            IntLiteral(5),
                            IntLiteral(6)
                        ]
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_case_85(self):
        input = """class main {
            var a:string = new Shape()[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        NewExpr(
                            Id("Shape"),
                            []
                        ),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_case_86(self):
        input = """class main {
            var a:string = ("temp"^"temp")[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        BinaryOp(
                            "^",
                            StringLiteral("temp"),
                            StringLiteral("temp")
                        ),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_case_87(self):
        input = """class main {
            var a:string = self.t[2];
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(VarDecl(
                    Id("a"),
                    StringType(),
                    ArrayCell(
                        FieldAccess(
                            SelfLiteral(),
                            Id("t")
                        ),
                        IntLiteral(2)
                    )
                ))
            ])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_case_88(self):
        input = """class main {
            func test():void{
                a:=new X().a[2].t[5+2];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            Id("a"),
                            ArrayCell(
                                FieldAccess(
                                    ArrayCell(
                                        FieldAccess(
                                            NewExpr(
                                                Id("X"),
                                                []
                                            ),
                                            Id("a")
                                        ),
                                        IntLiteral(2)
                                    ),
                                    Id("t")
                                ),
                                BinaryOp("+",IntLiteral(5),IntLiteral(2))
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_case_89(self):
        input = """class main {
            func test():void{
                Shape.a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            FieldAccess(
                                Id("Shape"),
                                Id("a")
                            ),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_case_90(self):
        input = """class main {
            const a:Temp = 5*2 + 1;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    ConstDecl(
                        Id("a"),
                        ClassType(Id("Temp")),
                        BinaryOp(
                            "+",
                            BinaryOp("*",IntLiteral(5),IntLiteral(2)),
                            IntLiteral(1)
                        )
                    )
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_case_91(self):
        input = """class main {
            func constructor(){
                for i:=1;false;i:=2{
                    if false{
                        return i+j;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        For(
                            Assign(
                                Id("i"),
                                IntLiteral(1)
                            ),
                            BooleanLiteral(False),
                            Assign(
                                Id("i"),
                                IntLiteral(2)
                            ),
                            Block([
                                If(
                                    BooleanLiteral(False),
                                    Block([
                                        Return(BinaryOp("+",Id("i"),Id("j")))
                                    ])
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_case_92(self):
        input = """class main {
            func constructor(){
                if true{
                    if false{
                        return 1;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        If(
                            BooleanLiteral(True),
                            Block([
                                If(
                                    BooleanLiteral(False),
                                    Block([
                                        Return(IntLiteral(1))
                                    ])
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_case_93(self):
        input = """class main {
            func constructor(){
                var a:string = "hi";
                for i:=1;false;j:=true{
                    @t();
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        VarDecl(Id("a"),StringType(),StringLiteral("hi")),
                        For(
                            Assign(
                                Id("i"),
                                IntLiteral(1)
                            ),
                            BooleanLiteral(False),
                            Assign(
                                Id("j"),
                                BooleanLiteral(True)
                            ),
                            Block([
                                CallStmt(
                                    None,
                                    Id("@t"),
                                    []
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_case_94(self):
        input = """class main {
            func constructor(){
                var t:int = null;
                var a:string = self;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        VarDecl(Id("t"),IntType(),NullLiteral()),
                        VarDecl(Id("a"),StringType(),SelfLiteral())
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_case_95(self):
        input = """class main {
            func test():void{}
            func constructor(){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [],
                    VoidType(),
                    Block([])
                ),
                MethodDecl(
                    Id("constructor"),
                    [],
                    VoidType(),
                    Block([
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_case_96(self):
        input = """class main {
            const a:Shape = new Shape(2);
            func test():void{}
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(ConstDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(2)]))),
                MethodDecl(Id("test"),[],VoidType(),Block([]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_case_97(self):
        input = """class main {
            func test():void{}
            func @io():int{
                return 1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [],
                    VoidType(),
                    Block([])
                ),
                MethodDecl(
                    Id("@io"),
                    [],
                    IntType(),
                    Block([
                        Return(IntLiteral(1))
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_case_98(self):
        input = """class main {
            var a:int;
            var b:string =5;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    VarDecl(Id("a"),IntType())
                ),
                AttributeDecl(
                    VarDecl(Id("b"),StringType(),IntLiteral(5))
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_case_99(self):
        input = """class main {
            func test():void{
                a[3+x.foo(2)] := a[b[2]]+3;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            ArrayCell(
                                Id("a"),
                                BinaryOp(
                                    "+",
                                    IntLiteral(3),
                                    CallExpr(
                                        Id("x"),
                                        Id("foo"),
                                        [IntLiteral(2)]
                                    )
                                )
                            ),
                            BinaryOp(
                                "+",
                                ArrayCell(
                                    Id("a"),
                                    ArrayCell(
                                        Id("b"),
                                        IntLiteral(2)
                                    )
                                ),
                                IntLiteral(3)
                            )
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,399))

    def test_case_100(self):
        input = """class main {
            func test():void{
                @getArea(Shape.check());
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        CallStmt(
                            None,
                            Id("@getArea"),
                            [
                                CallExpr(
                                    Id("Shape"),
                                    Id("check"),
                                    []
                                )
                            ]
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,400))