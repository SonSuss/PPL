
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy



class Member:
    def __init__(self,n,t,isFunc=False,isMu=False):
        self.name = n
        self.typ = t
        self.isFunc = isFunc
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


class GetEvm(BaseVisitor,Utils):
    def __init__(self):
        pass
    
    def visitProgram(self,ast, c):
        env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        return env
        
    def visitClassDecl(self, ast, c):
        if ast.classname.name in map(lambda x: x.name,c):
            raise Redeclared(Class(),ast.classname.name)
        mem = reduce(lambda a,e: a + [self.visit(e,a)] ,ast.memlist,[])
        return c + [BKClass(ast.classname.name,ast.parentname,mem)]
    
    def visitMethodDecl(self,ast,c):
        if ast.name.name in map(lambda x: x.name,c):
            if ast.name.name != "constructor":
                raise Redeclared(Method(),ast.name.name)
        partype = []
        parlst=[]
        for e in ast.param:
            if e.variable.name in parlst:
                raise Redeclared(Parameter(),e.variable.name)
            else: 
                parlst += e.variable.name
                partype = partype + [e.varType] 
        return Member(ast.name.name,MType(partype,ast.returnType),True) 
    
    def visitFor(self,ast,c): 
        mem = reduce(lambda a,e : self.visit(e,a) + a ,ast.loop.stmt, [])
        return [mem]
    
    def visitIf(self,ast,c):
        thenblock = []
        elseblock = []
        if ast.preStmt :
            thenblock =reduce(lambda a,e : self.visit(e,a) + a ,ast.preStmt.stmt, [])
            if ast.elseStmt:
                elseblock = reduce(lambda a,e : self.visit(e,a) + a ,ast.elseStmt.stmt, [])
        else:
            thenblock =reduce(lambda a,e : self.visit(e,a) + a ,ast.thenStmt.stmt, [])
            if ast.elseStmt:
                elseblock = reduce(lambda a,e : self.visit(e,a) + a ,ast.elseStmt.stmt, [])
        return [thenblock,elseblock]

    
    def visitAttributeDecl(self,ast,c):
        field = self.visit(ast.decl,c) 
        return field 
    
    def visitVarDecl(self, ast, c):
        if ast.variable.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.variable.name)
        return Member(ast.variable.name,ast.varType,False,True)
    
    def visitConstDecl(self,ast,c):
        if ast.constant.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.constant.name)
        return Member(ast.constant.name,ast.constType)
    
    

################################################################

