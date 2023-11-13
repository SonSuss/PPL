import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):
    def test_redeclared_class(self):
        """class a {} class Program {func @main() {}} class a {}"""
        input = Program([ClassDecl(Id("a"),[]),
                         ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))]),
                         ClassDecl(Id("a"),[])])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_attribute(self):
        """class Program {func @main() {}} class a {var a:int;var c:int;var c:int;}"""
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))]),
                         ClassDecl(Id("a"),[VarDecl(Id("a"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("c"),IntType())])])
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_redeclared_class_with_ast(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[]),
                         ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))])])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_redeclared_attribute_with_ast(self):
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([]))]),
                         ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,403))    
    def test_method_redeclered_param_block(self): #need to fix after submit
        """
        Class a {
            func a (a:int, b:int): int{
                var a : int =1 ;
            }
            }"""
        input = Program([ClassDecl(Id('a'),[MethodDecl(Id("a"),
                                                             [VarDecl(Id("a"),IntType()),
                                                              VarDecl(Id("b"),IntType())],
                                                             IntType(),
                                                             Block([VarDecl(Id("a"),IntType(),IntLiteral(1))]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_method_redeclered(self):
        """Class Program {
            func a (a:int, b:int): int{}
            func a (a:int, b:int): int{}
            func @main (){}
            }"""
        input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("a"),
                                                             [VarDecl(Id("a"),IntType()),
                                                              VarDecl(Id("b"),IntType())],
                                                             IntType(),
                                                             Block([])),
                                                  MethodDecl(Id("a"),
                                                             [VarDecl(Id("a"),IntType()),
                                                              VarDecl(Id("b"),IntType())],
                                                             IntType(),
                                                             Block([])),
                                                  MethodDecl(Id("@main"),[],VoidType(),Block([]))])])
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,405)) 
    
    # def test_for_redeclered(self):
    #     """Class Program {
    #         func @main (){
    #             for a:=1;a<10;a=a+1 {
    #                 var a :int ;
    #                 const a :int ;
    #             }
    #         }
    #         }"""
    #     input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
    #                                                          [],
    #                                                          VoidType(),
    #                                                          Block([For(Assign(Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
    #                                                                     Block([VarDecl(Id("a"),IntType()),ConstDecl(Id("a"),IntType(),None)]))]))])])
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,406)) 
    # def test_if_redeclered(self):
    #     """Class Program {
    #         func @main (): int{
    #             if a < 0 {
    #                 var a :int ;
    #                 const a :int;
    #             }
    #         }
    #         }"""
    #     input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
    #                                                          [],
    #                                                          VoidType(),
    #                                                          Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),Block([VarDecl(Id("a"),IntType()),ConstDecl(Id("a"),IntType(),None)]))]))])])
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,407))
        
    # def test_if_redeclered_prestmt(self):
    #     """Class Program {
    #         func @main (): int{
    #             if {const a: int =10; var a:int;} a < 0 {
    #                 var a :int ;
    #             }
    #         }
    #         }"""
    #     input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
    #                                                          [],
    #                                                          VoidType(),
    #                                                          Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),Block([VarDecl(Id("a"),IntType())]),
    #                                                                    Block([ConstDecl(Id("a"),IntType(),IntLiteral(10)),VarDecl(Id("a"),IntType())]))]))])])
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_if_redeclered_elseStmt(self):
        """Class Program {
            func @main (): int{
                if a < 0 {
                    var a :int ;
                }
                else {
                    var b:int;
                    const b:int;
                }
            }
            }"""
        input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
                                                             [],
                                                             VoidType(),
                                                             Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),Block([VarDecl(Id("a"),IntType())]),None,Block([VarDecl(Id("b"),IntType()),ConstDecl(Id("b"),IntType(),None)]))]))])])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_if_redeclered_prestmt_elseStmt(self):
        """Class Program {
            func @main (): int{
                if {const a: int =10} a < 0 {
                    var b :int ;
                }
                else {
                    var a:int ;
                    coust a:int;
                }
            }
            }"""
        input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),
                                                             [],
                                                             VoidType(),
                                                             Block([If(BinaryOp("<",Id("a"),IntLiteral(0)),
                                                                       Block([VarDecl(Id("b"),IntType())]),
                                                                       Block([ConstDecl(Id("a"),IntType(),IntLiteral(10))]),
                                                                       Block([VarDecl(Id("a"),IntType()),ConstDecl(Id("a"),IntType(),None)]))]))])])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_no_entry_point_class(self):  
        """ class a {} 
            class b {}
        """
        input = Program([ClassDecl(Id('a'),[]),
                         ClassDecl(Id('b'),[])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_no_entry_point_method(self):  
        """ class a {} 
            class Program {
                func a () : int {}
            }
        """
        input = Program([ClassDecl(Id('a'),[]),
                         ClassDecl(Id('Program'),[MethodDecl(Id("a"),[],IntType(),Block([]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,412))
        

    def test_no_entry_point_method_atrribute_samename(self):  
        """ class a {} 
            class Program {
                var @main : int;
            }
        """
        input = Program([ClassDecl(Id('a'),[]),
                         ClassDecl(Id('Program'),[VarDecl(Id("@main"),IntType())])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,413))
        

    def test_no_entry_point_method_param(self):  
        """ class a {} 
            class Program {
                func @main(a:int){}
            }
        """
        input = Program([ClassDecl(Id('a'),[]),
                         ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[VarDecl(Id("a"),IntType())],VoidType(),Block([]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    # def test_if_in_if(self):  
    #     """ class a {} 
    #         class Program {
    #             func @main(){
    #                 if a < 5 {
    #                     var a : int;
    #                     if a ==10 {
    #                         var a:int;
    #                     }
    #                     else {
    #                         var a:int;
    #                     }
    #                     const a:int;
    #                 }
    #             }
    #         }
    #     """
    #     input = Program([ClassDecl(Id('a'),[]),
    #                      ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([
    #                          If(BinaryOp("<",Id("a"),IntLiteral(5)),Block([
    #                              VarDecl(Id("a"),IntType()),
    #                              If(BinaryOp("==",Id("a"),IntLiteral(10)),
    #                                 Block([VarDecl(Id("a"),IntType())]),None,
    #                                 Block([VarDecl(Id("a"),IntType())]),),
    #                              ConstDecl(Id("a"),IntType(),None)
    #                          ])),
                             
    #                      ]))])])
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_redeclered_io_class(self):  
        """ class io {} 
            class Program {
                func @main() : int {}
            }
        """
        input = Program([ClassDecl(Id('io'),[]),
                         ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))])])
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_class_program_papa(self):  
        """ class io {} 
            class io <- Program {
                func @main() : int {}
            }
        """
        input = Program([ClassDecl(Id('io'),[]),
                         ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("io"))])
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_entry_not_voidtype(self):  
        """ class io <- Program {
                func @main():int {}
            }
        """
        input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],IntType(),Block([]))],Id("io"))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_for_in_for_redeclered(self):
        """ class Program {
                func @main(){
                    for a := 0; a < 10; a++{
                        const b : int;
                        for a = 0; a < 10; a++{
                            var c: int ;
                            const c:int;
                        }
                        var b:int;
                    }
                }
            }
        """
        input = Program([ClassDecl(Id('Program'),[MethodDecl(Id("@main"),[],VoidType(),Block([ConstDecl(Id("b"),IntType(),None),For(Assign(Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("+",Id("a"),IntLiteral(1)),
                                                                                                  Block([For(Assign(Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("+",Id("a"),IntLiteral(1)),
                                                                                                             Block([VarDecl(Id("c"),IntType()),ConstDecl(Id("c"),FloatType(),None)]))])),
                                                                                              VarDecl(Id("b"),IntType())
            
            ]))],Id("io"))])
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_constructor(self):  
        """ class  Program {
                var a : int;
                func constructor() {}
            }
        """
        input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
                                                  MethodDecl(Id("constructor"),[],VoidType(),Block([]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_constructor_differ_param(self):  
        """ class  Program {
                var a : int;
                func constructor() {}
                func constructor(a:int) {}
                var b : int;
            }
        """
        input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
                                                  MethodDecl(Id("constructor"),[],VoidType(),Block([])),
                                                  MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
                                                  VarDecl(Id("b"),IntType())])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_constructor_same_param(self):  
        """ class  Program {
                var a : int;
                func constructor(a:int) {}
                func constructor(a:int) {}
            }
        """
        input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
                                                  MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
                                                  MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,422))
 
    def test_chain_inheritance_class_dup(self):
        """
        class a{
            var s:string;
            func constructor(b:int){}
        }
        class a <- b {
            var a:a;
            func temp():int{}
            func constructor(a:int){}
            func constructor(t,w:string){}
        }
        class b <-Program{
            var t:int;
            func @main() {}
        }
        class c <- a{}
        """
        input = Program([ClassDecl(Id("a"),[VarDecl(Id("s"),StringType()),
                                            MethodDecl(Id("constructor"),[VarDecl(Id("b"),IntType())],VoidType(),Block([]))]),
                         ClassDecl(Id("b"),[VarDecl(Id("a"),ClassType(Id("a"))),
                                            MethodDecl(Id("temp"),[],IntType(),Block([])),
                                            MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
                                            MethodDecl(Id("constructor"),[VarDecl(Id("t"),StringType()),VarDecl(Id("w"),StringType())],VoidType(),Block([]))],Id("a")),
                         ClassDecl(Id("Program"),[VarDecl(Id("t"),IntType()),
                                                  MethodDecl(Id("@main"),[],VoidType(),Block([]))],Id("b")),
                         ClassDecl(Id("a"),[],Id("c"))])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,423)) 
        
    def test_constructor_same_param(self):  
        """ class  Program {
                var a : int;
                func constructor(a:int) {}
                func constructor(a:int) {}
            }
        """
        input = Program([ClassDecl(Id('Program'),[VarDecl(Id("a"),IntType()),
                                                  MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),
                                                  MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,424))
        

        
################################################################
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
