import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):
#     def test_redeclared_class(self):
#         """class a {} class Program {func @main() {}} class a {}"""
#         input = Program([ClassDecl(Id("a"),[]),
#                          ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))]),
#                          ClassDecl(Id("a"),[])])
#         expect = "Redeclared Class: a"
#         self.assertTrue(TestChecker.test(input,expect,400))
#     def test_redeclared_attribute(self):
#         """class Program {func @main() {}} class a {var a:int;var c:int;var c:int;}"""
#         input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))]),
#                          ClassDecl(Id("a"),[VarDecl(Id("a"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("c"),IntType())])])
#         expect = "Redeclared Attribute: c"
#         self.assertTrue(TestChecker.test(input,expect,401))
    
#     def test_redeclared_class_with_ast(self):
#         input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[]),
#                          ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))])])
#         expect = "Redeclared Class: a"
#         self.assertTrue(TestChecker.test(input,expect,402))
#     def test_redeclared_attribute_with_ast(self):
#         input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))]),
#                          ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
#         expect = "Redeclared Attribute: c"
#         self.assertTrue(TestChecker.test(input,expect,403))    
#     def test_method_redeclered_param_block(self): #need to fix after submit
#         """
#         Class a {
#             func a (a:int, b:int): int{
#                 var a : int =1 ;
#             }
#             }"""
#         input = Program([ClassDecl(Id('a'),[MethodDecl(Id("a"),
#                                                              [VarDecl(Id("a"),IntType()),
#                                                               VarDecl(Id("b"),IntType())],
#                                                              IntType(),
#                                                              Block([VarDecl(Id("a"),IntType(),IntLiteral(1))]))])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,404))
    
#     def test_method_redeclered(self):
#         """Class Program {
#             func a (a:int, b:int): int{}
#             func a (a:int, b:int): int{}
#             func @main (){}
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("a"),
#                                                              [VarDecl(Id("a"),IntType()),
#                                                               VarDecl(Id("b"),IntType())],
#                                                              IntType(),
#                                                              Block([])),
#                                                   MethodDecl(Id("a"),
#                                                              [VarDecl(Id("a"),IntType()),
#                                                               VarDecl(Id("b"),IntType())],
#                                                              IntType(),
#                                                              Block([])),
#                                                   MethodDecl(Id("@main"),[],VoidType(),Block([]))])])
#         expect = "Redeclared Method: a"
#         self.assertTrue(TestChecker.test(input,expect,405)) 
    
#     def test_for_redeclered(self):
#         """Class Program {
#             func @main (){
#                 for a:=1;a<10;a=a+1 {
#                     var a :int ;
#                     const a :int=1 ;
#                 }
#             }
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
#                                                              [],
#                                                              VoidType(),
#                                                              Block([For(Assign(Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
#                                                                         Block([VarDecl(Id("a"),IntType()),
#                                                                                ConstDecl(Id("a"),IntType(),IntLiteral(1))]))]))])])
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,406)) 
        
#     def test_if_redeclered(self):
#         """Class Program {
#             func @main (): int{
#                 if a < 0 {
#                     var a :int ;
#                     const a :int = 0;
#                 }
#             }
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
#                                                              [],
#                                                              VoidType(),
#                                                              Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),
#                                                                        Block([VarDecl(Id("a"),IntType()),
#                                                                               ConstDecl(Id("a"),IntType(),IntLiteral(0))]))]))])])
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,407))
        
#     def test_if_redeclered_prestmt(self):
#         """Class Program {
#             func @main (): int{
#                 if {const a: int =10; var a:int;} a < 0 {
#                     var a :int ;
#                 }
#             }
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
#                                                              [],
#                                                              VoidType(),
#                                                              Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),Block([VarDecl(Id("a"),IntType())]),
#                                                                        Block([ConstDecl(Id("a"),IntType(),IntLiteral(10)),VarDecl(Id("a"),IntType())]))]))])])
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,408))
        
#     def test_if_redeclered_elseStmt(self):
#         """Class Program {
#             func @main (): int{
#                 if a < 0 {
#                     var a :int ;
#                 }
#                 else {
#                     var b:int;
#                     const b:int;
#                 }
#             }
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
#                                                              [],
#                                                              VoidType(),
#                                                              Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),Block([VarDecl(Id("a"),IntType())]),None,Block([VarDecl(Id("b"),IntType()),ConstDecl(Id("b"),IntType(),None)]))]))])])
#         expect = "Type Mismatch In Declaration: ConstDecl(Id(b),IntType,None)"
#         self.assertTrue(TestChecker.test(input,expect,409))
        
#     def test_if_redeclered_prestmt_elseStmt(self):
#         """Class Program {
#             func @main (): int{
#                 if {const a: int =10} a < 0 {
#                     var b :int ;
#                 }
#                 else {
#                     var a:int ;
#                     coust a:int = 100;
#                 }
#             }
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
#                                                              [],
#                                                              VoidType(),
#                                                              Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),
#                                                                        Block([VarDecl(Id("b"),IntType())]),
#                                                                        Block([ConstDecl(Id("a"),IntType(),IntLiteral(10))]),
#                                                                        Block([VarDecl(Id("a"),IntType()),
#                                                                               ConstDecl(Id("a"),IntType(),IntLiteral(100))]))]))])])
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,410))
        
