# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,307,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,65,8,1,10,1,12,1,68,
        9,1,1,1,1,1,1,1,1,1,5,1,74,8,1,10,1,12,1,77,9,1,1,1,5,1,80,8,1,10,
        1,12,1,83,9,1,1,2,5,2,86,8,2,10,2,12,2,89,9,2,1,2,5,2,92,8,2,10,
        2,12,2,95,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,108,
        8,3,1,4,1,4,1,5,4,5,113,8,5,11,5,12,5,114,1,5,1,5,1,5,4,5,120,8,
        5,11,5,12,5,121,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,131,8,5,11,5,12,
        5,132,1,5,1,5,5,5,137,8,5,10,5,12,5,140,9,5,1,5,5,5,143,8,5,10,5,
        12,5,146,9,5,1,5,1,5,4,5,150,8,5,11,5,12,5,151,1,5,1,5,5,5,156,8,
        5,10,5,12,5,159,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,168,8,5,11,5,
        12,5,169,1,5,1,5,1,5,3,5,175,8,5,1,6,1,6,1,6,1,6,1,6,3,6,182,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        199,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,207,8,8,5,8,209,8,8,10,8,12,
        8,212,9,8,1,8,1,8,1,9,5,9,217,8,9,10,9,12,9,220,9,9,1,9,1,9,1,9,
        1,9,1,9,5,9,227,8,9,10,9,12,9,230,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,239,8,9,5,9,241,8,9,10,9,12,9,244,9,9,1,9,1,9,3,9,248,8,9,
        1,10,1,10,1,10,1,10,1,10,3,10,255,8,10,1,11,1,11,1,12,1,12,1,13,
        1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,270,8,16,1,17,1,17,
        5,17,274,8,17,10,17,12,17,277,9,17,1,18,1,18,1,19,1,19,1,20,1,20,
        5,20,285,8,20,10,20,12,20,288,9,20,1,21,1,21,1,22,1,22,5,22,294,
        8,22,10,22,12,22,297,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,0,8,1,0,9,12,1,0,25,28,1,0,29,32,1,0,33,34,1,0,35,
        36,1,0,37,38,1,0,44,45,1,0,39,40,326,0,51,1,0,0,0,2,59,1,0,0,0,4,
        87,1,0,0,0,6,107,1,0,0,0,8,109,1,0,0,0,10,174,1,0,0,0,12,181,1,0,
        0,0,14,198,1,0,0,0,16,200,1,0,0,0,18,247,1,0,0,0,20,254,1,0,0,0,
        22,256,1,0,0,0,24,258,1,0,0,0,26,260,1,0,0,0,28,262,1,0,0,0,30,264,
        1,0,0,0,32,269,1,0,0,0,34,271,1,0,0,0,36,278,1,0,0,0,38,280,1,0,
        0,0,40,282,1,0,0,0,42,289,1,0,0,0,44,291,1,0,0,0,46,300,1,0,0,0,
        48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,
        0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,1,0,0,55,56,5,46,0,0,56,
        57,3,4,2,0,57,58,5,0,0,1,58,1,1,0,0,0,59,60,5,2,0,0,60,61,3,34,17,
        0,61,62,5,3,0,0,62,66,3,8,4,0,63,65,3,34,17,0,64,63,1,0,0,0,65,68,
        1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,0,
        69,70,5,4,0,0,70,71,5,5,0,0,71,75,3,4,2,0,72,74,5,6,0,0,73,72,1,
        0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,81,1,0,0,0,77,
        75,1,0,0,0,78,80,3,14,7,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,
        0,0,81,82,1,0,0,0,82,3,1,0,0,0,83,81,1,0,0,0,84,86,3,6,3,0,85,84,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,93,1,0,0,0,
        89,87,1,0,0,0,90,92,3,10,5,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,
        0,0,0,93,94,1,0,0,0,94,5,1,0,0,0,95,93,1,0,0,0,96,97,3,8,4,0,97,
        98,3,34,17,0,98,99,5,46,0,0,99,108,1,0,0,0,100,101,5,7,0,0,101,102,
        3,40,20,0,102,103,5,8,0,0,103,104,3,34,17,0,104,105,1,0,0,0,105,
        106,5,46,0,0,106,108,1,0,0,0,107,96,1,0,0,0,107,100,1,0,0,0,108,
        7,1,0,0,0,109,110,7,0,0,0,110,9,1,0,0,0,111,113,3,18,9,0,112,111,
        1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,116,
        1,0,0,0,116,117,5,46,0,0,117,175,1,0,0,0,118,120,3,14,7,0,119,118,
        1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,123,
        1,0,0,0,123,124,5,46,0,0,124,175,1,0,0,0,125,126,5,13,0,0,126,127,
        3,14,7,0,127,128,5,5,0,0,128,130,5,46,0,0,129,131,3,14,7,0,130,129,
        1,0,0,0,131,132,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,134,
        1,0,0,0,134,157,5,46,0,0,135,137,5,14,0,0,136,135,1,0,0,0,137,140,
        1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,144,1,0,0,0,140,138,
        1,0,0,0,141,143,5,5,0,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,
        1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,149,
        5,46,0,0,148,150,3,14,7,0,149,148,1,0,0,0,150,151,1,0,0,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,5,46,0,0,154,156,
        1,0,0,0,155,138,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,
        1,0,0,0,158,175,1,0,0,0,159,157,1,0,0,0,160,161,5,15,0,0,161,162,
        3,14,7,0,162,163,5,16,0,0,163,164,3,14,7,0,164,165,5,5,0,0,165,167,
        5,46,0,0,166,168,3,14,7,0,167,166,1,0,0,0,168,169,1,0,0,0,169,167,
        1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,5,46,0,0,172,175,
        1,0,0,0,173,175,5,17,0,0,174,112,1,0,0,0,174,119,1,0,0,0,174,125,
        1,0,0,0,174,160,1,0,0,0,174,173,1,0,0,0,175,11,1,0,0,0,176,182,3,
        34,17,0,177,182,5,18,0,0,178,182,5,19,0,0,179,182,5,20,0,0,180,182,
        5,21,0,0,181,176,1,0,0,0,181,177,1,0,0,0,181,178,1,0,0,0,181,179,
        1,0,0,0,181,180,1,0,0,0,182,13,1,0,0,0,183,199,3,16,8,0,184,199,
        3,32,16,0,185,186,3,34,17,0,186,187,3,20,10,0,187,188,3,32,16,0,
        188,199,1,0,0,0,189,190,5,22,0,0,190,191,3,34,17,0,191,192,5,4,0,
        0,192,199,1,0,0,0,193,199,3,34,17,0,194,195,3,32,16,0,195,196,5,
        23,0,0,196,197,3,32,16,0,197,199,1,0,0,0,198,183,1,0,0,0,198,184,
        1,0,0,0,198,185,1,0,0,0,198,189,1,0,0,0,198,193,1,0,0,0,198,194,
        1,0,0,0,199,15,1,0,0,0,200,201,3,12,6,0,201,202,5,3,0,0,202,203,
        3,14,7,0,203,210,5,23,0,0,204,206,3,14,7,0,205,207,5,23,0,0,206,
        205,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,204,1,0,0,0,209,
        212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,213,1,0,0,0,212,
        210,1,0,0,0,213,214,5,4,0,0,214,17,1,0,0,0,215,217,3,8,4,0,216,215,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,
        1,0,0,0,220,218,1,0,0,0,221,222,3,34,17,0,222,223,3,30,15,0,223,
        224,3,32,16,0,224,248,1,0,0,0,225,227,3,8,4,0,226,225,1,0,0,0,227,
        230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,
        228,1,0,0,0,231,232,3,34,17,0,232,233,3,30,15,0,233,234,5,24,0,0,
        234,235,3,44,22,0,235,242,5,23,0,0,236,238,3,44,22,0,237,239,5,23,
        0,0,238,237,1,0,0,0,238,239,1,0,0,0,239,241,1,0,0,0,240,236,1,0,
        0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,245,1,0,
        0,0,244,242,1,0,0,0,245,246,5,8,0,0,246,248,1,0,0,0,247,218,1,0,
        0,0,247,228,1,0,0,0,248,19,1,0,0,0,249,255,3,22,11,0,250,255,3,24,
        12,0,251,255,3,26,13,0,252,255,3,28,14,0,253,255,3,30,15,0,254,249,
        1,0,0,0,254,250,1,0,0,0,254,251,1,0,0,0,254,252,1,0,0,0,254,253,
        1,0,0,0,255,21,1,0,0,0,256,257,7,1,0,0,257,23,1,0,0,0,258,259,7,
        2,0,0,259,25,1,0,0,0,260,261,7,3,0,0,261,27,1,0,0,0,262,263,7,4,
        0,0,263,29,1,0,0,0,264,265,7,5,0,0,265,31,1,0,0,0,266,270,3,38,19,
        0,267,270,3,42,21,0,268,270,3,44,22,0,269,266,1,0,0,0,269,267,1,
        0,0,0,269,268,1,0,0,0,270,33,1,0,0,0,271,275,5,44,0,0,272,274,3,
        36,18,0,273,272,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,
        1,0,0,0,276,35,1,0,0,0,277,275,1,0,0,0,278,279,7,6,0,0,279,37,1,
        0,0,0,280,281,3,40,20,0,281,39,1,0,0,0,282,286,5,45,0,0,283,285,
        5,45,0,0,284,283,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,
        1,0,0,0,287,41,1,0,0,0,288,286,1,0,0,0,289,290,7,7,0,0,290,43,1,
        0,0,0,291,295,5,41,0,0,292,294,5,44,0,0,293,292,1,0,0,0,294,297,
        1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,298,1,0,0,0,297,295,
        1,0,0,0,298,299,5,41,0,0,299,45,1,0,0,0,300,301,5,42,0,0,301,302,
        3,32,16,0,302,303,5,5,0,0,303,304,3,32,16,0,304,305,5,43,0,0,305,
        47,1,0,0,0,30,51,66,75,81,87,93,107,114,121,132,138,144,151,157,
        169,174,181,198,206,210,218,228,238,242,247,254,269,275,286,295
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'start'", "'def'", "'('", "')'", "':'", 
                     "'return'", "'string['", "']'", "'int'", "'string'", 
                     "'bool'", "'dict'", "'if'", "'else'", "'for'", "'in'", 
                     "'break'", "'CiteAPA'", "'CiteMLA'", "'CiteCMS'", "'CiteCSE'", 
                     "'print('", "','", "'['", "'+'", "'-'", "'*'", "'/'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'and'", 
                     "'or'", "'='", "'+='", "'True'", "'False'", "'\"'", 
                     "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CHAR", "DIGIT", "NEWLINE", "SPACE" ]

    RULE_program = 0
    RULE_method_decl = 1
    RULE_block = 2
    RULE_var_decl = 3
    RULE_type = 4
    RULE_statement = 5
    RULE_method_name = 6
    RULE_expr = 7
    RULE_method_call = 8
    RULE_var_assign = 9
    RULE_operation = 10
    RULE_arithm_op = 11
    RULE_rel_op = 12
    RULE_eq_op = 13
    RULE_cond_op = 14
    RULE_assign_op = 15
    RULE_literal = 16
    RULE_id = 17
    RULE_char_num = 18
    RULE_int_literal = 19
    RULE_decimal_literal = 20
    RULE_bool_literal = 21
    RULE_string_literal = 22
    RULE_dict = 23

    ruleNames =  [ "program", "method_decl", "block", "var_decl", "type", 
                   "statement", "method_name", "expr", "method_call", "var_assign", 
                   "operation", "arithm_op", "rel_op", "eq_op", "cond_op", 
                   "assign_op", "literal", "id", "char_num", "int_literal", 
                   "decimal_literal", "bool_literal", "string_literal", 
                   "dict" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    CHAR=44
    DIGIT=45
    NEWLINE=46
    SPACE=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def method_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Method_declContext)
            else:
                return self.getTypedRuleContext(ExprParser.Method_declContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 48
                self.method_decl()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(ExprParser.T__0)
            self.state = 55
            self.match(ExprParser.NEWLINE)
            self.state = 56
            self.block()
            self.state = 57
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.IdContext)
            else:
                return self.getTypedRuleContext(ExprParser.IdContext,i)


        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_method_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_decl" ):
                listener.enterMethod_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_decl" ):
                listener.exitMethod_decl(self)




    def method_decl(self):

        localctx = ExprParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ExprParser.T__1)
            self.state = 60
            self.id_()
            self.state = 61
            self.match(ExprParser.T__2)
            self.state = 62
            self.type_()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 63
                self.id_()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(ExprParser.T__3)
            self.state = 70
            self.match(ExprParser.T__4)
            self.state = 71
            self.block()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 72
                self.match(ExprParser.T__5)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56624856956928) != 0):
                self.state = 78
                self.expr()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Var_declContext)
            else:
                return self.getTypedRuleContext(ExprParser.Var_declContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self.var_decl() 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 90
                    self.statement() 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def decimal_literal(self):
            return self.getTypedRuleContext(ExprParser.Decimal_literalContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = ExprParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.type_()
                self.state = 97
                self.id_()
                self.state = 98
                self.match(ExprParser.NEWLINE)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(ExprParser.T__6)
                self.state = 101
                self.decimal_literal()
                self.state = 102
                self.match(ExprParser.T__7)
                self.state = 103
                self.id_()
                self.state = 105
                self.match(ExprParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def var_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Var_assignContext)
            else:
                return self.getTypedRuleContext(ExprParser.Var_assignContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 111
                    self.var_assign()
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17592186052096) != 0)):
                        break

                self.state = 116
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 118
                    self.expr()
                    self.state = 121 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56624856956928) != 0)):
                        break

                self.state = 123
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(ExprParser.T__12)
                self.state = 126
                self.expr()
                self.state = 127
                self.match(ExprParser.T__4)
                self.state = 128
                self.match(ExprParser.NEWLINE)
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 129
                    self.expr()
                    self.state = 132 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56624856956928) != 0)):
                        break

                self.state = 134
                self.match(ExprParser.NEWLINE)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744194080) != 0):
                    self.state = 138
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==14:
                        self.state = 135
                        self.match(ExprParser.T__13)
                        self.state = 140
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 144
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 141
                        self.match(ExprParser.T__4)
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 147
                    self.match(ExprParser.NEWLINE)
                    self.state = 149 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 148
                        self.expr()
                        self.state = 151 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56624856956928) != 0)):
                            break

                    self.state = 153
                    self.match(ExprParser.NEWLINE)
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.match(ExprParser.T__14)
                self.state = 161
                self.expr()
                self.state = 162
                self.match(ExprParser.T__15)
                self.state = 163
                self.expr()
                self.state = 164
                self.match(ExprParser.T__4)
                self.state = 165
                self.match(ExprParser.NEWLINE)
                self.state = 167 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 166
                    self.expr()
                    self.state = 169 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56624856956928) != 0)):
                        break

                self.state = 171
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.match(ExprParser.T__16)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_method_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_name" ):
                listener.enterMethod_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_name" ):
                listener.exitMethod_name(self)




    def method_name(self):

        localctx = ExprParser.Method_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_name)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.id_()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(ExprParser.T__17)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(ExprParser.T__18)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.match(ExprParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.match(ExprParser.T__20)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_call(self):
            return self.getTypedRuleContext(ExprParser.Method_callContext,0)


        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ExprParser.LiteralContext,i)


        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def operation(self):
            return self.getTypedRuleContext(ExprParser.OperationContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.id_()
                self.state = 186
                self.operation()
                self.state = 187
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(ExprParser.T__21)
                self.state = 190
                self.id_()
                self.state = 191
                self.match(ExprParser.T__3)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 193
                self.id_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 194
                self.literal()
                self.state = 195
                self.match(ExprParser.T__22)
                self.state = 196
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_name(self):
            return self.getTypedRuleContext(ExprParser.Method_nameContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_method_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call" ):
                listener.enterMethod_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call" ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = ExprParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.method_name()
            self.state = 201
            self.match(ExprParser.T__2)
            self.state = 202
            self.expr()
            self.state = 203
            self.match(ExprParser.T__22)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56624856956928) != 0):
                self.state = 204
                self.expr()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 205
                    self.match(ExprParser.T__22)


                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(ExprParser.Assign_opContext,0)


        def literal(self):
            return self.getTypedRuleContext(ExprParser.LiteralContext,0)


        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TypeContext)
            else:
                return self.getTypedRuleContext(ExprParser.TypeContext,i)


        def string_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.String_literalContext)
            else:
                return self.getTypedRuleContext(ExprParser.String_literalContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)




    def var_assign(self):

        localctx = ExprParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_assign)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                    self.state = 215
                    self.type_()
                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 221
                self.id_()
                self.state = 222
                self.assign_op()
                self.state = 223
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                    self.state = 225
                    self.type_()
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 231
                self.id_()
                self.state = 232
                self.assign_op()
                self.state = 233
                self.match(ExprParser.T__23)
                self.state = 234
                self.string_literal()
                self.state = 235
                self.match(ExprParser.T__22)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 236
                    self.string_literal()
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 237
                        self.match(ExprParser.T__22)


                    self.state = 244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 245
                self.match(ExprParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithm_op(self):
            return self.getTypedRuleContext(ExprParser.Arithm_opContext,0)


        def rel_op(self):
            return self.getTypedRuleContext(ExprParser.Rel_opContext,0)


        def eq_op(self):
            return self.getTypedRuleContext(ExprParser.Eq_opContext,0)


        def cond_op(self):
            return self.getTypedRuleContext(ExprParser.Cond_opContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(ExprParser.Assign_opContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = ExprParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operation)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.arithm_op()
                pass
            elif token in [29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.rel_op()
                pass
            elif token in [33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.eq_op()
                pass
            elif token in [35, 36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.cond_op()
                pass
            elif token in [37, 38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.assign_op()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithm_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_arithm_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithm_op" ):
                listener.enterArithm_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithm_op" ):
                listener.exitArithm_op(self)




    def arithm_op(self):

        localctx = ExprParser.Arithm_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arithm_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_rel_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_op" ):
                listener.enterRel_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_op" ):
                listener.exitRel_op(self)




    def rel_op(self):

        localctx = ExprParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eq_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_eq_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq_op" ):
                listener.enterEq_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq_op" ):
                listener.exitEq_op(self)




    def eq_op(self):

        localctx = ExprParser.Eq_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eq_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_cond_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_op" ):
                listener.enterCond_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_op" ):
                listener.exitCond_op(self)




    def cond_op(self):

        localctx = ExprParser.Cond_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cond_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_assign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_op" ):
                listener.enterAssign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_op" ):
                listener.exitAssign_op(self)




    def assign_op(self):

        localctx = ExprParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==37 or _la==38):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_literal(self):
            return self.getTypedRuleContext(ExprParser.Int_literalContext,0)


        def bool_literal(self):
            return self.getTypedRuleContext(ExprParser.Bool_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(ExprParser.String_literalContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ExprParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.int_literal()
                pass
            elif token in [39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.bool_literal()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.string_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def char_num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Char_numContext)
            else:
                return self.getTypedRuleContext(ExprParser.Char_numContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = ExprParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(ExprParser.CHAR)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.char_num() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Char_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def DIGIT(self):
            return self.getToken(ExprParser.DIGIT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_char_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_num" ):
                listener.enterChar_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_num" ):
                listener.exitChar_num(self)




    def char_num(self):

        localctx = ExprParser.Char_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_char_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not(_la==44 or _la==45):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decimal_literal(self):
            return self.getTypedRuleContext(ExprParser.Decimal_literalContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_int_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_literal" ):
                listener.enterInt_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_literal" ):
                listener.exitInt_literal(self)




    def int_literal(self):

        localctx = ExprParser.Int_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_int_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.decimal_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decimal_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DIGIT)
            else:
                return self.getToken(ExprParser.DIGIT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_decimal_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimal_literal" ):
                listener.enterDecimal_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimal_literal" ):
                listener.exitDecimal_literal(self)




    def decimal_literal(self):

        localctx = ExprParser.Decimal_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_decimal_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ExprParser.DIGIT)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 283
                    self.match(ExprParser.DIGIT) 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_bool_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_literal" ):
                listener.enterBool_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_literal" ):
                listener.exitBool_literal(self)




    def bool_literal(self):

        localctx = ExprParser.Bool_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            _la = self._input.LA(1)
            if not(_la==39 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHAR)
            else:
                return self.getToken(ExprParser.CHAR, i)

        def getRuleIndex(self):
            return ExprParser.RULE_string_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literal" ):
                listener.enterString_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literal" ):
                listener.exitString_literal(self)




    def string_literal(self):

        localctx = ExprParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_string_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ExprParser.T__40)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 292
                self.match(ExprParser.CHAR)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self.match(ExprParser.T__40)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ExprParser.LiteralContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDict" ):
                listener.enterDict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDict" ):
                listener.exitDict(self)




    def dict_(self):

        localctx = ExprParser.DictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dict)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ExprParser.T__41)
            self.state = 301
            self.literal()
            self.state = 302
            self.match(ExprParser.T__4)
            self.state = 303
            self.literal()
            self.state = 304
            self.match(ExprParser.T__42)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





