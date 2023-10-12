# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
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


    # Visit a parse tree produced by CSlangParser#relational_expr0.
    def visitRelational_expr0(self, ctx:CSlangParser.Relational_expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#relational_expr.
    def visitRelational_expr(self, ctx:CSlangParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr_lst.
    def visitExpr_lst(self, ctx:CSlangParser.Expr_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statements.
    def visitStatements(self, ctx:CSlangParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_decl.
    def visitAssign_decl(self, ctx:CSlangParser.Assign_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_assign.
    def visitAttribute_assign(self, ctx:CSlangParser.Attribute_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_decl.
    def visitAttribute_decl(self, ctx:CSlangParser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#variable_decl.
    def visitVariable_decl(self, ctx:CSlangParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constraint_decl.
    def visitConstraint_decl(self, ctx:CSlangParser.Constraint_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#non_inital_decl.
    def visitNon_inital_decl(self, ctx:CSlangParser.Non_inital_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#inital_decl.
    def visitInital_decl(self, ctx:CSlangParser.Inital_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_state.
    def visitIf_state(self, ctx:CSlangParser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_state.
    def visitFor_state(self, ctx:CSlangParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_state.
    def visitBreak_state(self, ctx:CSlangParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_state.
    def visitContinue_state(self, ctx:CSlangParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_state.
    def visitReturn_state(self, ctx:CSlangParser.Return_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#call_state.
    def visitCall_state(self, ctx:CSlangParser.Call_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instance_method_invo_access.
    def visitInstance_method_invo_access(self, ctx:CSlangParser.Instance_method_invo_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_method_invo_access.
    def visitStatic_method_invo_access(self, ctx:CSlangParser.Static_method_invo_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_state.
    def visitBlock_state(self, ctx:CSlangParser.Block_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#index_op.
    def visitIndex_op(self, ctx:CSlangParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#id_lst.
    def visitId_lst(self, ctx:CSlangParser.Id_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#id_access.
    def visitId_access(self, ctx:CSlangParser.Id_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#io_st.
    def visitIo_st(self, ctx:CSlangParser.Io_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#io_mt.
    def visitIo_mt(self, ctx:CSlangParser.Io_mtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typ.
    def visitTyp(self, ctx:CSlangParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attri_type.
    def visitAttri_type(self, ctx:CSlangParser.Attri_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#bool_literal.
    def visitBool_literal(self, ctx:CSlangParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array.
    def visitArray(self, ctx:CSlangParser.ArrayContext):
        return self.visitChildren(ctx)



del CSlangParser