#     def test_no_entry_point_class(self):  
#         """ class a {} 
#             class b {}
#         """
#         input = Program([ClassDecl(Id('a'),[]),
#                          ClassDecl(Id('b'),[])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,411))

#     def test_no_entry_point_method(self):  
#         """ class a {} 
#             class Program {
#                 func a () : int {}
#             }
#         """
#         input = Program([ClassDecl(Id('a'),[]),
#                          ClassDecl(Id('Program'),[MethodDecl(Id("a"),[],IntType(),Block([]))])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,412))
        

#     def test_no_entry_point_method_atrribute_samename(self):  
#         """ class a {} 
#             class Program {
#                 var @main : int;
#             }
#         """
#         input = Program([ClassDecl(Id('a'),[]),
#                          ClassDecl(Id('Program'),[VarDecl(Id("@main"),IntType())])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,413))
        

#     def test_no_entry_point_method_param(self):  
#         """ class a {} 
#             class Program {
#                 func @main(a:int){}
#             }
#         """
#         input = Program([ClassDecl(Id('a'),[]),
#                          ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[VarDecl(Id("a"),IntType())],VoidType(),Block([]))])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,414))
    
#     def test_if_in_if(self):  
#         """ class a {} 
#             class Program {
#                 func @main(){
#                     if a < 5 {
#                         var a : int;
#                         if a ==10 {
#                             var a:int;
#                         }
#                         else {
#                             var a:int;
#                         }
#                         const a:int = 10;
#                     }
#                 }
#             }
#         """
#         input = Program([ClassDecl(Id('a'),[]),
#                          ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([
#                              If(BinaryOp("<",Id("a"),IntLiteral(5)),Block([
#                                  VarDecl(Id("a"),IntType()),
#                                  If(BinaryOp("==",Id("a"),IntLiteral(10)),
#                                     Block([VarDecl(Id("a"),IntType())]),None,
#                                     Block([VarDecl(Id("a"),IntType())]),),
#                                  ConstDecl(Id("a"),IntType(),IntLiteral(10))
#                              ])),
                             
#                          ]))])])
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,415))
        
#     def test_redeclered_io_class(self):  
#         """ class io {} 
#             class Program {
#                 func @main() : int {}
#             }
#         """
#         input = Program([ClassDecl(Id('io'),[]),
#                          ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))])])
#         expect = "Redeclared Class: io"
#         self.assertTrue(TestChecker.test(input,expect,416))

#     def test_class_program_papa(self):  
#         """ class io {} 
#             class io <- Program {
#                 func @main() : int {}
#             }
#         """
#         input = Program([ClassDecl(Id('io'),[]),
#                          ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("io"))])
#         expect = "Redeclared Class: io"
#         self.assertTrue(TestChecker.test(input,expect,417))
        
#     def test_entry_not_voidtype(self):  
#         """ class io <- Program {
#                 func @main():int {}
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],IntType(),Block([]))],Id("io"))])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,418))
    
#     def test_for_in_for_redeclered(self):
#         """ class Program {
#                 func @main(){
#                     for a := 0; a < 10; a++{
#                         const b : float = 1.0;
#                         for a = 0; a < 10; a++{
#                             var c: int ;
#                             const c:int;
#                         }
#                         var e:int;
#                     }
#                 }
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([ConstDecl(Id("b"),FloatType(),FloatLiteral(1.0)),For(Assign(Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("+",Id("a"),IntLiteral(1)),
#                                                                                                   Block([For(Assign(Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("+",Id("a"),IntLiteral(1)),
#                                                                                                              Block([VarDecl(Id("c"),IntType()),ConstDecl(Id("c"),FloatType(),None)]))])),
#                                                                                               VarDecl(Id("e"),IntType())
            
#             ]))],Id("io"))])
#         expect = "Type Mismatch In Declaration: ConstDecl(Id(c),FloatType,None)"
#         self.assertTrue(TestChecker.test(input,expect,419))
    
#     def test_constructor(self):  
#         """ class  Program {
#                 var a : int;
#                 func constructor() {}
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
#                                                   MethodDecl(Id("constructor"),[],VoidType(),Block([]))])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,420))
        
#     def test_constructor_differ_param(self):  
#         """ class  Program {
#                 var a : int;
#                 func constructor() {}
#                 func constructor(a:int) {}
#                 var b : int;
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
#                                                   MethodDecl(Id("constructor"),[],VoidType(),Block([])),
#                                                   MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
#                                                   VarDecl(Id("b"),IntType())])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,421))
        
#     def test_constructor_same_param(self):  
#         """ class  Program {
#                 var a : int;
#                 func constructor(a:int) {}
#                 func constructor(a:int) {}
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
#                                                   MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
#                                                   MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([]))])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,422))
 
#     def test_chain_inheritance_class_dup(self):
#         """
#         class a{
#             var s:string;
#             func constructor(b:int){}
#         }
#         class a <- b {
#             var a:a;
#             func temp():int{}
#             func constructor(a:int){}
#             func constructor(t,w:string){}
#         }
#         class b <-Program{
#             var t:int;
#             func @main() {}
#         }
#         class c <- a{}
#         """
#         input = Program([ClassDecl(Id("a"),[VarDecl(Id("s"),StringType()),
#                                             MethodDecl(Id("constructor"),[VarDecl(Id("b"),IntType())],VoidType(),Block([]))]),
#                          ClassDecl(Id("b"),[VarDecl(Id("a"),ClassType(Id("a"))),
#                                             MethodDecl(Id("temp"),[],IntType(),Block([])),
#                                             MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
#                                             MethodDecl(Id("constructor"),[VarDecl(Id("t"),StringType()),VarDecl(Id("w"),StringType())],VoidType(),Block([]))],Id("a")),
#                          ClassDecl(Id("Program"),[VarDecl(Id("t"),IntType()),
#                                                   MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("b")),
#                          ClassDecl(Id("a"),[],Id("c"))])
#         expect = "Redeclared Class: a"
#         self.assertTrue(TestChecker.test(input,expect,423)) 
        
#     def test_constructor_same_param(self):  
#         """ class  Program {
#                 var a : int;
#                 func constructor(a:int) {}
#                 func constructor(a:int) {}
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
#                                                   MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
#                                                   MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([]))])])
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,424))
        
#     def test_undeclared_classname(self):  
#         """ class  a <- Program {
#                 func @main() {}
#             }
#         """
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("a"))])
#         expect = "Undeclared Class: a"
#         self.assertTrue(TestChecker.test(input,expect,425))

