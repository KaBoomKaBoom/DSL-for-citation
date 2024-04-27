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
        # if "for" in queue:
        #     #print(self.var_value)
        #     if any(el in queue[queue.index("in")+5] for el in ['CiteAPA' , 'CiteMLA' , 'CiteCMS' , 'CiteCSE' , 'CiteISO' , 'CiteIEEE'] ):
        #         for q in self.var_value:
        #             self.enterExpr(ctx.expr())
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
        method_name = ctx.method_name().getText()
        method_args = [arg.getText() for arg in ctx.id_()]
        for arg in ctx.literal():
            method_args.append(arg.getText().replace('"', ''))
        if method_name == "CiteAPA":
            cite_text,cite_bib = generate_apa_citation(*method_args)
            # print(f"Citation: {cite_text}")
            # print(f"Bibliography: {cite_bib}")
            return cite_text, cite_bib
        elif method_name == "CiteMLA":
            cite_text,cite_bib = generate_mla_citation(*method_args)
            print(f"Citation: {cite_text}")
            print(f"Bibliography: {cite_bib}")
            return cite_text, cite_bib
        elif method_name == "CiteCMS":
            cite_text,cite_bib = generate_cms_citation(*method_args)
            print(f"Citation: {cite_text}")
            print(f"Bibliography: {cite_bib}")
            return cite_text, cite_bib
        elif method_name == "CiteCSE":
            cite_text,cite_bib = generate_cse_citation(*method_args)
            print(f"Citation: {cite_text}")
            print(f"Bibliography: {cite_bib}")
            return cite_text, cite_bib


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

def generate_apa_citation(qouote, source_type, author, year, title, book_title, publisher):
    #print(qouote, source_type, author, year, title, book_title, publisher)
    doc = Document("test.docx")
        # For in-text citation
    citation_text = qouote + "(" + author + ", " + str(year) + ")"
    p = doc.add_paragraph(citation_text)
    p.style.font.name = 'Times New Roman'
    p.style.font.size = Pt(12)
        # For bibliography/reference list
    citation_bib = author + " (" + str(year) + "). " + title + ". "
    p = doc.add_paragraph(citation_bib)

    if source_type == "book":
        citation_bib += book_title  + ' ' + publisher + "."
        p.add_run(book_title + ' ')
        p.add_run(publisher + ".").italic = True   
    elif source_type == "journal":
        citation_bib += book_title  + ' ' + publisher + "."
        p.add_run(book_title + ' ')
        p.add_run(publisher + ".").italic = True 
    elif source_type == "website":
        citation_bib += book_title  + ' ' + publisher + "."
    doc.save('test.docx')
    return citation_text, citation_bib

def generate_mla_citation(qouote, source_type, author, year, title, book_title, publisher):
    #print(qouote, source_type, author, year, title, book_title, publisher)
    doc = Document("test.docx")
        # For in-text citation
    citation_text = qouote + " (" + author + ")."
    p = doc.add_paragraph(citation_text)
    p.style.font.name = 'Times New Roman'
    p.style.font.size = Pt(12)
        # For bibliography/reference list
    citation_bib = author + '"' + title + '."'
    p = doc.add_paragraph(citation_bib)

    if source_type == "book":
        citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
        p.add_run(book_title + ', ').italic = True
        p.add_run(publisher + ", ")
        p.add_run(str(year) + ".") 
    elif source_type == "journal":
        citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
        p.add_run(book_title + ', ').italic = True
        p.add_run(publisher + ", ")
        p.add_run(str(year) + ".")
         
    elif source_type == "website":
        citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
        p.add_run(book_title + ', ').italic = True
        p.add_run(publisher + ", ")
        p.add_run(str(year) + ".")
    doc.save('test.docx')
    return citation_text, citation_bib

def generate_cms_citation(qouote, source_type, author, year, title='', book_title='', publisher='', link=''):
    #print(qouote, source_type, author, year, title, book_title, publisher)
    doc = Document("test.docx")
        # For in-text citation
    citation_text = qouote + " (" + author + " " + str(year) + ")."
    p = doc.add_paragraph(citation_text)
    p.style.font.name = 'Times New Roman'
    p.style.font.size = Pt(12)
        # For bibliography/reference list
    citation_bib = author + ". "

    if source_type == "book":
        citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
        p = doc.add_paragraph(citation_bib)
        p.add_run(book_title + '. ').italic = True
        p.add_run(publisher + ", ")
        p.add_run(str(year) + ".") 
    elif source_type == "journal":
        citation_bib += '"' + book_title  + '," ' + publisher + ', ' + str(year) +  "."
        p.add_run('"' + book_title + '," ')
        p.add_run(publisher + ", ")
        p.add_run(str(year) + ".")
         
    elif source_type == "website":
        date = datetime.datetime.now()
        citation_bib += title  + ', ' + publisher + ', ' + 'accessed ' + date.strftime("%d %b %Y") + ", " +  link + "."
        p.add_run(title + ', ')
        p.add_run(publisher + ", ")
        p.add_run( 'accessed ' + date.strftime("%d %b %Y") + ", ")
        p.add_run(link + ".")
    doc.save('test.docx')
    return citation_text, citation_bib

def generate_cse_citation(qouote, source_type, author, year,  book_title='', title='', publisher='', link='', index = 1):
    #print(qouote, source_type, author, year, title, book_title, publisher)
    doc = Document("test.docx")
        # For in-text citation superscript the number of the citation
    citation_text = qouote + ' ' + str(index) + "."
    p = doc.add_paragraph(qouote )
    index_run = p.add_run(str(index))
    index_run.superscript = True
    p.add_run('.')
    p.style.font.name = 'Times New Roman'
    p.style.font.size = Pt(12)
        # For bibliography/reference list
    citation_bib = author  

    if source_type == "book":
        citation_bib += book_title  + ', ' + publisher + ', ' + str(year) +  "."
        p = doc.add_paragraph(citation_bib)
        p.add_run(book_title + '. ')
        p.add_run(publisher + "; ")
        p.add_run(str(year) + ".") 
    elif source_type == "journal":
        citation_bib += '"' + book_title  + '," ' + publisher + ', ' + str(year) +  "."
        p.add_run(book_title + '. ')
        p.add_run(publisher + ", ")
        p.add_run(str(year) + ".")
         
    elif source_type == "website":
        date = datetime.datetime.now()
        citation_bib += title  + ', ' + publisher + str(year) +', ' + '[accessed ' + date.strftime("%d %b %Y") + "]; " +  link + "."
        p = doc.add_paragraph(author)
        p.add_run(title + '. ')
        p.add_run(publisher + ". " + str(year))
        p.add_run( '[accessed ' + date.strftime("%d %b %Y") + "]; ")
        p.add_run(link + ".")
    doc.save('test.docx')
    return citation_text, citation_bib

del ExprParser