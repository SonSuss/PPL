# Generated from e:/hocbaidcm/PPL/assignment/assign2/assignment2-initial/assignment2-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete listener for a parse tree produced by CSlangParser.
class CSlangListener(ParseTreeListener):

    # Enter a parse tree produced by CSlangParser#program.
    def enterProgram(self, ctx:CSlangParser.ProgramContext):
        pass

    # Exit a parse tree produced by CSlangParser#program.
    def exitProgram(self, ctx:CSlangParser.ProgramContext):
        pass


    # Enter a parse tree produced by CSlangParser#class_dcl.
    def enterClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        pass

    # Exit a parse tree produced by CSlangParser#class_dcl.
    def exitClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        pass


    # Enter a parse tree produced by CSlangParser#class_body.
    def enterClass_body(self, ctx:CSlangParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by CSlangParser#class_body.
    def exitClass_body(self, ctx:CSlangParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by CSlangParser#method_dcl.
    def enterMethod_dcl(self, ctx:CSlangParser.Method_dclContext):
        pass

    # Exit a parse tree produced by CSlangParser#method_dcl.
    def exitMethod_dcl(self, ctx:CSlangParser.Method_dclContext):
        pass


    # Enter a parse tree produced by CSlangParser#constructor_decl.
    def enterConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        pass

    # Exit a parse tree produced by CSlangParser#constructor_decl.
    def exitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        pass


    # Enter a parse tree produced by CSlangParser#param_lst.
    def enterParam_lst(self, ctx:CSlangParser.Param_lstContext):
        pass

    # Exit a parse tree produced by CSlangParser#param_lst.
    def exitParam_lst(self, ctx:CSlangParser.Param_lstContext):
        pass


    # Enter a parse tree produced by CSlangParser#param.
    def enterParam(self, ctx:CSlangParser.ParamContext):
        pass

    # Exit a parse tree produced by CSlangParser#param.
    def exitParam(self, ctx:CSlangParser.ParamContext):
        pass


    # Enter a parse tree produced by CSlangParser#statements.
    def enterStatements(self, ctx:CSlangParser.StatementsContext):
        pass

    # Exit a parse tree produced by CSlangParser#statements.
    def exitStatements(self, ctx:CSlangParser.StatementsContext):
        pass


    # Enter a parse tree produced by CSlangParser#storedecl.
    def enterStoredecl(self, ctx:CSlangParser.StoredeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#storedecl.
    def exitStoredecl(self, ctx:CSlangParser.StoredeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#constdecl.
    def enterConstdecl(self, ctx:CSlangParser.ConstdeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#constdecl.
    def exitConstdecl(self, ctx:CSlangParser.ConstdeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#vardecl.
    def enterVardecl(self, ctx:CSlangParser.VardeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#vardecl.
    def exitVardecl(self, ctx:CSlangParser.VardeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#non_inital_decl.
    def enterNon_inital_decl(self, ctx:CSlangParser.Non_inital_declContext):
        pass

    # Exit a parse tree produced by CSlangParser#non_inital_decl.
    def exitNon_inital_decl(self, ctx:CSlangParser.Non_inital_declContext):
        pass


    # Enter a parse tree produced by CSlangParser#inital_decl.
    def enterInital_decl(self, ctx:CSlangParser.Inital_declContext):
        pass

    # Exit a parse tree produced by CSlangParser#inital_decl.
    def exitInital_decl(self, ctx:CSlangParser.Inital_declContext):
        pass


    # Enter a parse tree produced by CSlangParser#assigndecl.
    def enterAssigndecl(self, ctx:CSlangParser.AssigndeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#assigndecl.
    def exitAssigndecl(self, ctx:CSlangParser.AssigndeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#assign.
    def enterAssign(self, ctx:CSlangParser.AssignContext):
        pass

    # Exit a parse tree produced by CSlangParser#assign.
    def exitAssign(self, ctx:CSlangParser.AssignContext):
        pass


    # Enter a parse tree produced by CSlangParser#ifstmt.
    def enterIfstmt(self, ctx:CSlangParser.IfstmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#ifstmt.
    def exitIfstmt(self, ctx:CSlangParser.IfstmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#forstmt.
    def enterForstmt(self, ctx:CSlangParser.ForstmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#forstmt.
    def exitForstmt(self, ctx:CSlangParser.ForstmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#continue_state.
    def enterContinue_state(self, ctx:CSlangParser.Continue_stateContext):
        pass

    # Exit a parse tree produced by CSlangParser#continue_state.
    def exitContinue_state(self, ctx:CSlangParser.Continue_stateContext):
        pass


    # Enter a parse tree produced by CSlangParser#return_state.
    def enterReturn_state(self, ctx:CSlangParser.Return_stateContext):
        pass

    # Exit a parse tree produced by CSlangParser#return_state.
    def exitReturn_state(self, ctx:CSlangParser.Return_stateContext):
        pass


    # Enter a parse tree produced by CSlangParser#break_state.
    def enterBreak_state(self, ctx:CSlangParser.Break_stateContext):
        pass

    # Exit a parse tree produced by CSlangParser#break_state.
    def exitBreak_state(self, ctx:CSlangParser.Break_stateContext):
        pass


    # Enter a parse tree produced by CSlangParser#callstmt.
    def enterCallstmt(self, ctx:CSlangParser.CallstmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#callstmt.
    def exitCallstmt(self, ctx:CSlangParser.CallstmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#instance_method_invo_access.
    def enterInstance_method_invo_access(self, ctx:CSlangParser.Instance_method_invo_accessContext):
        pass

    # Exit a parse tree produced by CSlangParser#instance_method_invo_access.
    def exitInstance_method_invo_access(self, ctx:CSlangParser.Instance_method_invo_accessContext):
        pass


    # Enter a parse tree produced by CSlangParser#static_method_invo_access.
    def enterStatic_method_invo_access(self, ctx:CSlangParser.Static_method_invo_accessContext):
        pass

    # Exit a parse tree produced by CSlangParser#static_method_invo_access.
    def exitStatic_method_invo_access(self, ctx:CSlangParser.Static_method_invo_accessContext):
        pass


    # Enter a parse tree produced by CSlangParser#io_st.
    def enterIo_st(self, ctx:CSlangParser.Io_stContext):
        pass

    # Exit a parse tree produced by CSlangParser#io_st.
    def exitIo_st(self, ctx:CSlangParser.Io_stContext):
        pass


    # Enter a parse tree produced by CSlangParser#block.
    def enterBlock(self, ctx:CSlangParser.BlockContext):
        pass

    # Exit a parse tree produced by CSlangParser#block.
    def exitBlock(self, ctx:CSlangParser.BlockContext):
        pass


    # Enter a parse tree produced by CSlangParser#io_mt.
    def enterIo_mt(self, ctx:CSlangParser.Io_mtContext):
        pass

    # Exit a parse tree produced by CSlangParser#io_mt.
    def exitIo_mt(self, ctx:CSlangParser.Io_mtContext):
        pass


    # Enter a parse tree produced by CSlangParser#lhs.
    def enterLhs(self, ctx:CSlangParser.LhsContext):
        pass

    # Exit a parse tree produced by CSlangParser#lhs.
    def exitLhs(self, ctx:CSlangParser.LhsContext):
        pass


    # Enter a parse tree produced by CSlangParser#arraycell.
    def enterArraycell(self, ctx:CSlangParser.ArraycellContext):
        pass

    # Exit a parse tree produced by CSlangParser#arraycell.
    def exitArraycell(self, ctx:CSlangParser.ArraycellContext):
        pass


    # Enter a parse tree produced by CSlangParser#fieldaccess.
    def enterFieldaccess(self, ctx:CSlangParser.FieldaccessContext):
        pass

    # Exit a parse tree produced by CSlangParser#fieldaccess.
    def exitFieldaccess(self, ctx:CSlangParser.FieldaccessContext):
        pass


    # Enter a parse tree produced by CSlangParser#idlst.
    def enterIdlst(self, ctx:CSlangParser.IdlstContext):
        pass

    # Exit a parse tree produced by CSlangParser#idlst.
    def exitIdlst(self, ctx:CSlangParser.IdlstContext):
        pass


    # Enter a parse tree produced by CSlangParser#iden.
    def enterIden(self, ctx:CSlangParser.IdenContext):
        pass

    # Exit a parse tree produced by CSlangParser#iden.
    def exitIden(self, ctx:CSlangParser.IdenContext):
        pass


    # Enter a parse tree produced by CSlangParser#expr_lst.
    def enterExpr_lst(self, ctx:CSlangParser.Expr_lstContext):
        pass

    # Exit a parse tree produced by CSlangParser#expr_lst.
    def exitExpr_lst(self, ctx:CSlangParser.Expr_lstContext):
        pass


    # Enter a parse tree produced by CSlangParser#expr.
    def enterExpr(self, ctx:CSlangParser.ExprContext):
        pass

    # Exit a parse tree produced by CSlangParser#expr.
    def exitExpr(self, ctx:CSlangParser.ExprContext):
        pass


    # Enter a parse tree produced by CSlangParser#expr1.
    def enterExpr1(self, ctx:CSlangParser.Expr1Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr1.
    def exitExpr1(self, ctx:CSlangParser.Expr1Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr2.
    def enterExpr2(self, ctx:CSlangParser.Expr2Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr2.
    def exitExpr2(self, ctx:CSlangParser.Expr2Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr3.
    def enterExpr3(self, ctx:CSlangParser.Expr3Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr3.
    def exitExpr3(self, ctx:CSlangParser.Expr3Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr4.
    def enterExpr4(self, ctx:CSlangParser.Expr4Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr4.
    def exitExpr4(self, ctx:CSlangParser.Expr4Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr5.
    def enterExpr5(self, ctx:CSlangParser.Expr5Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr5.
    def exitExpr5(self, ctx:CSlangParser.Expr5Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr6.
    def enterExpr6(self, ctx:CSlangParser.Expr6Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr6.
    def exitExpr6(self, ctx:CSlangParser.Expr6Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr7.
    def enterExpr7(self, ctx:CSlangParser.Expr7Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr7.
    def exitExpr7(self, ctx:CSlangParser.Expr7Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr8.
    def enterExpr8(self, ctx:CSlangParser.Expr8Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr8.
    def exitExpr8(self, ctx:CSlangParser.Expr8Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr9.
    def enterExpr9(self, ctx:CSlangParser.Expr9Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr9.
    def exitExpr9(self, ctx:CSlangParser.Expr9Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr10.
    def enterExpr10(self, ctx:CSlangParser.Expr10Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr10.
    def exitExpr10(self, ctx:CSlangParser.Expr10Context):
        pass


    # Enter a parse tree produced by CSlangParser#expr11.
    def enterExpr11(self, ctx:CSlangParser.Expr11Context):
        pass

    # Exit a parse tree produced by CSlangParser#expr11.
    def exitExpr11(self, ctx:CSlangParser.Expr11Context):
        pass


    # Enter a parse tree produced by CSlangParser#relational.
    def enterRelational(self, ctx:CSlangParser.RelationalContext):
        pass

    # Exit a parse tree produced by CSlangParser#relational.
    def exitRelational(self, ctx:CSlangParser.RelationalContext):
        pass


    # Enter a parse tree produced by CSlangParser#relat_bool.
    def enterRelat_bool(self, ctx:CSlangParser.Relat_boolContext):
        pass

    # Exit a parse tree produced by CSlangParser#relat_bool.
    def exitRelat_bool(self, ctx:CSlangParser.Relat_boolContext):
        pass


    # Enter a parse tree produced by CSlangParser#relat_int_float.
    def enterRelat_int_float(self, ctx:CSlangParser.Relat_int_floatContext):
        pass

    # Exit a parse tree produced by CSlangParser#relat_int_float.
    def exitRelat_int_float(self, ctx:CSlangParser.Relat_int_floatContext):
        pass


    # Enter a parse tree produced by CSlangParser#multiplying.
    def enterMultiplying(self, ctx:CSlangParser.MultiplyingContext):
        pass

    # Exit a parse tree produced by CSlangParser#multiplying.
    def exitMultiplying(self, ctx:CSlangParser.MultiplyingContext):
        pass


    # Enter a parse tree produced by CSlangParser#adding.
    def enterAdding(self, ctx:CSlangParser.AddingContext):
        pass

    # Exit a parse tree produced by CSlangParser#adding.
    def exitAdding(self, ctx:CSlangParser.AddingContext):
        pass


    # Enter a parse tree produced by CSlangParser#logical_bin.
    def enterLogical_bin(self, ctx:CSlangParser.Logical_binContext):
        pass

    # Exit a parse tree produced by CSlangParser#logical_bin.
    def exitLogical_bin(self, ctx:CSlangParser.Logical_binContext):
        pass


    # Enter a parse tree produced by CSlangParser#logical_not.
    def enterLogical_not(self, ctx:CSlangParser.Logical_notContext):
        pass

    # Exit a parse tree produced by CSlangParser#logical_not.
    def exitLogical_not(self, ctx:CSlangParser.Logical_notContext):
        pass


    # Enter a parse tree produced by CSlangParser#typ.
    def enterTyp(self, ctx:CSlangParser.TypContext):
        pass

    # Exit a parse tree produced by CSlangParser#typ.
    def exitTyp(self, ctx:CSlangParser.TypContext):
        pass


    # Enter a parse tree produced by CSlangParser#array_type.
    def enterArray_type(self, ctx:CSlangParser.Array_typeContext):
        pass

    # Exit a parse tree produced by CSlangParser#array_type.
    def exitArray_type(self, ctx:CSlangParser.Array_typeContext):
        pass


    # Enter a parse tree produced by CSlangParser#literal.
    def enterLiteral(self, ctx:CSlangParser.LiteralContext):
        pass

    # Exit a parse tree produced by CSlangParser#literal.
    def exitLiteral(self, ctx:CSlangParser.LiteralContext):
        pass


    # Enter a parse tree produced by CSlangParser#bool_literal.
    def enterBool_literal(self, ctx:CSlangParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by CSlangParser#bool_literal.
    def exitBool_literal(self, ctx:CSlangParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by CSlangParser#array.
    def enterArray(self, ctx:CSlangParser.ArrayContext):
        pass

    # Exit a parse tree produced by CSlangParser#array.
    def exitArray(self, ctx:CSlangParser.ArrayContext):
        pass



del CSlangParser