#     def test_oop_class(self):  
#         """ 
#         class a{}
#         class  a <- Program {
#                 func @main() {}
#             }
#         """
#         input = Program([
#             ClassDecl(Id("a"),[]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("a"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,426))
        
#     def test_oop_multiple_class_oroboros(self):  
#         """ 
#         class a <- c {
#             var b :int;
#             var a:int; 
#         }
#         class program<- a{
#             const a:int = 1;
#         }
#         class  c <- Program {
#                 func @main() {}
#             }
#         """
#         input = Program([
#             ClassDecl(Id("c"),[VarDecl(Id("b"),IntType()),
#                                VarDecl(Id("a"),IntType())],Id("a")),
#             ClassDecl(Id("a"),[ConstDecl(Id("a"),IntType(),IntLiteral(1))],Id("Program")),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("c"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,427))

    
#     def test_redeclared_param(self):################
#         """Class Program {
#             func @main (a:int, a:float){}
#             }"""
#         input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
#                                                              [VarDecl(Id("a"),IntType()),VarDecl(Id("a"),FloatType())],
#                                                              VoidType(),
#                                                              Block([]))])])
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input,expect,428))    
    

#     def test_undeclared_expr_ID_in_class_scope(self):  
#         """ 
#         class c {
#             var b :int = a + 1;#################
#             const a:int =1;
#         }
#         class  c <- Program {
#             func @main() {}
#             var a :int;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("c"),[VarDecl(Id("b"),IntType(),IntLiteral(1)),
#                                ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      VarDecl(Id("a"),IntType())],Id("c"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,429))
    
#     def test_static_redecl_method(self):  
#         """ 
#         class c {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  Program {
#             func @main() {}
#             func @a(){}
#             var a :int;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("c"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                                      MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      VarDecl(Id("a"),IntType())])])
#         expect = "Redeclared Method: @a"
#         self.assertTrue(TestChecker.test(input,expect,430))
    
#     def test_static_redecl_attri(self):  
#         """ 
#         class c {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  c<-Program {
#             func @main() {}
#             var @a : int;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("c"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      VarDecl(Id("@a"),IntType())])])
#         expect = "Redeclared Attribute: @a"
#         self.assertTrue(TestChecker.test(input,expect,431))
    
#     def test_classtype(self):  
#         """ 
#         class C {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  C<-Program {
#             func @main() {}
#             var a : A;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      VarDecl(Id("a"),ClassType(Id("A")))],Id("C"))])
#         expect = "Undeclared Class: A"
#         self.assertTrue(TestChecker.test(input,expect,432))
    
#     def test_var_attridecl_void_type(self):  
#         """ 
#         class C {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  C<-Program {
#             func @main() {}
#             var a : voidtype;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      VarDecl(Id("a"),VoidType())],Id("C"))])
#         expect = "Type Mismatch In Declaration: VarDecl(Id(a),VoidType)"
#         self.assertTrue(TestChecker.test(input,expect,433))

#     def test_const_attridecl_void_type(self):  
#         """ 
#         class C {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  C<-Program {
#             func @main() {}
#             const a : voidtype;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      ConstDecl(Id("a"),VoidType(),None)],Id("C"))])
#         expect = "Type Mismatch In Declaration: ConstDecl(Id(a),VoidType,None)"
#         self.assertTrue(TestChecker.test(input,expect,434))
        
#     def test_const_no_init(self):  
#         """ 
#         class C {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  C<-Program {
#             func @main() {}
#             const a : int;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      ConstDecl(Id("a"),IntType(),None)],Id("C"))])
#         expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,None)"
#         self.assertTrue(TestChecker.test(input,expect,435))
        
#     def test_const_init_null(self):  
#         """ 
#         class C {
#             func @a() : int{}
#             const a : int =1 ;
#         }
#         class  C<-Program {
#             func @main() {}
#             const a : int = null;
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[MethodDecl(Id("@a"),[],IntType(),Block([])),
#                 ConstDecl(Id("a"),IntType(),IntLiteral(1))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
#                                      ConstDecl(Id("a"),IntType(),NullLiteral())],Id("C"))])
#         expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,NullLiteral())"
#         self.assertTrue(TestChecker.test(input,expect,436))

#     def test_redeclared_in_block(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 var a: float;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  VarDecl(Id("a"),FloatType())]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,437))
    
#     def test_break(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 break ;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  Break()]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,438))

#     def test_continue(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 continue
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  Continue()]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,439))
        
