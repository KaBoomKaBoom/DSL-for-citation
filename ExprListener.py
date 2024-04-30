#id, source_type, author, title, place, publisher, year    
# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser
    
from docx import Document
from docx.shared import Pt
import datetime
import re
import Standards as st
# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):
    
    def __init__(self):
        self.var_value = None
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
        # print("Entering statement")
        queue=[child.getText() for child in ctx.children]
        # print(queue)
        if ctx.var_assign():
            for var_assign_ctx in ctx.var_assign():
                self.var_value = self.enterVar_assign(var_assign_ctx)
            #print(f"Variable: {self.var_value}")
        elif ctx.for_expr():
            print("Enter for")  
          
    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass

    def enterFor_expr(self, ctx:ExprParser.For_exprContext):
        qu = [child.getText() for child in ctx.children]
        print(qu)
        for qu[2] in self.var_value:
            #print(qu[2])
            pass
        
        # Define a regular expression pattern to match the method name and arguments
        pattern = r'(\w+)\((.*?)\)'

        # Use re.findall to find all matches of the pattern in the string
        matches = re.findall(pattern, qu[9])

        if matches:
            method_name = matches[0][0]  # Extract method name from the first match
            method_args = matches[0][1].split(",")  # Extract arguments and split them into a list

            # Trim any whitespace from arguments
            method_args = [arg.strip() for arg in method_args]
            method_args = [arg.replace('"', '') for arg in method_args]
            print("Method Name:", method_name)
            print("Arguments:", method_args)
            
        if method_name == "CiteAPA":
            for el in self.var_value:
                method_args[0] = el
                cite_text,cite_bib = st.Standards.generate_apa_citation(*method_args)
                print(f"Citation: {cite_text}")
                print(f"Bibliography: {cite_bib}")
                print('----------------------------')
        elif method_name == "CiteMLA":
            for el in self.var_value:
                method_args[0] = el
                cite_text,cite_bib = st.Standards.generate_mla_citation(*method_args)
                print(f"Citation: {cite_text}")
                print(f"Bibliography: {cite_bib}")
                print('----------------------------')
        elif method_name == "CiteCMS":
            for el in self.var_value:
                method_args[0] = el
                cite_text,cite_bib = st.Standardsgenerate_cms_citation(*method_args)
                print(f"Citation: {cite_text}")
                print(f"Bibliography: {cite_bib}")
                print('----------------------------')
        elif method_name == "CiteCSE":
            index = 1
            for el in self.var_value:
                method_args[0] = el
                cite_text,cite_bib = st.Standards.generate_cse_citation(*method_args, index)
                print(f"Citation: {cite_text}")
                print(f"Bibliography: {cite_bib}")
                print('----------------------------')
                index+=1
        elif method_name == "CiteISO":
            index = 1
            for el in self.var_value:
                method_args[0] = el
                cite_text,cite_bib = st.Standards.cite_iso(*method_args, index)
                print(f"Citation: {cite_text}")
                print(f"Bibliography: {cite_bib}")
                print('----------------------------')
                index+=1
        elif method_name == "CiteIEEE":
            index = 1
            for el in self.var_value:
                method_args[0] = el
                cite_text,cite_bib = st.Standards.cite_ieee(*method_args, index)
                print(f"Citation: {cite_text}")
                print(f"Bibliography: {cite_bib}")
                print('----------------------------')
                index+=1


    def exitFor_expr(self, ctx:ExprParser.For_exprContext):
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
        q = [child.getText() for child in ctx.children]
        method_name = q[0]
        method_args = [arg.getText() for arg in ctx.id_()]
        for arg in ctx.literal():
            method_args.append(arg.getText().replace('"', ''))

    # Exit a parse tree produced by ExprParser#method_call.
    def exitMethod_call(self, ctx:ExprParser.Method_callContext):
        #print("Exiting method call")
        pass

    # Enter a parse tree produced by ExprParser#var_assign.
    def enterVar_assign(self, ctx:ExprParser.Var_assignContext):
        #print("Entering variable assignment")
        #var_name = ctx.id_().getText()
        var_value = [string.getText() for string in ctx.string_literal()]
        var_value = [el.replace('"', '') for el in var_value]  
        #print(f"Variable: {var_name}, Value: {var_value}")
        return var_value

    # Exit a parse tree produced by ExprParser#var_assign.
    def exitVar_assign(self, ctx:ExprParser.Var_assignContext):
        #print("Exiting variable assignment")
        pass

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