from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_dcl.
    def visitClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_body.
    def visitClass_body(self, ctx:CSlangParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_lst.
    def visitMethod_lst(self, ctx:CSlangParser.Method_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_dcl.
    def visitMethod_dcl(self, ctx:CSlangParser.Method_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_decl.
    def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param_lst.
    def visitParam_lst(self, ctx:CSlangParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#multiplying.
    def visitMultiplying(self, ctx:CSlangParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#adding.
    def visitAdding(self, ctx:CSlangParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#logical_bin.
    def visitLogical_bin(self, ctx:CSlangParser.Logical_binContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#logical_not.
    def visitLogical_not(self, ctx:CSlangParser.Logical_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#relational.
    def visitRelational(self, ctx:CSlangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#relat_bool.
    def visitRelat_bool(self, ctx:CSlangParser.Relat_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#relat_int_float.
    def visitRelat_int_float(self, ctx:CSlangParser.Relat_int_floatContext):
        return self.visitChildren(ctx)

    def visitRelational_expr0(self, ctx:CSlangParser.Relational_expr0Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CSlangParser#relational_expr.
    def visitRelational_expr(self, ctx:CSlangParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_lst.
    def visitExpr_lst(self, ctx:CSlangParser.Expr_lstContext):
        lst=[]
        for a in ctx.getChildren():
            lst.append(a.accept(self))
        return lst


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return BinaryOp(ctx.getChild(1).accept(self),ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return BinaryOp(ctx.getChild(1).accept(self),ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return BinaryOp(ctx.getChild(1).accept(self),ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return BinaryOp(ctx.getChild(1).accept(self),ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return BinaryOp(ctx.getChild(1).accept(self),ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return UnaryOp(ctx.getChild(0).accept(self),ctx.getChild().accept(self))


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return UnaryOp(ctx.getChild(0).getText(),ctx.getChild().accept(self))


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        if ctx.expr8():
            return ctx.getChild(0).accept(self)
        return ArrayCell(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self) )


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        if ctx.expr9():
            return ctx.getChild(0).accept(self)
        else:
            if ctx.getChildCount()==3:
                return FieldAccess(ctx.getChild(0).accept(self), Id(ctx.getChild(2).getText()),[])
            else:
                return CallExpr(ctx.getChild(0).accept(self), Id(ctx.getChild(2).getText()),ctx.getChild(4).accept(self))


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        if ctx.expr10():
            return ctx.getChild(0).accept(self)
        if ctx.DOT():
            if ctx.getChildCount() == 3:
                return FieldAccess(Id(ctx.getChild(0).getText()), Id(ctx.getChild(2).getText()),[])
            
            return CallExpr(Id(ctx.getChild(0).getText()), Id(ctx.getChild(2).getText()),ctx.getChild(4).accept(self))
        else:
            if ctx.getChildCount()==1:
                return FieldAccess(None, Id(ctx.getChild(0).getText()),[])
            return CallExpr(None, Id(ctx.getChild(0).getText()), ctx.getChild(2).accept(self))

    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        if ctx.expr11():
            return ctx.getChild(0).accept(self)
        else:
            return NewExpr(ctx.getChild(1).getText(),ctx.getChild(3).accept)


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        if ctx.expr():
            return ctx.expr().accept(self)
        if ctx.literal():
            return ctx.literal().accept(self)
        if ctx.SELF():
            return SelfLiteral()
        if ctx.ID():
            return Id(ctx.getChild(0).getText())
        if ctx.NULL():
            return NullLiteral()
        

    # Visit a parse tree produced by CSlangParser#statements.
    def visitStatements(self, ctx:CSlangParser.StatementsContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#assign_decl.
    def visitAssign_decl(self, ctx:CSlangParser.Assign_declContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#attribute_assign.
    def visitAttribute_assign(self, ctx:CSlangParser.Attribute_assignContext):
        return Assign(ctx.getChild(0).accpet(self), ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#attribute_decl.
    def visitAttribute_decl(self, ctx:CSlangParser.Attribute_declContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#variable_decl.
    def visitVariable_decl(self, ctx:CSlangParser.Variable_declContext):
        return VarDecl(ctx.getChild(1).accept(self))


    # Visit a parse tree produced by CSlangParser#constraint_decl.
    def visitConstraint_decl(self, ctx:CSlangParser.Constraint_declContext):
        return ConstDecl(ctx.getChild(1).accept(self))


    # Visit a parse tree produced by CSlangParser#non_inital_decl.
    def visitNon_inital_decl(self, ctx:CSlangParser.Non_inital_declContext):
        return ctx.getChild(0).accept(self),ctx.getChild(2).accept(self),None


    # Visit a parse tree produced by CSlangParser#inital_decl.
    def visitInital_decl(self, ctx:CSlangParser.Inital_declContext):
        if ctx.getChildCount() <= 5:
            return ctx.getChild(0).accept(self), ctx.getChild(2).accept(self),ctx.getChild(4).accept(self)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return ArrayType(ctx.getChild(1).getText(),ctx.getChild(3).accept(self))


    # Visit a parse tree produced by CSlangParser#if_state.
    def visitIf_state(self, ctx:CSlangParser.If_stateContext):
        if ctx.ELSE():
            if ctx.getChildCount()==6:
                return If(ctx.expr().accept(self),ctx.block_state(1).accept(self),ctx.block_state(0).accept(self),ctx.block_state(2).accept(self))
            else:
                return If(ctx.expr().accept(self),ctx.block_state(0).accept(self),None,ctx.block_state(1).accept(self))
        else:
            if ctx.getChildCount()==4:
                return If(ctx.expr().accept(self),ctx.block_state(1).accept(self),ctx.block_state(0).accept(self),None)
            else:
                return If(ctx.expr().accept(self),ctx.block_state(0).accept(self),None,None)


    # Visit a parse tree produced by CSlangParser#for_state.
    def visitFor_state(self, ctx:CSlangParser.For_stateContext):
        return For(ctx.attribute_assign(0).accept(self), ctx.relational_expr0().accept(self),ctx.attribute_assign(1).accept(self), ctx.block_state().accept(self))


    # Visit a parse tree produced by CSlangParser#break_state.
    def visitBreak_state(self, ctx:CSlangParser.Break_stateContext):
        return Break()


    # Visit a parse tree produced by CSlangParser#continue_state.
    def visitContinue_state(self, ctx:CSlangParser.Continue_stateContext):
        return Continue()


    # Visit a parse tree produced by CSlangParser#return_state.
    def visitReturn_state(self, ctx:CSlangParser.Return_stateContext):
        return Return(ctx.expr().accept(self))


    def visitCall_state(self, ctx:CSlangParser.Call_stateContext):
        return ctx.getChild(0).accept(self)
    

    # Visit a parse tree produced by CSlangParser#instance_method_invo_access.
    def visitInstance_method_invo_access(self, ctx:CSlangParser.Instance_method_invo_accessContext):
        param=[]
        for a in ctx.expr_lst():
            param.append(a.accept(self))
        if ctx.DOT():
            return CallStmt(ctx.expr().accept(self),Id(ctx.AT_ID().getText(),param) )
        else:
            return CallStmt(None,Id(ctx.AT_ID().getText(),param))


    # Visit a parse tree produced by CSlangParser#static_method_invo_access.
    def visitStatic_method_invo_access(self, ctx:CSlangParser.Static_method_invo_accessContext):
        param=[]
        for a in ctx.expr_lst():
            param.append(a.accept(self))
        if ctx.DOT():
            return CallStmt(Id(ctx.ID().getText()),Id(ctx.AT_ID().getText(),param) )
        else:
            return CallStmt(None,Id(ctx.AT_ID().getText(),param))

    # Visit a parse tree produced by CSlangParser#block_state.
    def visitBlock_state(self, ctx:CSlangParser.Block_stateContext):
        stmt = []
        for a in ctx.getChildren():
            stmt.append(a.accept(self))
        return Block(stmt)


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#index_op.
    def visitIndex_op(self, ctx:CSlangParser.Index_opContext):
        arr = ctx.expr(0).accept(self)
        idx = ctx.expr(1).accept(self)
        return ArrayCell(arr,idx)


    # Visit a parse tree produced by CSlangParser#id_lst.
    def visitId_lst(self, ctx:CSlangParser.Id_lstContext):
        return [a for a in ctx.getChildren()]


    # Visit a parse tree produced by CSlangParser#id_access.
    def visitId_access(self, ctx:CSlangParser.Id_accessContext):
        return Id(ctx.getChild(0).getText())


    # Visit a parse tree produced by CSlangParser#io_st.
    def visitIo_st(self, ctx:CSlangParser.Io_stContext):
        if ctx.getChildCount() == 6:
            return CallStmt(ctx.expr().accept(self),ctx.io_mt().accept(self),[])
        return CallStmt(ctx.getChild(0).accept(self),ctx.io_mt().accept(self),[ctx.getChild(4).accept(self)])


    # Visit a parse tree produced by CSlangParser#io.
    def visitIo_mt(self, ctx:CSlangParser.Io_mtContext):
        return Id(ctx.getChild(0).accpet(self))

    # Visit a parse tree produced by CSlangParser#typ.
    def visitTyp(self, ctx:CSlangParser.TypContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOL():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        if ctx.VOID():
            return VoidType()


    # Visit a parse tree produced by CSlangParser#attri_type.
    def visitAttri_type(self, ctx:CSlangParser.Attri_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOL():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        if ctx.INT_LITERAL() or ctx.NON_ZERO_INT():
            return IntLiteral(ctx.getChild(0).getText())
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(ctx.getChild(0).getText())
        if ctx.bool_literal():
            return ctx.bool_literal().accept(self)    
        if ctx.STRING_literal():
            return StringLiteral(ctx.getChild(0).getText())
        if ctx.array():
            return ctx.array().accept(self)
                       

    # Visit a parse tree produced by CSlangParser#bool_literal.
    def visitBool_literal(self, ctx:CSlangParser.Bool_literalContext):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)
        


    # Visit a parse tree produced by CSlangParser#array.
    def visitArray(self, ctx:CSlangParser.ArrayContext):
        litList = []
        for lit in ctx.literal():
            litList.append(lit.accept(self))
        return ArrayLiteral(litList)


#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------

from abc import ABC, abstractmethod, ABCMeta
#from Visitor import Visitor
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
    expr:Expr
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