# ##for if break / con
#     def test_for_if_break(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 for i:= 0; i<5 ;i := i +1{
#                     if a < 10 {
#                     break;
#                 }}
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
#                                                      Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([Break()]))]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,440))
# ## if break/con
#     def test_if_break(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 if a < 10 {
#                     break;
#                 }
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([Break()]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,441))

# ## for for break/con
#     def test_for_for_break(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 for i:= 0; i<5 ;i := i +1{
#                     for i:= 0; i<5 ;i := i +1{
#                         break;
#                     }
#                     break;
#                 }
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
#                                                      Block([For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Break()])),
#                                                             Break()]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,442))
        
#     def test_arraytype(self):
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a :int ;
#                 if a < 10 {
#                     var a [2]srting = ["batcoctreem","daybagiaxuongbien"]
#                 }
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  If(BinaryOp("<",Id("a"),IntLiteral(10)),
#                                                      Block([VarDecl(Id('a'),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('batcoctreem'),StringLiteral('daybagiaxuongbien')]))]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,443))


#     def test_lhs_assign_id_undeclared(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a : int;
#                 b := 10 ;   
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  Assign(Id("b"),IntLiteral(10))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Undeclared Attribute: b"
#         self.assertTrue(TestChecker.test(input,expect,444))
        
#     def test_lhs_assign_id_declared_insame_scope(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a : int;
#                 a := 10 ;   
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  Assign(Id("a"),IntLiteral(10))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,445))
        
#     def test_lhs_assign_id_declared_other_scope(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var a : int;
#                 for  i := 0 ; i < 10 ; i++{
#                     a := 10 ;
#                     i:=10;
#                     b := 1.2;
#             }}
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id('i'),IntLiteral(1))),
#                                                      Block([Assign(Id('a'),IntLiteral(10)),
#                                                             Assign(Id('i'),IntLiteral(10)),
#                                                             Assign(Id('b'),FloatLiteral(1.2))]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Undeclared Attribute: b"
#         self.assertTrue(TestChecker.test(input,expect,446))
        
#     def test_lhs_assign_id_declared_other_class(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var b: float = 0;
#             func @a(a : int) : int{
#                 var a : int;
#                 for  i := 0 ; i < 10 ; i++{
#                     a := 10 ;
#                     i:=10;
#             }}
#         }
#         class  C<-Program {
#             func @main() {
#                 b := 10;
#             }
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id("b"),IntType()),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),IntType()),
#                                                  For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id('i'),IntLiteral(1))),
#                                                      Block([Assign(Id('a'),IntLiteral(10)),
#                                                             Assign(Id('i'),IntLiteral(10))]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),
#                                                 Block([Assign(Id('b'),IntLiteral(10))]))],Id("C"))])
#         expect = "Undeclared Attribute: b"
#         self.assertTrue(TestChecker.test(input,expect,447))        
  
#     def test_lhs_assign_array_same_scope(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 b[1] = 10 ;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(ArrayCell(Id('b'),IntLiteral(1)),IntLiteral(10))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,448))
        
#     def test_lhs_assign_array_expr_not_int(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 b[true] = 10 ;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(ArrayCell(Id('b'),BooleanLiteral(True)),IntLiteral(10))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Expression: ArrayCell(Id(b),BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input,expect,449))

#     def test_lhs_assign_array_class(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [5]int;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 b[1] = a ;
#                 c[2] := b[1];
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(5,IntType())),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(ArrayCell(Id('b'),IntLiteral(1)),Id('a')),
#                                                  Assign(ArrayCell(Id('c'),IntLiteral(2)),ArrayCell(Id('b'),IntLiteral(1)))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,450))

#     def test_lhs_assign_array_id_in_cell(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [5]int;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 b[1] = a ;
#                 c[b] := b[1];
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(5,IntType())),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(ArrayCell(Id('b'),IntLiteral(1)),Id('a')),
#                                                  Assign(ArrayCell(Id('c'),Id('b')),ArrayCell(Id('b'),IntLiteral(1)))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Expression: ArrayCell(Id(c),Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,451))

#     def test_lhs_assign_array_id_in_cell_int_return(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [5]int;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 b[1] = a ;
#                 c[b[2]] := b[1];
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(5,IntType())),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(ArrayCell(Id('b'),IntLiteral(1)),Id('a')),
#                                                  Assign(ArrayCell(Id('c'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(Id('b'),IntLiteral(1)))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,452))
        
#     def test_lhs_assign_field_access_norm(self):  #################
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c :int = 5 ;
#             func @a(a : int) : int{
#                 var a: C;
#                 a.c = 1;
#                 a.c = self.a;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),IntType()),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),ClassType(Id('C'))),
#                                                  Assign(FieldAccess(Id('a'),Id('c')),IntLiteral(1)),
#                                                  Assign(FieldAccess(Id('a'),Id('c')),FieldAccess(SelfLiteral(),Id('a')))
#                                                 ]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,453))
        
#     def test_lhs_assign_field_access_self(self):  #################
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c :int = 5 ;
#             func @a(a : int) : int{
#                 var a: C;
#                 self.c := self.a;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),IntType()),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),ClassType(Id('C'))),
#                                                  Assign(FieldAccess(SelfLiteral(),Id('c')),FieldAccess(SelfLiteral(),Id('a')))
#                                                 ]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,454))
        
