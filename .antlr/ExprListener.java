// Generated from c:/Users/Andrei/Desktop/DSL-for-citation/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ExprParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ExprParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ExprParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ExprParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl(ExprParser.Var_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl(ExprParser.Var_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(ExprParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(ExprParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ExprParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ExprParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#for_expr}.
	 * @param ctx the parse tree
	 */
	void enterFor_expr(ExprParser.For_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#for_expr}.
	 * @param ctx the parse tree
	 */
	void exitFor_expr(ExprParser.For_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#method_name}.
	 * @param ctx the parse tree
	 */
	void enterMethod_name(ExprParser.Method_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#method_name}.
	 * @param ctx the parse tree
	 */
	void exitMethod_name(ExprParser.Method_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ExprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ExprParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#method_call}.
	 * @param ctx the parse tree
	 */
	void enterMethod_call(ExprParser.Method_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#method_call}.
	 * @param ctx the parse tree
	 */
	void exitMethod_call(ExprParser.Method_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#var_assign}.
	 * @param ctx the parse tree
	 */
	void enterVar_assign(ExprParser.Var_assignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#var_assign}.
	 * @param ctx the parse tree
	 */
	void exitVar_assign(ExprParser.Var_assignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#math_expr}.
	 * @param ctx the parse tree
	 */
	void enterMath_expr(ExprParser.Math_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#math_expr}.
	 * @param ctx the parse tree
	 */
	void exitMath_expr(ExprParser.Math_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#math_symbol}.
	 * @param ctx the parse tree
	 */
	void enterMath_symbol(ExprParser.Math_symbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#math_symbol}.
	 * @param ctx the parse tree
	 */
	void exitMath_symbol(ExprParser.Math_symbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterOperation(ExprParser.OperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitOperation(ExprParser.OperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#assign_op}.
	 * @param ctx the parse tree
	 */
	void enterAssign_op(ExprParser.Assign_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#assign_op}.
	 * @param ctx the parse tree
	 */
	void exitAssign_op(ExprParser.Assign_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(ExprParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(ExprParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#id}.
	 * @param ctx the parse tree
	 */
	void enterId(ExprParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#id}.
	 * @param ctx the parse tree
	 */
	void exitId(ExprParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#char_num}.
	 * @param ctx the parse tree
	 */
	void enterChar_num(ExprParser.Char_numContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#char_num}.
	 * @param ctx the parse tree
	 */
	void exitChar_num(ExprParser.Char_numContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#int_literal}.
	 * @param ctx the parse tree
	 */
	void enterInt_literal(ExprParser.Int_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#int_literal}.
	 * @param ctx the parse tree
	 */
	void exitInt_literal(ExprParser.Int_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#decimal_literal}.
	 * @param ctx the parse tree
	 */
	void enterDecimal_literal(ExprParser.Decimal_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#decimal_literal}.
	 * @param ctx the parse tree
	 */
	void exitDecimal_literal(ExprParser.Decimal_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#string_literal}.
	 * @param ctx the parse tree
	 */
	void enterString_literal(ExprParser.String_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#string_literal}.
	 * @param ctx the parse tree
	 */
	void exitString_literal(ExprParser.String_literalContext ctx);
}