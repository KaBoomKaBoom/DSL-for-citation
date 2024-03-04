# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#method_decl.
    def enterMethod_decl(self, ctx:ExprParser.Method_declContext):
        pass

    # Exit a parse tree produced by ExprParser#method_decl.
    def exitMethod_decl(self, ctx:ExprParser.Method_declContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#var_decl.
    def enterVar_decl(self, ctx:ExprParser.Var_declContext):
        pass

    # Exit a parse tree produced by ExprParser#var_decl.
    def exitVar_decl(self, ctx:ExprParser.Var_declContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#method_name.
    def enterMethod_name(self, ctx:ExprParser.Method_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#method_name.
    def exitMethod_name(self, ctx:ExprParser.Method_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#method_call.
    def enterMethod_call(self, ctx:ExprParser.Method_callContext):
        pass

    # Exit a parse tree produced by ExprParser#method_call.
    def exitMethod_call(self, ctx:ExprParser.Method_callContext):
        pass


    # Enter a parse tree produced by ExprParser#var_assign.
    def enterVar_assign(self, ctx:ExprParser.Var_assignContext):
        pass

    # Exit a parse tree produced by ExprParser#var_assign.
    def exitVar_assign(self, ctx:ExprParser.Var_assignContext):
        pass


    # Enter a parse tree produced by ExprParser#operation.
    def enterOperation(self, ctx:ExprParser.OperationContext):
        pass

    # Exit a parse tree produced by ExprParser#operation.
    def exitOperation(self, ctx:ExprParser.OperationContext):
        pass


    # Enter a parse tree produced by ExprParser#arithm_op.
    def enterArithm_op(self, ctx:ExprParser.Arithm_opContext):
        pass

    # Exit a parse tree produced by ExprParser#arithm_op.
    def exitArithm_op(self, ctx:ExprParser.Arithm_opContext):
        pass


    # Enter a parse tree produced by ExprParser#rel_op.
    def enterRel_op(self, ctx:ExprParser.Rel_opContext):
        pass

    # Exit a parse tree produced by ExprParser#rel_op.
    def exitRel_op(self, ctx:ExprParser.Rel_opContext):
        pass


    # Enter a parse tree produced by ExprParser#eq_op.
    def enterEq_op(self, ctx:ExprParser.Eq_opContext):
        pass

    # Exit a parse tree produced by ExprParser#eq_op.
    def exitEq_op(self, ctx:ExprParser.Eq_opContext):
        pass


    # Enter a parse tree produced by ExprParser#cond_op.
    def enterCond_op(self, ctx:ExprParser.Cond_opContext):
        pass

    # Exit a parse tree produced by ExprParser#cond_op.
    def exitCond_op(self, ctx:ExprParser.Cond_opContext):
        pass


    # Enter a parse tree produced by ExprParser#assign_op.
    def enterAssign_op(self, ctx:ExprParser.Assign_opContext):
        pass

    # Exit a parse tree produced by ExprParser#assign_op.
    def exitAssign_op(self, ctx:ExprParser.Assign_opContext):
        pass


    # Enter a parse tree produced by ExprParser#literal.
    def enterLiteral(self, ctx:ExprParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#literal.
    def exitLiteral(self, ctx:ExprParser.LiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#char_num.
    def enterChar_num(self, ctx:ExprParser.Char_numContext):
        pass

    # Exit a parse tree produced by ExprParser#char_num.
    def exitChar_num(self, ctx:ExprParser.Char_numContext):
        pass


    # Enter a parse tree produced by ExprParser#int_literal.
    def enterInt_literal(self, ctx:ExprParser.Int_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#int_literal.
    def exitInt_literal(self, ctx:ExprParser.Int_literalContext):
        pass


    # Enter a parse tree produced by ExprParser#decimal_literal.
    def enterDecimal_literal(self, ctx:ExprParser.Decimal_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#decimal_literal.
    def exitDecimal_literal(self, ctx:ExprParser.Decimal_literalContext):
        pass


    # Enter a parse tree produced by ExprParser#bool_literal.
    def enterBool_literal(self, ctx:ExprParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#bool_literal.
    def exitBool_literal(self, ctx:ExprParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by ExprParser#string_literal.
    def enterString_literal(self, ctx:ExprParser.String_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#string_literal.
    def exitString_literal(self, ctx:ExprParser.String_literalContext):
        pass


    # Enter a parse tree produced by ExprParser#dict.
    def enterDict(self, ctx:ExprParser.DictContext):
        pass

    # Exit a parse tree produced by ExprParser#dict.
    def exitDict(self, ctx:ExprParser.DictContext):
        pass



del ExprParser