#     def test_lhs_assign_field_access_at_id(self):  #################
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c :int = 5 ;
#             func @a(a : int) : int{
#                 var a: C;
#                 self.c = self.a;
#                 @c = self.c
#             }
#         }
#         class  C<-Program {
#             var @c : int ;
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),IntType()),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),ClassType(Id('C'))),
#                                                  Assign(FieldAccess(None,Id('@c')),FieldAccess(SelfLiteral(),Id('c')))
#                                                 ]))]),
#             ClassDecl(Id('Program'),[VarDecl(Id('@c'),IntType())
#                 ,MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,455))
        
#     def test_lhs_assign_field_access_at_id_undecl(self):
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c :int = 5 ;
#             func @a(a : int) : int{
#                 var a: C;
#                 self.c = self.a;
#                 @d = self.c
#             }
#         }
#         class  C<-Program {
#             var @c : int ;
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),IntType()),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("a"),ClassType(Id('C'))),
#                                                  Assign(FieldAccess(None,Id('@d')),FieldAccess(SelfLiteral(),Id('c')))
#                                                 ]))]),
#             ClassDecl(Id('Program'),[VarDecl(Id('@c'),IntType())
#                 ,MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Undeclared Attribute: @d"
#         self.assertTrue(TestChecker.test(input,expect,456))

#     def test_assign_cannot_assign(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [5]int;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 a := a ;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(5,IntType())),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(Id('a'),Id('a'))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,457))

#     def test_assign_cannot_assign(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [5]int;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 self.a := a ;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(5,IntType())),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(FieldAccess(SelfLiteral(),Id('a')),Id('a'))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,458))

#     def test_assign_type_miss_match_stmt(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [5]int;
#             func @a(a : int) : int{
#                 var b : [5]int ; 
#                 self.d : = a ;
#             }
#             var d :void;
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(5,IntType())),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id("b"),ArrayType(5,IntType())),
#                                                  Assign(FieldAccess(SelfLiteral(),Id('d')),Id('a'))])),
#                                VarDecl(Id('d'),VoidType())]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(d)),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,459))

#     def test_arraylit(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [3]int = [1,2,3];
#             func @a(a : int) : int{}
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,460))

#     def test_arraylit_Illegal(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             var c : [3]int = [1,2,3.2];
#             func @a(a : int) : int{}
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                VarDecl(Id('c'),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(3.2)])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3.2)]"
#         self.assertTrue(TestChecker.test(input,expect,461))

#     def test_binaryop_in_var_int_int(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b :int = a + self.a;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id('b'),IntType(),BinaryOp('+',Id('a'),FieldAccess(SelfLiteral(),Id('a'))))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,462))

#     def test_binaryop_in_var_int_float(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b :int = 1.2 + self.a;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id('b'),IntType(),BinaryOp('+',FloatLiteral(1.2),FieldAccess(SelfLiteral(),Id('a'))))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Declaration: VarDecl(Id(b),IntType,BinaryOp(+,FloatLit(1.2),FieldAccess(Self(),Id(a))))"
#         self.assertTrue(TestChecker.test(input,expect,463))
        
#     def test_binaryop_in_var_float_int(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b :float = 1 + self.a;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id('b'),FloatType(),BinaryOp('+',IntLiteral(1),FieldAccess(SelfLiteral(),Id('a'))))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,464))
        
#     def test_binaryop_in_assign_float_int(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b :float;
#                 b := a + 1
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id('b'),FloatType()),
#                                                  Assign(Id('b'),BinaryOp('+',Id('a'),IntLiteral(1)))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,465))

#     def test_binaryop_in_assign_string(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b :float;
#                 b := "a + 1"
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id('b'),FloatType()),
#                                                  Assign(Id('b'),StringLiteral("a + 1"))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b),StringLit(a + 1))"
#         self.assertTrue(TestChecker.test(input,expect,466))

#     def test_binaryop_in_assign_bin_bin(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 var b :float;
#                 b := a + 1 + 3 * 1.2 ;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([VarDecl(Id('b'),FloatType()),
#                                                  Assign(Id('b'),BinaryOp('*',BinaryOp('+',Id('a'),BinaryOp('+',IntLiteral(1),IntLiteral(3))),
#                                                                          FloatLiteral(1.2)))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,465))

#     def test_binaryop_in_string(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 const b : string = "ayo" ^ "whatshup"
#                 b := ""
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),StringType(),BinaryOp('^',StringLiteral("Ayo"),StringLiteral("whatsup"))),
#                                                  Assign(Id('b'),StringLiteral(""))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Cannot Assign To Constant: AssignStmt(Id(b),StringLit())"
#         self.assertTrue(TestChecker.test(input,expect,466))

#     def test_unary(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 const c : bool = !b;
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  ConstDecl(Id('c'),BoolType(),UnaryOp('!',Id('b')))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,467))

#     def test_call_expr(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):int {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C;
#                 const c : int = a.sikma(1,'a',b);
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],IntType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C'))),
#                                                  ConstDecl(Id('c'),IntType(),CallExpr(Id('a'),Id('sikma'),[IntLiteral(1),
#                                                                                                            StringLiteral('a'),
#                                                                                                            BooleanLiteral(False)]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,468))
        
