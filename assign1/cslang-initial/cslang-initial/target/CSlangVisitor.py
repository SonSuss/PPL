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


    # Visit a parse tree produced by CSlangParser#gb.
    def visitGb(self, ctx:CSlangParser.GbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_lst.
    def visitClass_lst(self, ctx:CSlangParser.Class_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_dcl.
    def visitClass_dcl(self, ctx:CSlangParser.Class_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_body.
    def visitClass_body(self, ctx:CSlangParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#menthod_lst.
    def visitMenthod_lst(self, ctx:CSlangParser.Menthod_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#menthod_dcl.
    def visitMenthod_dcl(self, ctx:CSlangParser.Menthod_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_decl.
    def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#menthod_body.
    def visitMenthod_body(self, ctx:CSlangParser.Menthod_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param_lst.
    def visitParam_lst(self, ctx:CSlangParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
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


    # Visit a parse tree produced by CSlangParser#statement_lst.
    def visitStatement_lst(self, ctx:CSlangParser.Statement_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statements.
    def visitStatements(self, ctx:CSlangParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decl_state.
    def visitDecl_state(self, ctx:CSlangParser.Decl_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign.
    def visitAssign(self, ctx:CSlangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_form.
    def visitAssign_form(self, ctx:CSlangParser.Assign_formContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decl_typ.
    def visitDecl_typ(self, ctx:CSlangParser.Decl_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decl_array.
    def visitDecl_array(self, ctx:CSlangParser.Decl_arrayContext):
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


    # Visit a parse tree produced by CSlangParser#block_state.
    def visitBlock_state(self, ctx:CSlangParser.Block_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_block.
    def visitIf_block(self, ctx:CSlangParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#menthod_invo_state.
    def visitMenthod_invo_state(self, ctx:CSlangParser.Menthod_invo_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#access_lst.
    def visitAccess_lst(self, ctx:CSlangParser.Access_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#access.
    def visitAccess(self, ctx:CSlangParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_access.
    def visitStatic_access(self, ctx:CSlangParser.Static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instance_access.
    def visitInstance_access(self, ctx:CSlangParser.Instance_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instance_menthod_invo_access.
    def visitInstance_menthod_invo_access(self, ctx:CSlangParser.Instance_menthod_invo_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_menthod_invo_access.
    def visitStatic_menthod_invo_access(self, ctx:CSlangParser.Static_menthod_invo_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#idlist.
    def visitIdlist(self, ctx:CSlangParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#index_op.
    def visitIndex_op(self, ctx:CSlangParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#identifier.
    def visitIdentifier(self, ctx:CSlangParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#io_st.
    def visitIo_st(self, ctx:CSlangParser.Io_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#io.
    def visitIo(self, ctx:CSlangParser.IoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#fm.
    def visitFm(self, ctx:CSlangParser.FmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#boolean.
    def visitBoolean(self, ctx:CSlangParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typ.
    def visitTyp(self, ctx:CSlangParser.TypContext):
        return self.visitChildren(ctx)



del CSlangParser