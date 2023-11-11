
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy


# class Member:
#     def __init__(self,n,t,isMu=False):
#         self.name = n
#         self.typ = t
#         self.isMu = isMu
#     def __str__(self):
#         return "Member("+self.name+","+str(self.typ)+","+str(self.kind)+","+str(self.isMu)+")"



# class BKClass:
#     def __init__(self,n,p,m):
#         self.name = n
#         self.parent = p
#         self.member = m
#     def __str__(self):
#         return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"

class Member:
    def __init__(self,n,t,isMu=False):
        self.name = n
        self.typ = t
        self.isMu = isMu
    def __str__(self):
        return "Member("+self.name+","+str(self.typ)+","+str(self.isMu)+")"



class BKClass:
    def __init__(self,n,p,m):
        self.name = n
        self.parent = p
        self.member = m
    def __str__(self):
        return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"

# class StaticChecker(BaseVisitor,Utils):
#     inttype = IntType()
#     floattype = FloatType()
#     voidtype = VoidType()
#     booltype = BoolType()
#     stringtype = StringType() 
#     def __init__(self,ast):
#         self.ast = ast
#         self.io = [BKClass("io",None,[
#                             Member("@readInt",MType([],StaticChecker.inttype),False),
#                             Member("@writeIntLn",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
#                             ])]
#     def check(self):
#         self.visit(self.ast,self.io)
#         return "successful"

#     def visitProgram(self,ast, c):
#         env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        
#     def visitClassDecl(self, ast, c):
#         if ast.classname.name in map(lambda x: x.name,c):
#             raise Redeclared(Class(),ast.classname.name)
#         mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
#         return [BKClass(ast.classname.name,ast.parentname,mem)]+c

#     def visitAttributeDecl(self,ast,c):
#         field = self.visit(ast.decl,c) 
#         return [field]+c

#     def visitVarDecl(self, ast, c):
#         if ast.variable.name in map(lambda x: x.name,c):
#             raise Redeclared(Attribute(),ast.variable.name)
#         return Member(ast.variable.name,ast.varType,True)


class GetEvm(BaseVisitor,Utils):
    def __init__(self):
        pass
    
    def visitProgram(self,ast, c):
        env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        return env
        
    def visitClassDecl(self, ast, c):
        if ast.classname.name in map(lambda x: x.name,c):
            raise Redeclared(Class(),ast.classname.name)
        mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
        return [BKClass(ast.classname.name,ast.parentname,mem)]+c
    
    def visitMethodDecl(self,ast,c):
        if ast.name.name in map(lambda x: x.name,c):
            raise Redeclared(Method(),ast.name.name)
        reduce(lambda a,e : self.visit(e,a) + a ,ast.param + ast.body.stmt,[])
        partype = reduce(lambda a,e : [e.varType] + a, ast.param ,[])
        return [Member(ast.name.name,MType(partype,ast.returnType))] + c
    
    def visitFor(self,ast,c):
        mem = reduce(lambda a,e : self.visit(e,a) + a ,ast.loop.stmt, [])
        return []
    
    def visitIf(self,ast,c):
        thenblock = []
        elseblock = []
        if ast.preStmt :
            thenblock =reduce(lambda a,e : self.visit(e,a) + a ,ast.preStmt.stmt + ast.thenStmt.stmt, [])
            if ast.elseStmt:
                elseblock = reduce(lambda a,e : self.visit(e,a) + a , ast.preStmt.stmt + ast.elseStmt.stmt, [])
        else:
            thenblock =reduce(lambda a,e : self.visit(e,a) + a ,ast.thenStmt.stmt, [])
            if ast.elseStmt:
                elseblock = reduce(lambda a,e : self.visit(e,a) + a ,ast.elseStmt.stmt, [])
        return []

    
    def visitAttributeDecl(self,ast,c):
        field = self.visit(ast.decl,c) 
        return field + c
    
    def visitVarDecl(self, ast, c):
        if ast.variable.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.variable.name)
        return [Member(ast.variable.name,ast.varType,True)]
    
    def visitConstDecl(self,ast,c):
        if ast.constant.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.constant.name)
        return [Member(ast.constant.name,ast.constType)]
    
    

