from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):
    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return Program([x.accept(self) for x in ctx.class_dcl()])


    # Visit a parse tree produced by CSlangParser#class_dcl.
    def visitClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        memlist= []
        for body in ctx.class_body():
            memlist += body.accept(self)
        if ctx.SUPER_CLASS():
            return ClassDecl(Id(ctx.getChild(3).getText()),memlist,Id(ctx.getChild(1).getText()))
        return ClassDecl(Id(ctx.getChild(1).getText()),memlist,None)


    # Visit a parse tree produced by CSlangParser#class_body.
    def visitClass_body(self, ctx:CSlangParser.Class_bodyContext):
        if ctx.storedecl():
            return [AttributeDecl(a) for a in ctx.storedecl().accept(self)]
        return [ctx.getChild(0).accept(self)]


    # Visit a parse tree produced by CSlangParser#method_dcl.
    def visitMethod_dcl(self, ctx:CSlangParser.Method_dclContext):
        return MethodDecl(Id(ctx.getChild(1).getText()),ctx.getChild(3).accept(self),VoidType(),ctx.getChild(7).accept(self)) if ctx.VOID() else MethodDecl(Id(ctx.getChild(1).getText()),ctx.getChild(3).accept(self),ctx.getChild(6).accept(self),ctx.getChild(7).accept(self))


    # Visit a parse tree produced by CSlangParser#constructor_decl.
    def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        return MethodDecl(Id(ctx.getChild(1).getText()),ctx.getChild(3).accept(self),VoidType(),ctx.getChild(5).accept(self))


    # Visit a parse tree produced by CSlangParser#param_lst.
    def visitParam_lst(self, ctx:CSlangParser.Param_lstContext):
        if ctx.getChildCount()==0:
            return []
        return [a for b in ctx.param() for a in b.accept(self)]
        

    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        if ctx.idlst():
            return [VarDecl(a,ctx.getChild(2).accept(self),None) for a in ctx.getChild(0).accept(self)]
        return [VarDecl(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self),None)]


    # Visit a parse tree produced by CSlangParser#statements.
    def visitStatements(self, ctx:CSlangParser.StatementsContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#storedecl.
    def visitStoredecl(self, ctx:CSlangParser.StoredeclContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#constdecl.
    def visitConstdecl(self, ctx:CSlangParser.ConstdeclContext):
        if ctx.non_inital_decl():
            constDeclLst= ctx.getChild(1).accept(self) #[[]]->[] aaaaaaa cuu toi
            return [ConstDecl(a[0],a[1],None) for a in constDeclLst]
        else:
            constDeclLst = []
            sublist = ctx.getChild(1).accept(self) #[1,[2,3],4]->[[1,2],[1,3]]
            n = len(sublist) - 1
            x = int(n/2)
            for i in range(0,x):
                childlist =[]
                childlist.append(sublist[i])
                childlist.append(sublist[x])
                childlist.append(sublist[x+1+i])
                constDeclLst.append(childlist)
            return [ConstDecl(a[0],a[1],a[2]) for a in constDeclLst]


    # Visit a parse tree produced by CSlangParser#vardecl.
    def visitVardecl(self, ctx:CSlangParser.VardeclContext):
        if ctx.non_inital_decl():
            varDeclLst= ctx.getChild(1).accept(self) #[[]]->[] aaaaaaa cuu toi
            return [VarDecl(a[0],a[1],None) for a in varDeclLst]
        else:
            varDeclLst = []
            sublist = ctx.getChild(1).accept(self)
            n = len(sublist) - 1
            x = int(n/2)
            for i in range(0,x):
                childlist =[]
                childlist.append(sublist[i])
                childlist.append(sublist[x])
                childlist.append(sublist[x+1+i])
                varDeclLst.append(childlist)
            return [VarDecl(a[0],a[1],a[2]) for a in varDeclLst]


    # Visit a parse tree produced by CSlangParser#non_inital_decl.
    def visitNon_inital_decl(self, ctx:CSlangParser.Non_inital_declContext):
        idlst=ctx.getChild(0).accept(self) #list of identifiers
        lst=[[x,ctx.getChild(2).accept(self)] for x in idlst]
        return lst


    # Visit a parse tree produced by CSlangParser#inital_decl.
    def visitInital_decl(self, ctx:CSlangParser.Inital_declContext):
        if not ctx.inital_decl():
            return [ctx.getChild(0).accept(self),ctx.getChild(2).accept(self),ctx.getChild(4).accept(self)]
        else:
            return [ctx.getChild(0).accept(self)] + ctx.getChild(2).accept(self) + [ctx.getChild(4).accept(self)]

    # Visit a parse tree produced by CSlangParser#assigndecl.
    def visitAssigndecl(self, ctx:CSlangParser.AssigndeclContext):
        return [ctx.getChild(0).accept(self)]


    # Visit a parse tree produced by CSlangParser#assign.
    def visitAssign(self, ctx:CSlangParser.AssignContext):
        return Assign(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#ifstmt.
    def visitIfstmt(self, ctx:CSlangParser.IfstmtContext):
        if ctx.getChildCount() ==3:
            return [If(ctx.getChild(1).accept(self),ctx.getChild(2).accept(self),None,None)]
        if ctx.getChildCount() ==4:
            return [If(ctx.getChild(2).accept(self),ctx.getChild(3).accept(self),ctx.getChild(1).accept(self),None)]
        if ctx.getChildCount() ==5:   
            return [If(ctx.getChild(1).accept(self),ctx.getChild(2).accept(self),None,ctx.getChild(4).accept(self))]
        return [If(ctx.getChild(2).accept(self),ctx.getChild(3).accept(self),ctx.getChild(1).accept(self),ctx.getChild(5).accept(self))]

    # Visit a parse tree produced by CSlangParser#forstmt.
    def visitForstmt(self, ctx:CSlangParser.ForstmtContext):
        return [For(ctx.getChild(1).accept(self),ctx.getChild(3).accept(self),ctx.getChild(5).accept(self),ctx.getChild(6).accept(self))]


    # Visit a parse tree produced by CSlangParser#continue_state.
    def visitContinue_state(self, ctx:CSlangParser.Continue_stateContext):
        return [Continue()]


    # Visit a parse tree produced by CSlangParser#return_state.
    def visitReturn_state(self, ctx:CSlangParser.Return_stateContext):
        if ctx.expr():
            return [Return(ctx.getChild(1).accept(self))]
        return [Return(None)]

    # Visit a parse tree produced by CSlangParser#break_state.
    def visitBreak_state(self, ctx:CSlangParser.Break_stateContext):
        return [Break()]


    # Visit a parse tree produced by CSlangParser#callstmt.
    def visitCallstmt(self, ctx:CSlangParser.CallstmtContext):
        return [ctx.getChild(0).accept(self)]


    # Visit a parse tree produced by CSlangParser#instance_method_invo_access.
    def visitInstance_method_invo_access(self, ctx:CSlangParser.Instance_method_invo_accessContext):
        if ctx.LBRACK():
            return CallStmt(ArrayCell(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self)),Id(ctx.getChild(5).getText()),ctx.getChild(7).accept(self))
        return CallStmt(ctx.getChild(0).accept(self), Id(ctx.getChild(2).getText()), ctx.getChild(4).accept(self))


    # Visit a parse tree produced by CSlangParser#static_method_invo_access.
    def visitStatic_method_invo_access(self, ctx:CSlangParser.Static_method_invo_accessContext):
        if ctx.DOT():
            return CallStmt(Id(ctx.getChild(0).getText()),Id(ctx.getChild(2).getText()),ctx.getChild(4).accept(self))
        return CallStmt(None,Id(ctx.getChild(0).getText()),ctx.getChild(2).accept(self))

    # Visit a parse tree produced by CSlangParser#io_st.
    def visitIo_st(self, ctx:CSlangParser.Io_stContext):
        a,b = ctx.getChild(2).accept(self)
        return CallStmt(ctx.getChild(0).accept(self),a,b )


    # Visit a parse tree produced by CSlangParser#block.
    def visitBlock(self, ctx:CSlangParser.BlockContext):
        stmtlst = []
        for a in ctx.statements():
            stmtlst += a.accept(self)
        return Block(stmtlst)


    # Visit a parse tree produced by CSlangParser#io_mt.
    def visitIo_mt(self, ctx:CSlangParser.Io_mtContext):
        if ctx.getChildCount()==3:
            return Id(ctx.getChild(0).getText()) , []
        return Id(ctx.getChild(0).getText()) , [ctx.getChild(2).accept(self)]


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#arraycell.
    def visitArraycell(self, ctx:CSlangParser.ArraycellContext):
        return ArrayCell(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#fieldaccess.
    def visitFieldaccess(self, ctx:CSlangParser.FieldaccessContext):
        if ctx.AT_ID():
            if ctx.getChildCount()==1:
                return FieldAccess(None, Id(ctx.getChild(0).getText()))
            return FieldAccess(Id(ctx.getChild(0).getText()), Id(ctx.getChild(2).getText()))
        if ctx.LBRACK():
            return FieldAccess(ArrayCell(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self)),Id(ctx.getChild(5).getText()))
        return FieldAccess(ctx.getChild(0).accept(self),Id(ctx.getChild(2).getText()))

    # Visit a parse tree produced by CSlangParser#idlst.
    def visitIdlst(self, ctx:CSlangParser.IdlstContext):
        return [a.accept(self) for a in ctx.iden()]


    # Visit a parse tree produced by CSlangParser#iden.
    def visitIden(self, ctx:CSlangParser.IdenContext):
        return Id(ctx.getChild(0).getText()) if ctx.ID() else FieldAccess(None,Id(ctx.getChild(0).getText()))


    # Visit a parse tree produced by CSlangParser#expr_lst.
    def visitExpr_lst(self, ctx:CSlangParser.Expr_lstContext):
        return [a.accept(self) for a in ctx.expr()]


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return BinaryOp(ctx.getChild(1).getText(),ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


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
        return UnaryOp('!',ctx.getChild(1).accept(self))


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        if ctx.expr7():
            return ctx.expr7().accept(self)
        return UnaryOp('-',ctx.getChild(1).accept(self))


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        if ctx.getChildCount()==1:
            return ctx.getChild(0).accept(self)
        return ArrayCell(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self))


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        if ctx.expr9():
            return ctx.getChild(0).accept(self)
        if ctx.LBRACK():
            if ctx.LPAREN():
                return CallExpr(ArrayCell(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self)),Id(ctx.getChild(5).getText()),ctx.getChild(7).accept(self))
            return FieldAccess(ArrayCell(ctx.getChild(0).accept(self),ctx.getChild(2).accept(self)),Id(ctx.getChild(5).getText()))
        else:
            if ctx.LPAREN():
                return CallExpr(ctx.getChild(0).accept(self),Id(ctx.getChild(2).getText()),ctx.getChild(4).accept(self))    
            return FieldAccess(ctx.getChild(0).accept(self),Id(ctx.getChild(2).getText()))
            
   
    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        if ctx.expr10():
            return ctx.getChild(0).accept(self)
        if ctx.DOT():
            if ctx.getChildCount()==3:
                return FieldAccess(Id(ctx.getChild(0).getText()),Id(ctx.getChild(2).getText()))
            return CallExpr(Id(ctx.getChild(0).getText()),Id(ctx.getChild(2).getText()),ctx.getChild(4).accept(self))
        if ctx.getChildCount()==1:
            return FieldAccess(None,Id(ctx.getChild(0).getText()))
        return CallExpr(None,Id(ctx.getChild(0).getText()),ctx.getChild(2).accept(self))

    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return ctx.getChild(0).accept(self) if ctx.getChildCount()==1 else NewExpr(Id(ctx.getChild(1).getText()), ctx.getChild(3).accept(self))


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        if ctx.ID():
            return Id(ctx.getChild(0).getText())
        if ctx.literal():
            return ctx.getChild(0).accept(self)
        if ctx.SELF():
            return SelfLiteral()
        if ctx.NULL():
            return NullLiteral()
        return ctx.getChild(1).accept(self)

    # Visit a parse tree produced by CSlangParser#relational.
    def visitRelational(self, ctx:CSlangParser.RelationalContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#relat_bool.
    def visitRelat_bool(self, ctx:CSlangParser.Relat_boolContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CSlangParser#relat_int_float.
    def visitRelat_int_float(self, ctx:CSlangParser.Relat_int_floatContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CSlangParser#multiplying.
    def visitMultiplying(self, ctx:CSlangParser.MultiplyingContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CSlangParser#adding.
    def visitAdding(self, ctx:CSlangParser.AddingContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CSlangParser#logical_bin.
    def visitLogical_bin(self, ctx:CSlangParser.Logical_binContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CSlangParser#logical_not.
    def visitLogical_not(self, ctx:CSlangParser.Logical_notContext):
        return ctx.getChild(0).getText()


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


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return ArrayType(int(ctx.getChild(1).getText()), ctx.getChild(3).accept(self))


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        if ctx.INT_LITERAL() or ctx.NON_ZERO_INT():
            return IntLiteral(int(ctx.getChild(0).getText()))
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.getChild(0).getText()))
        if ctx.bool_literal():
            return ctx.getChild(0).accept(self)    
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.getChild(0).getText())
        if ctx.array():
            return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CSlangParser#bool_literal.
    def visitBool_literal(self, ctx:CSlangParser.Bool_literalContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        return BooleanLiteral(False)


    # Visit a parse tree produced by CSlangParser#array.
    def visitArray(self, ctx:CSlangParser.ArrayContext):
        return ArrayLiteral([a.accept(self) for a in ctx.literal()])
   