#     def test_call_expr_size(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):int {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C;
#                 const c : int = a.sikma(1,'a',b,5);
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],IntType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C'))),
#                                                  ConstDecl(Id('c'),IntType(),CallExpr(Id('a'),Id('sikma'),[IntLiteral(1),
#                                                                                                            StringLiteral('a'),
#                                                                                                            BooleanLiteral(False),
#                                                                                                            IntLiteral(5)]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(sikma),[IntLit(1),StringLit(a),BooleanLit(False),IntLit(5)])"
#         self.assertTrue(TestChecker.test(input,expect,469))
        
#     def test_call_expr_void(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):void {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C;
#                 const c : int = a.sikma(1,'a',b);
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C'))),
#                                                  ConstDecl(Id('c'),IntType(),CallExpr(Id('a'),Id('sikma'),[IntLiteral(1),
#                                                                                                            StringLiteral('a'),
#                                                                                                            BooleanLiteral(False)]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(sikma),[IntLit(1),StringLit(a),BooleanLit(False)])"
#         self.assertTrue(TestChecker.test(input,expect,470))

#     def test_call_expr_io(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):void {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C;
#                 const c : int = io.@readInt();
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C'))),
#                                                  ConstDecl(Id('c'),IntType(),CallExpr(Id('io'),Id('@readInt'),[]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,471))

#     def test_call_expr_io_misstype(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):void {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C;
#                 const c : int = io.@readFloat();
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C'))),
#                                                  ConstDecl(Id('c'),IntType(),CallExpr(Id('io'),Id('@readFloat'),[]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Declaration: ConstDecl(Id(c),IntType,CallExpr(Id(io),Id(@readFloat),[]))"
#         self.assertTrue(TestChecker.test(input,expect,472))

#     def test_call_expr_io_void(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):void {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C;
#                 const c : int = io.@writeInt();
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C'))),
#                                                  ConstDecl(Id('c'),IntType(),CallExpr(Id('io'),Id('@writeInt'),[]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(@writeInt),[])"
#         self.assertTrue(TestChecker.test(input,expect,473))

