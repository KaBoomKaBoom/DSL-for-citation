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


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#var_decl.
    def enterVar_decl(self, ctx:ExprParser.Var_declContext):
        print("Entering variable declaration")
        var_type = ctx.type_().getText()
        var_name = ctx.id_().getText()
        print(f"Type: {var_type}, Name: {var_name}")

    # Exit a parse tree produced by ExprParser#var_decl.
    def exitVar_decl(self, ctx:ExprParser.Var_declContext):
        print("Exiting variable declaration")


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
        print("Entering variable assignment")
        var_name = ctx.id_().getText()
        var_value = [string.getText() for string in ctx.string_literal()]
        print(f"Variable: {var_name}, Value: {var_value}")

    # Exit a parse tree produced by ExprParser#var_assign.
    def exitVar_assign(self, ctx:ExprParser.Var_assignContext):
        print("Exiting variable assignment")


    # Enter a parse tree produced by ExprParser#math_expr.
    def enterMath_expr(self, ctx:ExprParser.Math_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#math_expr.
    def exitMath_expr(self, ctx:ExprParser.Math_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#math_symbol.
    def enterMath_symbol(self, ctx:ExprParser.Math_symbolContext):
        pass

    # Exit a parse tree produced by ExprParser#math_symbol.
    def exitMath_symbol(self, ctx:ExprParser.Math_symbolContext):
        pass


    # Enter a parse tree produced by ExprParser#operation.
    def enterOperation(self, ctx:ExprParser.OperationContext):
        pass

    # Exit a parse tree produced by ExprParser#operation.
    def exitOperation(self, ctx:ExprParser.OperationContext):
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


    # Enter a parse tree produced by ExprParser#string_literal.
    def enterString_literal(self, ctx:ExprParser.String_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#string_literal.
    def exitString_literal(self, ctx:ExprParser.String_literalContext):
        pass



del ExprParser