################################################################
class StaticChecker(BaseVisitor,Utils):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType() 
    def __init__(self,ast):
        self.ast = ast
        self.io = [BKClass("io",None,[
                            Member("@readInt",MType([],StaticChecker.inttype),False),
                            Member("@writeIntLn",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
                            ])]
    def check(self):
        self.visit(self.ast,self.io)
        return "successful"

    def visitProgram(self,ast, c):
        evm=GetEvm().visit(ast,c)
        entryclass = next(filter(lambda entryclass: entryclass.name == "Program",evm),None)
        if entryclass:
            # entryfunc= next(filter(lambda entryfunc: entryfunc.name == "@main",entryclass.member),None)
            if not next(filter(lambda entryfunc: entryfunc.name == "@main" and isinstance(entryfunc.typ,MType) and len(entryfunc.typ.partype)== 0 and str(entryfunc.typ.rettype)=="VoidType",entryclass.member),None):
                raise NoEntryPoint()
        else: raise NoEntryPoint()
    
    def visitClassDecl(self, ast, c):
        pass

    def visitMemDecl(self,ast,c):
        pass
    
    def visitMethodDecl(self,ast,c):
        pass
    
    # def visitAttributeDecl(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitVarDecl(self, ast, c):
    #     return self.visit(ast,c)
    
    # def visitConstDecl(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitStmt(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitStoreDecl(self,ast,c):
    #     return self.visit(ast.decl,c)
    
    # def visitBlock(self,ast,c):
    #     return self.visit(ast.block,c)
    
    # def visitAssign(self,ast,c):
    #     return self.visit(ast.assign,c)
    
    # def visitIf(self,ast,c):
    #     return self.visit(ast.If,c)
    
    # def visitFor(self,ast,c):
    #     return self.visit(ast.For,c)
    
    # def visitBreak(self,ast,c):
    #     return self.visit(ast.Break,c)
    
    # def visitContinue(self,ast,c):
    #     return self.visit(ast.Continue,c)
    
    # def visitReturn(self,ast,c):
    #     return self.visit(ast.Return,c)
    
    # def visitCall(self,ast,c):
    #     return self.visit(ast.Call,c)
    
    # def visitExpr(self,ast,c):
    #     return self.visit(ast.Expr,c)
    
    # def visitId(self,ast,c):
    #     return self.visit(ast.Id,c)
    
    # def visitArrayCell(self,ast,c):
    #     return self.visit(ast.ArrayCell,c)
    
    # def visitFieldAccess(self,ast,c):
    #     return self.visit(ast.FieldAccess,c)
    
    # def visitBinaryOp(self,ast,c):
    #     return self.visit(ast.BinaryOp,c)
    
    # def visitUnaryOp(self,ast,c):
    #     return self.visit(ast.UnaryOp,c)
    
    # def visitCallExpr(self,ast,c):
    #     return self.visit(ast.CallExpr,c)
    
    # def visitNewExpr(self,ast,c):
    #     return self.visit(ast.NewExpr,c)
    
    # def visitLiteral(self,ast,c):
    #     return self.visit(ast.Literal,c)
    
    # def visitIntLiteral(self,ast,c):
    #     return self.visit(ast.IntLiteral,c)
    
    # def visitFloatLiteral(self,ast,c):
    #     return self.visit(ast.FloatLiteral,c)
    
    # def visitStringLiteral(self,ast,c):
    #     return self.visit(ast.StringLiteral,c)
    
    # def visitBooleanLiteral(self,ast,c):
    #     return self.visit(ast.BooleanLiteral,c)
    
    # def visitNullLiteral(self,ast,c):
    #     return self.visit(ast.NullLiteral,c)
    
    # def visitSelfLiteral(self,ast,c):
    #     return self.visit(ast.SelfLiteral,c)
    
    # def visitArrayLiteral(self,ast,c):
    #     return self.visit(ast.ArrayLiteral,c)
    
    # def visitType(self,ast,c):
    #     return self.visit(ast.Type,c)
    
    # def visitIntType(self,ast,c):
    #     return self.visit(ast.IntType,c)
    
    # def visitFloatType(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitBoolType(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitStringType(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitArrayType(self,ast,c):
    #     return self.visit(ast,c)
    
    # def visitClassType(self,ast,c):
    #     return self.visit(ast,c)
     