#     def test_new_expr_non_constructor(self):  
#         """ 
#         class C {
#             const a : int = 1 ;
#             func sikma(a:int,b:string,c:bool):void {}
#             func @a(a : int) : int{
#                 const b : bool = true;
#                 var a : C = new C();
#             }
#         }
#         class  C<-Program {
#             func @main() {}
#         }
#         """
#         input = Program([                                                                                                                 
#             ClassDecl(Id("C"),[ConstDecl(Id("a"),IntType(),IntLiteral(1)),
#                                MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
#                                                        VarDecl(Id('b'),StringType()),
#                                                        VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
#                                MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
#                                           Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
#                                                  VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[]))]))]),
#             ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
#         expect = "Type Mismatch In Expression: NewExpr(Id(C),[])"
#         self.assertTrue(TestChecker.test(input,expect,474))

    def test_new_expr_constructor(self):  
        """ 
        class C {
            func constructor() {
                
            }
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[]))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_new_expr_constructor_more(self):  
        """ 
        class C {
            func constructor() {}
            func constructor(a:int ,b : C) {}
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
                var z : C = new C(1, a);
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([])),
                               MethodDecl(Id('constructor'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ClassType(Id('C')))],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[])),
                                                 VarDecl(Id('z'),ClassType(Id('C')),NewExpr(Id('C'),[IntLiteral(1),Id('a')]))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_new_expr_constructor_wrong(self):  
        """ 
        class C {
            func constructor() {}
            func constructor(a:int ,b : C) {}
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
                var z : C = new C( a);
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([])),
                               MethodDecl(Id('constructor'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ClassType(Id('C')))],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[])),
                                                 VarDecl(Id('z'),ClassType(Id('C')),NewExpr(Id('C'),[Id('a')]))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "Type Mismatch In Expression: NewExpr(Id(C),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_return(self):  
        """ 
        class C {
            func constructor() {}
            func constructor(a:int ,b : C) {}
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
                var z : C = new C(1, a);
                return 1
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([])),
                               MethodDecl(Id('constructor'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ClassType(Id('C')))],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[])),
                                                 VarDecl(Id('z'),ClassType(Id('C')),NewExpr(Id('C'),[IntLiteral(1),Id('a')])),
                                                 Return(IntLiteral(1))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_return_wrong_expr(self):  
        """ 
        class C {
            func constructor() {}
            func constructor(a:int ,b : C) {}
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
                var z : C = new C(1, a);
                return z
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([])),
                               MethodDecl(Id('constructor'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ClassType(Id('C')))],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[])),
                                                 VarDecl(Id('z'),ClassType(Id('C')),NewExpr(Id('C'),[IntLiteral(1),Id('a')])),
                                                 Return(Id('z'))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "Type Mismatch In Statement: Return(Id(z))"
        self.assertTrue(TestChecker.test(input,expect,479))        
        
    def test_return_none(self):  
        """ 
        class C {
            func constructor() {
                return 
            }
            func constructor(a:int ,b : C) {}
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
                var z : C = new C(1, a);
                return self.a
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([Return()])),
                               MethodDecl(Id('constructor'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ClassType(Id('C')))],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[])),
                                                 VarDecl(Id('z'),ClassType(Id('C')),NewExpr(Id('C'),[IntLiteral(1),Id('a')])),
                                                 Return(FieldAccess(SelfLiteral(),Id('a')))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,480))          
        
    def test_return_something_in_void(self):  
        """ 
        class C {
            func constructor() {
                return 1
            }
            func constructor(a:int ,b : C) {}
            const a : int = 1 ;
            func sikma(a:int,b:string,c:bool):void {}
            func @a(a : int) : int{
                const b : bool = true;
                var a : C = new C();
                var z : C = new C(1, a);
                return self.a
            }
        }
        class  C<-Program {
            func @main() {}
        }
        """
        input = Program([                                                                                                                 
            ClassDecl(Id("C"),[MethodDecl(Id('constructor'),[],VoidType(),Block([Return(IntLiteral(1))])),
                               MethodDecl(Id('constructor'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),ClassType(Id('C')))],VoidType(),Block([])),
                               ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                               MethodDecl(Id('sikma'),[VarDecl(Id('a'),IntType()),
                                                       VarDecl(Id('b'),StringType()),
                                                       VarDecl(Id('c'),BoolType())],VoidType(),Block([])),
                               MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
                                          Block([ConstDecl(Id('b'),BoolType(),BooleanLiteral(True)),
                                                 VarDecl(Id('a'),ClassType(Id('C')),NewExpr(Id('C'),[])),
                                                 VarDecl(Id('z'),ClassType(Id('C')),NewExpr(Id('C'),[IntLiteral(1),Id('a')])),
                                                 Return(FieldAccess(SelfLiteral(),Id('a')))]))]),
            ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("C"))])
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,481))           
        
    # def test_everything_pass(self):  
    #     """ 
    #     class A{
    #         var a:int =10;
    #         const @b: float =1.1;
    #         # var arr : [2]float;
    #     }
    #     class c {
    #         func constructor(a : int ,b: float){}
    #         const a : int = 1 ;
    #         var arr : [2]int;
    #         func @a(a : int) : int{
    #             var a: float;
    #             for i := 1 ; i<10 ; i:=i+1 {
    #                 var i : int = 0 ;
    #                 a : = 1;
    #                 @z = i; 
    #                 continue;
    #             }
    #             arr[1] := 10
    #         }
    #     }
    #     class c<- Program {
    #         func @main() {
    #             for i := 1 ; i<10 ; i:=i+1 {
    #                 var i : int = 0 ;
    #                 break ;
    #             }
    #             var i : int = 10 ;
    #             if {int z : int = 10} i == z {
    #                 io.@print...
    #             }
    #             else {
    #                 io.@print
    #             }
    #         }
    #         var a :int;
    #         var @z : int ;
    #     }
    #     """
    #     input = Program([
    #         ClassDecl(Id("A"),[VarDecl(Id("a"),IntType(),IntLiteral(10)),
    #                            ConstDecl(Id("@b"),FloatType(),FloatLiteral(1.1))]),                                                                                                                
    #         ClassDecl(Id("c"),[MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),
    #                                       Block([])),
    #                            ConstDecl(Id("a"),IntType(),IntLiteral(1)),
    #                            VarDecl(Id('arr'),ArrayType(2,IntType())),
    #                            MethodDecl(Id("@a"),[VarDecl(Id("a"),IntType())],IntType(),
    #                                       Block([VarDecl(Id("a"),FloatType()),
    #                                              For(Assign(Id("i"),IntLiteral(1)),
    #                                                                                  BinaryOp("<",Id("i"),IntLiteral(1)),
    #                                                                                  Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
    #                                                                                  Block([VarDecl(Id("i"),IntType(),IntLiteral(0)),
    #                                                                                         Assign(Id('i'),IntLiteral(1)),
    #                                                                                         Assign(FieldAccess(None,Id("@z")),Id('i')),
    #                                                                                         Continue()])),
    #                                              Assign(ArrayCell(Id('arr'),IntLiteral(1)),IntLiteral(10))]))
    #                            ]),
    #         ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([For(Assign(Id("i"),IntLiteral(1)),
    #                                                                                  BinaryOp("<",Id("i"),IntLiteral(1)),
    #                                                                                  Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
    #                                                                                  Block([VarDecl(Id("i"),IntType(),IntLiteral(0)),
    #                                                                                         Break()])),
    #                                                                              VarDecl(Id("i"),IntType(),IntLiteral(10)),
    #                                                                              If(BinaryOp("==",Id("z"),Id("i")),
    #                                                                                 Block([]),
    #                                                                                 Block([VarDecl(Id("z"),IntType(),IntLiteral(10))]),
    #                                                                                 Block([]))])),
    #                                  VarDecl(Id("a"),IntType()),
    #                                  VarDecl(Id('@z'),IntType())],Id("c"))])
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,499))
        



# ##############################################################
from abc import ABC, abstractmethod, ABCMeta
#from Visitor import Visito
from dataclasses import dataclass
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self,param)

class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class MemDecl(AST):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Id(LHS):
    name:str
    def __str__(self):
        return "Id(" + self.name + ")"
        

# used for binary expression
@dataclass
class BinaryOp(Expr):
    op:str
    left:Expr
    right:Expr
    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

#used for unary expression with orerand like !,+,-
@dataclass
class UnaryOp(Expr):
    op:str
    body:Expr
    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

@dataclass
class CallExpr(Expr):
    obj: Expr # None if there is no obj
    method:Id
    param:List[Expr]
    def __str__(self):
        return "CallExpr(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class NewExpr(Expr):
    classname:Id
    param:List[Expr]
    def __str__(self):
        return "NewExpr(" + str(self.classname) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class ArrayCell(LHS):
    arr:Expr
    idx:Expr
    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