class StaticChecker(BaseVisitor,Utils):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType()
    voidtype = VoidType()
    selflitteral = SelfLiteral()
    notArraytype = [inttype, floattype, booltype,stringtype,voidtype]
    
    def __init__(self,ast):
        self.ast = ast
        self.io = [BKClass("io",None,[
                            Member("@readInt",MType([],StaticChecker.inttype),True),
                            Member("@writeInt",MType([StaticChecker.inttype],StaticChecker.voidtype),True),
                            Member("@readFloat",MType([],StaticChecker.floattype),True),
                            Member("@writeFloat",MType([StaticChecker.floattype],StaticChecker.voidtype),True),
                            Member("@readBool",MType([],StaticChecker.booltype),True),
                            Member("@writeBool",MType([StaticChecker.booltype],StaticChecker.booltype),True),
                            Member("@readStr",MType([],StaticChecker.stringtype),True),
                            Member("@writeStr",MType([StaticChecker.stringtype],StaticChecker.voidtype),True)
                            ])]
    def check(self):
        self.visit(self.ast,self.io)
        return ""

    def visitProgram(self,ast, c):
        c=GetEvm().visit(ast,c)
        globalScope = []
        for classScope in c:
            for staticmember in classScope.member:
                if "@" in staticmember.name:
                    if staticmember.name in map(lambda x: x.name,globalScope):
                        if staticmember.isFunc:
                            raise Redeclared(Method(),staticmember.name)
                        else: raise Redeclared(Attribute(),staticmember.name)
                    globalScope = [staticmember] + globalScope
                if "io" == staticmember.name:
                    raise Redeclared(Attribute(),staticmember.name)  
        entryclass = next(filter(lambda entryclass: entryclass.name == "Program",c),None)
        if entryclass:
            if not next(filter(lambda entryfunc: entryfunc.name == "@main" and isinstance(entryfunc.typ,MType) and len(entryfunc.typ.partype)== 0 and str(entryfunc.typ.rettype)=="VoidType",entryclass.member),None):
                raise NoEntryPoint()
        else: raise NoEntryPoint()
        c= [globalScope] + [c]
        for decl in ast.decl:self.visit(decl,c)
    
    def visitClassDecl(self, ast, c):
        classScope=c[1]
        scopename = next(filter(lambda x: x.name == ast.classname.name ,classScope),None)
        oop = scopename.member #not get self scope cuz not know anything yet ?
        if scopename.parent:
            parent = scopename.parent
            oroboros=[scopename.name]
            while True:
                name = parent.name
                if not name in map(lambda x: x.name,classScope):
                    raise Undeclared(Class(),name)
                if name in oroboros:
                    break
                oroboros += [name]
                scope = next(filter(lambda x: x.name == name ,classScope),None)
                if not scope:
                    raise Undeclared(Class(),)
                oop =  oop + scope.member 
                if scope.parent:
                    parent = scope.parent
                else: 
                    break
        c= [[Member("io",ClassType(Id("io")))]] + [oop] + c
        for memdecl in ast.memlist:
            c = self.visit(memdecl,c)
        

    def visitMemDecl(self,ast,c):
        return self.visit(ast,c)
    
    def visitMethodDecl(self,ast,c):
        param= reduce(lambda a,e : [GetEvm().visit(e,a)] + a ,ast.param,[])
        param.append(Member("func",ast.returnType))
        newc = [param] + c
        self.visit(ast.body,newc)
        c[0].insert(0,GetEvm().visit(ast,[]))
        return c
    
    def visitAttributeDecl(self,ast,c):
        return self.visit(ast,c)
    
    def visitVarDecl(self, ast, c):
        classMember=c[-1]
        retyp = self.visit(ast.varType,classMember)
        if retyp == "VoidType":
            raise TypeMismatchInDeclaration(ast)
        if ast.varInit : 
            expr = str(self.visit(ast.varInit,c))
            if expr != None :
                if retyp == "FloatType":
                    if expr != "FloatType" and expr != "IntType":
                        raise TypeMismatchInDeclaration(ast)
                else:
                    if expr != retyp:
                        raise TypeMismatchInDeclaration(ast)
        c[0].insert(0,GetEvm().visit(ast,c[0]))
        return c
    
    def visitConstDecl(self,ast,c):
        classMember=c[-1]
        retyp = self.visit(ast.constType,classMember)
        if retyp == "VoidType":
            raise TypeMismatchInDeclaration(ast)
        if ast.value: 
            expr = str(self.visit(ast.value,c))
            if expr == None:
                raise TypeMismatchInDeclaration(ast)
            if retyp == "FloatType":
                if expr != "FloatType" and expr != "IntType":
                    raise TypeMismatchInDeclaration(ast)
            else:
                if expr != retyp:
                    raise TypeMismatchInDeclaration(ast)
        else:
            raise TypeMismatchInDeclaration(ast)
        c[0].insert(0,GetEvm().visit(ast,c[0]))
        return c
    
    def visitStmt(self,ast,c):
        return self.visit(ast,c)
    
    def visitStoreDecl(self,ast,c):
        return self.visit(ast.decl,c)
    
    def visitBlock(self,ast,c):
        reduce(lambda a,e : self.visit(e,a) ,ast.stmt, [[]] + c)
    
    def visitAssign(self,ast,c):
        lhstyp = LeftHandSide().visit(ast.lhs,c)
        if not lhstyp[1]:
            raise CannotAssignToConstant(ast)
        if str(lhstyp[0]) == str(StaticChecker.voidtype):
            raise TypeMismatchInStatement(ast)
        exptyp = str(self.visit(ast.exp,c))
        # print([str(lhstyp[0]),exptyp])
        if str(lhstyp[0]) == "FloatType":
            if exptyp != "FloatType" and exptyp != "IntType":
                raise TypeMismatchInStatement(ast)
        else:
            if str(lhstyp[0]) != exptyp:
                raise TypeMismatchInStatement(ast)
        return c
    
    def visitIf(self,ast,c):
        checkScopelst = c
        if ast.preStmt:
            self.visit(ast.preStmt,checkScopelst)
            preScope = reduce(lambda a ,e : GetEvm().visit(e,a),ast.preStmt.stmt,[]) #make expr can find preScope
            checkScopelst = [[preScope]] + c
        if str(self.visit(ast.expr,checkScopelst)) != str(StaticChecker.booltype):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,checkScopelst)
        if ast.elseStmt :
            self.visit(ast.elseStmt,checkScopelst)
        return c
    
    def visitFor(self,ast,c):
        forBlock = [[Member("for",StaticChecker.inttype)]] + c
        if str(ast.initStmt.lhs)[:2]== "Id":
            initMember = Member(ast.initStmt.lhs.name,self.visit(ast.initStmt.exp,forBlock),False,True)
            forBlock[0].insert(0,initMember)
        else: 
            self.visit(ast.initStmt,forBlock)
        if str(self.visit(ast.expr,forBlock)) != str(StaticChecker.booltype):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop,forBlock)
        self.visit(ast.postStmt,forBlock)
        return c
    
    def visitBreak(self,ast,c):
        checklst = c[:-3]
        for scope in checklst:
            if "for" in map(lambda x: x.name, scope):return c
        raise MustInLoop(ast)
    
    
    def visitContinue(self,ast,c):
        checklst = c[:-3]
        for scope in checklst:
            if "for" in map(lambda x: x.name, scope):return c
        raise MustInLoop(ast)
    
    def visitReturn(self,ast,c):
        funcret = next(filter(lambda x : x.name == 'func', c[-5]),None)
        if ast.expr:
            exprrt = self.visit(ast.expr,c)
            if str(funcret.typ) != str(exprrt):
                raise TypeMismatchInStatement(ast)
        else:
                if str(funcret.typ) != 'VoidType':
                    raise TypeMismatchInStatement(ast)
        return c
    
    def visitCallStmt(self,ast,c):
        if ast.obj:
            obj = self.visit(ast.obj,c)
            objstr = str(obj)[:4]
            memberaccess = None
            if objstr == 'Clas':
                classlist = c[-1]
                classaccess = next(filter(lambda x: x.name == obj.classname.name , classlist),None)
                memberaccess =  next(filter(lambda x: x.name == ast.method.name , classaccess.member),None)
                if not memberaccess:
                    raise Undeclared(Method(),ast.method.name)
                if not memberaccess.isFunc:
                    raise TypeMismatchInStatement(ast)
                if str(memberaccess.typ.rettype) != "VoidType":
                    raise TypeMismatchInStatement(ast)
                if len(ast.param) !=  len(memberaccess.typ.partype):
                    raise TypeMismatchInStatement(ast)
                for i in range(0,len(ast.param)):
                    if str(memberaccess.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                        raise TypeMismatchInStatement(ast)
                return c
            if objstr == 'Self':
                ooplist=c[-3]
                memberaccess =  next(filter(lambda x: x.name == ast.method.name , ooplist),None)
                if not memberaccess:
                    raise Undeclared(Method(),ast.method.name)
                if not memberaccess.isFunc:
                    raise TypeMismatchInStatement(ast)
                if str(memberaccess.typ.rettype) != "VoidType":
                    raise TypeMismatchInStatement(ast)
                if len(ast.param) !=  len(memberaccess.typ.partype):
                    raise TypeMismatchInStatement(ast)
                for i in range(0,len(ast.param)):
                    if str(memberaccess.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                        raise TypeMismatchInStatement(ast)
                return c
            raise TypeMismatchInStatement(ast)
        else:
            globallist=c[-2]
            memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , globallist),None)
            if not memberaccess:
                raise Undeclared(Method(),ast.fieldname.name)
            if not memberaccess.isFunc:
                raise TypeMismatchInStatement(ast)
            if str(memberaccess.typ.rettype) != "VoidType":
                raise TypeMismatchInStatement(ast)
            if len(ast.param) !=  len(memberaccess.typ.partype):
                raise TypeMismatchInStatement(ast)
            for i in range(0,len(ast.param)):
                if str(memberaccess.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                    raise TypeMismatchInStatement(ast)
            return c
    
    def visitExpr(self,ast,c):
        return self.visit(ast.Expr,c)
    
    def visitId(self,ast,c):
        accessScopelst = c[:-3]
        idattri = None
        for scope in accessScopelst:
            idattri = next(filter(lambda x: x.name == ast.name ,scope),None)
            if idattri:
                break
        if not idattri:
            raise Undeclared(Attribute(),ast.name)##############
        return idattri.typ
        
    def visitArrayCell(self,ast,c):
        arr = self.visit(ast.arr,c)
        arrstr= arr
        if arrstr in StaticChecker.notArraytype:#############
            raise TypeMismatchInExpression(ast)
        expr = str(self.visit(ast.idx,c))
        if expr != str(StaticChecker.inttype):#################
            raise TypeMismatchInExpression(ast)
        return arr.eleType
    
    def visitFieldAccess(self,ast,c):
        if ast.obj:
            obj = self.visit(ast.obj,c)
            objstr = str(obj)[:4]
            memberaccess = None
            if objstr == 'Clas':
                classlist = c[-1]
                classaccess = next(filter(lambda x: x.name == obj.classname.name , classlist),None)
                memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , classaccess.member),None)
                if not memberaccess and not memberaccess.isFunc:
                    raise Undeclared(Attribute(),ast.fieldname.name) 
                return memberaccess.typ
            if objstr == 'Self':
                ooplist=c[-3]
                memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , ooplist),None)
                if not memberaccess and not memberaccess.isFunc:
                    raise Undeclared(Attribute(),ast.fieldname.name)
                return memberaccess.typ
            raise TypeMismatchInExpression(ast)
        else:
            globallist=c[-2]
            memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , globallist),None)
            if not memberaccess:
                raise Undeclared(Attribute(),ast.fieldname.name)###############
            if memberaccess.isFunc:
                raise TypeMismatchInExpression(ast)
            return memberaccess.typ
    
    def visitBinaryOp(self,ast,c):
        left = self.visit(ast.left,c)
        right =self.visit(ast.right,c)
        if not (left in StaticChecker.notArraytype and right in StaticChecker.notArraytype):
            raise TypeMismatchInExpression(ast)
        comparedtype = compareType(left,right)
        if not comparedtype:
            raise TypeMismatchInExpression(ast)
        compareop1 = ['==','!='] #int/bool comparison
        compareop2 = ['<','>','<=','>='] #int/float
        logicalop = ['&&','||'] #logical operator
        stringop = ['^']
        arithopIF = ['-','*','+']
        arithopI = ['\\','%']
        arithopF = ['/']        
        if ast.op in compareop1 and (comparedtype == StaticChecker.inttype or comparedtype == StaticChecker.booltype) :
            return StaticChecker.booltype
        if ast.op in compareop2 and (comparedtype == StaticChecker.inttype or comparedtype == StaticChecker.floattype) :
            return StaticChecker.booltype
        if ast.op in logicalop and comparedtype == StaticChecker.booltype:
            return StaticChecker.booltype
        if ast.op in stringop and comparedtype == StaticChecker.stringtype:
            return comparedtype
        if ast.op in arithopIF and (comparedtype == StaticChecker.inttype or comparedtype == StaticChecker.floattype) :
            return comparedtype
        if ast.op in arithopI and comparedtype == StaticChecker.inttype:
            return comparedtype
        if ast.op in arithopF and comparedtype == StaticChecker.floattype:
            return comparedtype
        raise TypeMismatchInExpression(ast)
               
    
    def visitUnaryOp(self,ast,c):
        body = self.visit(ast.body,c)
        if ast.op == '-' and (body == StaticChecker.inttype or body == StaticChecker.floattype) :
            return body
        if ast.op == '!' and body == StaticChecker.booltype :
            return body
        raise TypeMismatchInExpression(ast) 
    
    def visitCallExpr(self,ast,c):
        if ast.obj:
            obj = self.visit(ast.obj,c)
            objstr = str(obj)[:4]
            memberaccess = None
            if objstr == 'Clas':
                classlist = c[-1]
                classaccess = next(filter(lambda x: x.name == obj.classname.name , classlist),None)
                memberaccess =  next(filter(lambda x: x.name == ast.method.name , classaccess.member),None)
                if not memberaccess:
                    raise Undeclared(Method(),ast.fieldname.name)
                if not memberaccess.isFunc:
                    raise TypeMismatchInExpression(ast)
                if str(memberaccess.typ.rettype) == "VoidType":
                    raise TypeMismatchInExpression(ast)
                if len(ast.param) !=  len(memberaccess.typ.partype):
                    raise TypeMismatchInExpression(ast)
                for i in range(0,len(ast.param)):
                    if str(memberaccess.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                        raise TypeMismatchInExpression(ast)
                return memberaccess.typ.rettype
            if objstr == 'Self':
                ooplist=c[-3]
                memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , ooplist),None)
                if not memberaccess:
                    raise Undeclared(Method(),ast.fieldname.name)
                if not memberaccess.isFunc:
                    raise TypeMismatchInExpression(ast)
                if str(memberaccess.typ.rettype) == "VoidType":
                    raise TypeMismatchInExpression(ast)
                if len(ast.param) !=  len(memberaccess.typ.partype):
                    raise TypeMismatchInExpression(ast)
                for i in range(0,len(ast.param)):
                    if str(memberaccess.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                        raise TypeMismatchInExpression(ast)
                return memberaccess.typ.rettype
            raise TypeMismatchInExpression(ast)
        else:
            globallist=c[-2]
            memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , globallist),None)
            if not memberaccess:
                raise Undeclared(Method(),ast.fieldname.name)
            if not memberaccess.isFunc:
                raise TypeMismatchInExpression(ast)
            if str(memberaccess.typ.rettype) == "VoidType":
                raise TypeMismatchInExpression(ast)
            if len(ast.param) !=  len(memberaccess.typ.partype):
                raise TypeMismatchInExpression(ast)
            for i in range(0,len(ast.param)):
                if str(memberaccess.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                    raise TypeMismatchInExpression(ast)
            return memberaccess.typ
    
    def visitNewExpr(self,ast,c):
        idclass = next(filter(lambda x: x.name == ast.classname.name , c[-1]),None)
        if not idclass:
            raise Undeclared(Class(),ast.classname.name)
        constructor = list(filter(lambda x: x.name == 'constructor' , idclass.member))
        if len(constructor) == 0 :
            raise TypeMismatchInExpression(ast)
        for constr in constructor:
            if len(ast.param) !=  len(constr.typ.partype):
                continue
            for i in range(0,len(ast.param)):
                if str(constr.typ.partype[i]) != str(self.visit(ast.param[i],c)):
                    continue
            return ClassType(ast.classname)
        raise TypeMismatchInExpression(ast)
            
    
    def visitLiteral(self,ast,c):
        return self.visit(ast,c)
    
    def visitIntLiteral(self,ast,c):
        return StaticChecker.inttype
    
    def visitFloatLiteral(self,ast,c):
        return StaticChecker.floattype
    
    def visitStringLiteral(self,ast,c):
        return StaticChecker.stringtype
    
    def visitBooleanLiteral(self,ast,c):
        return StaticChecker.booltype
    
    def visitNullLiteral(self,ast,c):
        return None
    
    def visitSelfLiteral(self,ast,c):
        return StaticChecker.selflitteral
    
    def visitArrayLiteral(self,ast,c):
        keytype= self.visit(ast.value[0],c)
        count = 1
        for x in ast.value[1:]:
            value = str(self.visit(x,c))
            count +=1
            if value != str(keytype):
                raise IllegalArrayLiteral(ast)
        return ArrayType(count,keytype) 
    
    def visitType(self,ast,c):
        return self.visit(ast.Type,c)
    
    def visitIntType(self,ast,c):
        return str(ast)
    
    def visitFloatType(self,ast,c):
        return str(ast)
    
    def visitBoolType(self,ast,c):
        return str(ast)
    
    def visitStringType(self,ast,c):
        return str(ast)
    
    def visitArrayType(self,ast,c):
        return str(ast)
    
    def visitClassType(self,ast,c):
        if not ast.classname.name in map(lambda x: x.name ,c):
            raise Undeclared(Class(),ast.classname.name)
        return str(ast)
    
    def visitVoidType(self,ast,c):
        return str(ast)
    
class LeftHandSide(BaseVisitor,Utils):
    def visitId(self,ast,c):
        accessScopelst = c[:-3]
        idattri = None
        for scope in accessScopelst:
            idattri = next(filter(lambda x: x.name == ast.name ,scope),None)
            if idattri:
                break
        if not idattri:
            raise Undeclared(Attribute(),ast.name)
        return idattri.typ, idattri.isMu
        
    def visitArrayCell(self,ast,c):
        arr = self.visit(ast.arr,c)#->must id/field cuz teacher said cant be a[][]
        arrstr= arr[0]
        if arrstr in StaticChecker.notArraytype:#############
            raise TypeMismatchInExpression(ast)
        expr = str(StaticChecker(ast).visit(ast.idx,c))
        if expr != str(StaticChecker.inttype):#################
            raise TypeMismatchInExpression(ast)
        return arr[0].eleType , arr[1] 
    
    def visitFieldAccess(self,ast,c):
        if ast.obj:
            obj = self.visit(ast.obj,c)
            objstr = str(obj[0])[:4]
            memberaccess = None
            if objstr == 'Clas':
                classlist = c[-1]
                classaccess = next(filter(lambda x: x.name == obj[0].classname.name , classlist),None)
                memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , classaccess.member),None)
                if not memberaccess:
                    raise Undeclared(Attribute(),ast.fieldname.name) 
                return memberaccess.typ , memberaccess.isMu
            if objstr == 'Self':
                ooplist=c[-3]
                memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , ooplist),None)
                if not memberaccess:
                    raise Undeclared(Attribute(),ast.fieldname.name)
                return memberaccess.typ , memberaccess.isMu
            raise TypeMismatchInExpression(ast)
        else:
            globallist=c[-2]
            memberaccess =  next(filter(lambda x: x.name == ast.fieldname.name , globallist),None)
            if not memberaccess:
                raise Undeclared(Attribute(),ast.fieldname.name)
            return memberaccess.typ , memberaccess.isMu
        
    def visitSelfLiteral(self,ast,c):
        return StaticChecker(ast).selflitteral , True
    

def compareType(left,right):
    returntype=left
    if not (left or right):
        return False
    left = str(left)
    right = str(right)
    if left == str(StaticChecker.floattype):
        if right == str(StaticChecker.floattype) or right == str(StaticChecker.inttype):
            return StaticChecker.floattype
        return False
    if right == str(StaticChecker.floattype):
        if left == str(StaticChecker.floattype) or left == str(StaticChecker.inttype):
            return StaticChecker.floattype
        return False
    if left == right :
        return returntype
    else:
        return False
        