@dataclass
class FieldAccess(LHS):
    obj:Expr # None if there is no obj
    fieldname:Id
    def __str__(self):
        return "FieldAccess(" + ((str(self.obj) + ",") if self.obj else "") + str(self.fieldname) + ")"

class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class IntLiteral(Literal):
    value:int
    def __str__(self):
        return "IntLit(" + str(self.value) + ")"

@dataclass
class FloatLiteral(Literal):
    value:float
    def __str__(self):
        return "FloatLit(" + str(self.value) + ")"

@dataclass
class StringLiteral(Literal):
    value:str
    def __str__(self):
        return "StringLit(" + self.value + ")"

@dataclass
class BooleanLiteral(Literal):
    value:bool
    def __str__(self):
        return "BooleanLit(" + str(self.value) + ")"

class NullLiteral(Literal):
    def __str__(self):
        return "NullLiteral()"

class SelfLiteral(Literal):
    def __str__(self):
        return "Self()"
@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]
    def __str__(self):
        return '[' + ','.join(str(i) for i in self.value)+ ']'
class Decl(AST):
    __metaclass__ = ABCMeta
    pass
class StoreDecl(Stmt):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Block(Stmt):
    stmt:List[Stmt] # empty list if there is no statement in block
    def __str__(self):
        return "Block([" + ','.join(str(i) for i in self.stmt) + "])"

@dataclass
class Assign(Stmt):
    lhs:Expr
    exp:Expr
    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + "," +  str(self.exp) + ")"

@dataclass
class If(Stmt):
    expr:Expr
    thenStmt:Block
    preStmt:Block = None # None if there is no pre-statement
    elseStmt:Block = None # None if there is no else branch
    def __str__(self):
        return "If(" + ((str(self.preStmt) + ",") if self.preStmt else "") + str(self.expr) + "," + str(self.thenStmt) + (("," +  str(self.elseStmt)) if self.elseStmt else "")  + ")"

@dataclass
class For(Stmt):
    initStmt:Assign
    expr:Expr
    postStmt:Assign
    loop:Block  
    def __str__(self):
        return "For(" + str(self.initStmt) + "," + str(self.expr) + "," + str(self.postStmt) + ',' + str(self.loop)  + "])"

class Break(Stmt):
    def __str__(self):
        return "Break"

class Continue(Stmt):
    def __str__(self):
        return "Continue"

@dataclass
class Return(Stmt):
    expr:Expr = None # None if there is no expression after return
    def __str__(self):
        return "Return(" + (str(self.expr)  if  self.expr else "") + ")"

@dataclass
class CallStmt(Stmt):
    obj: Expr  # None if there is no obj 
    method:Id
    param:List[Expr]
    def __str__(self):
        return "Call(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

# used for local variable or parameter declaration 
@dataclass
class VarDecl(StoreDecl):
    variable : Id
    varType : Type
    varInit : Expr = None # None if there is no initial
    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + (","+ str(self.varInit) if self.varInit else "") + ")"
    def toParam(self):
        return "Param(" + str(self.variable) + "," + str(self.varType) + ")"


# used for local constant declaration
@dataclass
class ConstDecl(StoreDecl):
    constant : Id
    constType : Type
    value : Expr
    def __str__(self):
        return "ConstDecl(" + str(self.constant) + "," + str(self.constType) + "," + str(self.value) + ")"

 
#used for a class declaration
@dataclass
class ClassDecl(Decl):
    classname : Id
    memlist : List[MemDecl]
    parentname : Id = None # None if there is no parent
    def __str__(self):
        return "ClassDecl(" + str(self.classname) + (("," + str(self.parentname)) if self.parentname else "") + ",[" + ','.join(str(i) for i in self.memlist) + "])"



# used for a normal or special method declaration. 
# In the case of special method declaration, the return type is VoidType()
@dataclass
class MethodDecl(MemDecl):
    name: Id
    param: List[VarDecl]
    returnType: Type  # VoidType for constructor
    body: Block
    def __str__(self):
        return "MethodDecl(" + str(self.name) +  ",[" +  ','.join(i.toParam() for i in self.param) + "]," + ((str(self.returnType) ) if self.returnType else str(VoidType())) + "," + str(self.body) + ")"

@dataclass
class AttributeDecl(MemDecl):
    decl: StoreDecl #VarDecl or ConstDecl
    def __str__(self):
        return "AttributeDecl(" +  str(self.decl) + ")"


class IntType(Type):
    def __str__(self):
        return "IntType"

class FloatType(Type):
    def __str__(self):
        return "FloatType"

class BoolType(Type):
    def __str__(self):
        return "BoolType"

class StringType(Type):
    def __str__(self):
        return "StringType"

@dataclass
class ArrayType(Type):
    size : int
    eleType:Type
    def __str__(self):
        return "ArrayType(" + str(self.size) +  "," + str(self.eleType) + ")"

@dataclass
class ClassType(Type):
    classname:Id
    def __str__(self):
        return "ClassType(" + str(self.classname)  + ")"


class VoidType(Type):
    def __str__(self):
        return "VoidType"


# used for whole program
@dataclass
class Program(AST):
    decl : List[ClassDecl]
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
