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
        4,1,45,260,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,
        1,1,1,1,1,1,1,5,1,72,8,1,10,1,12,1,75,9,1,1,1,5,1,78,8,1,10,1,12,
        1,81,9,1,1,2,5,2,84,8,2,10,2,12,2,87,9,2,1,2,5,2,90,8,2,10,2,12,
        2,93,9,2,1,2,5,2,96,8,2,10,2,12,2,99,9,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,109,8,3,1,4,1,4,1,5,1,5,4,5,115,8,5,11,5,12,5,116,1,
        5,1,5,1,5,1,5,4,5,123,8,5,11,5,12,5,124,1,5,5,5,128,8,5,10,5,12,
        5,131,9,5,1,5,5,5,134,8,5,10,5,12,5,137,9,5,1,5,4,5,140,8,5,11,5,
        12,5,141,5,5,144,8,5,10,5,12,5,147,9,5,1,5,1,5,1,5,1,5,1,5,1,5,4,
        5,155,8,5,11,5,12,5,156,1,5,1,5,4,5,161,8,5,11,5,12,5,162,3,5,165,
        8,5,1,6,1,6,1,6,1,6,1,6,3,6,172,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,3,7,186,8,7,1,8,1,8,1,8,1,8,1,8,1,9,5,9,194,
        8,9,10,9,12,9,197,9,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,
        10,208,8,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,
        16,1,16,1,16,3,16,223,8,16,1,17,1,17,5,17,227,8,17,10,17,12,17,230,
        9,17,1,18,1,18,1,19,1,19,1,20,1,20,5,20,238,8,20,10,20,12,20,241,
        9,20,1,21,1,21,1,22,1,22,5,22,247,8,22,10,22,12,22,250,9,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,8,1,0,9,12,1,0,
        23,26,1,0,27,30,1,0,31,32,1,0,33,34,1,0,35,36,1,0,42,43,1,0,37,38,
        275,0,51,1,0,0,0,2,57,1,0,0,0,4,85,1,0,0,0,6,108,1,0,0,0,8,110,1,
        0,0,0,10,164,1,0,0,0,12,171,1,0,0,0,14,185,1,0,0,0,16,187,1,0,0,
        0,18,195,1,0,0,0,20,207,1,0,0,0,22,209,1,0,0,0,24,211,1,0,0,0,26,
        213,1,0,0,0,28,215,1,0,0,0,30,217,1,0,0,0,32,222,1,0,0,0,34,224,
        1,0,0,0,36,231,1,0,0,0,38,233,1,0,0,0,40,235,1,0,0,0,42,242,1,0,
        0,0,44,244,1,0,0,0,46,253,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,
        53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,
        0,54,55,5,1,0,0,55,56,3,4,2,0,56,1,1,0,0,0,57,58,5,2,0,0,58,59,3,
        34,17,0,59,60,5,3,0,0,60,64,3,8,4,0,61,63,3,34,17,0,62,61,1,0,0,
        0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,
        1,0,0,0,67,68,5,4,0,0,68,69,5,5,0,0,69,73,3,4,2,0,70,72,5,6,0,0,
        71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,79,1,
        0,0,0,75,73,1,0,0,0,76,78,3,14,7,0,77,76,1,0,0,0,78,81,1,0,0,0,79,
        77,1,0,0,0,79,80,1,0,0,0,80,3,1,0,0,0,81,79,1,0,0,0,82,84,3,6,3,
        0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,91,
        1,0,0,0,87,85,1,0,0,0,88,90,3,18,9,0,89,88,1,0,0,0,90,93,1,0,0,0,
        91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,0,0,0,93,91,1,0,0,0,94,96,3,
        10,5,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,
        5,1,0,0,0,99,97,1,0,0,0,100,101,3,8,4,0,101,102,3,34,17,0,102,109,
        1,0,0,0,103,104,5,7,0,0,104,105,3,40,20,0,105,106,5,8,0,0,106,107,
        3,34,17,0,107,109,1,0,0,0,108,100,1,0,0,0,108,103,1,0,0,0,109,7,
        1,0,0,0,110,111,7,0,0,0,111,9,1,0,0,0,112,165,3,16,8,0,113,115,3,
        14,7,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,
        0,0,0,117,165,1,0,0,0,118,119,5,13,0,0,119,120,3,14,7,0,120,122,
        5,5,0,0,121,123,3,14,7,0,122,121,1,0,0,0,123,124,1,0,0,0,124,122,
        1,0,0,0,124,125,1,0,0,0,125,145,1,0,0,0,126,128,5,14,0,0,127,126,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,135,
        1,0,0,0,131,129,1,0,0,0,132,134,5,5,0,0,133,132,1,0,0,0,134,137,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,139,1,0,0,0,137,135,
        1,0,0,0,138,140,3,14,7,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,129,1,0,0,0,144,147,
        1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,165,1,0,0,0,147,145,
        1,0,0,0,148,149,5,15,0,0,149,150,3,14,7,0,150,151,5,16,0,0,151,152,
        3,14,7,0,152,154,5,5,0,0,153,155,3,14,7,0,154,153,1,0,0,0,155,156,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,165,1,0,0,0,158,165,
        5,17,0,0,159,161,3,14,7,0,160,159,1,0,0,0,161,162,1,0,0,0,162,160,
        1,0,0,0,162,163,1,0,0,0,163,165,1,0,0,0,164,112,1,0,0,0,164,114,
        1,0,0,0,164,118,1,0,0,0,164,148,1,0,0,0,164,158,1,0,0,0,164,160,
        1,0,0,0,165,11,1,0,0,0,166,172,3,34,17,0,167,172,5,18,0,0,168,172,
        5,19,0,0,169,172,5,20,0,0,170,172,5,21,0,0,171,166,1,0,0,0,171,167,
        1,0,0,0,171,168,1,0,0,0,171,169,1,0,0,0,171,170,1,0,0,0,172,13,1,
        0,0,0,173,186,3,16,8,0,174,186,3,32,16,0,175,186,3,18,9,0,176,177,
        3,34,17,0,177,178,3,20,10,0,178,179,3,32,16,0,179,186,1,0,0,0,180,
        181,5,22,0,0,181,182,3,34,17,0,182,183,5,4,0,0,183,186,1,0,0,0,184,
        186,3,34,17,0,185,173,1,0,0,0,185,174,1,0,0,0,185,175,1,0,0,0,185,
        176,1,0,0,0,185,180,1,0,0,0,185,184,1,0,0,0,186,15,1,0,0,0,187,188,
        3,12,6,0,188,189,5,3,0,0,189,190,3,14,7,0,190,191,5,4,0,0,191,17,
        1,0,0,0,192,194,3,8,4,0,193,192,1,0,0,0,194,197,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,195,1,0,0,0,198,199,
        3,34,17,0,199,200,3,30,15,0,200,201,3,32,16,0,201,19,1,0,0,0,202,
        208,3,22,11,0,203,208,3,24,12,0,204,208,3,26,13,0,205,208,3,28,14,
        0,206,208,3,30,15,0,207,202,1,0,0,0,207,203,1,0,0,0,207,204,1,0,
        0,0,207,205,1,0,0,0,207,206,1,0,0,0,208,21,1,0,0,0,209,210,7,1,0,
        0,210,23,1,0,0,0,211,212,7,2,0,0,212,25,1,0,0,0,213,214,7,3,0,0,
        214,27,1,0,0,0,215,216,7,4,0,0,216,29,1,0,0,0,217,218,7,5,0,0,218,
        31,1,0,0,0,219,223,3,38,19,0,220,223,3,42,21,0,221,223,3,44,22,0,
        222,219,1,0,0,0,222,220,1,0,0,0,222,221,1,0,0,0,223,33,1,0,0,0,224,
        228,5,42,0,0,225,227,3,36,18,0,226,225,1,0,0,0,227,230,1,0,0,0,228,
        226,1,0,0,0,228,229,1,0,0,0,229,35,1,0,0,0,230,228,1,0,0,0,231,232,
        7,6,0,0,232,37,1,0,0,0,233,234,3,40,20,0,234,39,1,0,0,0,235,239,
        5,43,0,0,236,238,5,43,0,0,237,236,1,0,0,0,238,241,1,0,0,0,239,237,
        1,0,0,0,239,240,1,0,0,0,240,41,1,0,0,0,241,239,1,0,0,0,242,243,7,
        7,0,0,243,43,1,0,0,0,244,248,5,39,0,0,245,247,5,42,0,0,246,245,1,
        0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,251,1,
        0,0,0,250,248,1,0,0,0,251,252,5,39,0,0,252,45,1,0,0,0,253,254,5,
        40,0,0,254,255,3,32,16,0,255,256,5,5,0,0,256,257,3,32,16,0,257,258,
        5,41,0,0,258,47,1,0,0,0,25,51,64,73,79,85,91,97,108,116,124,129,
        135,141,145,156,162,164,171,185,195,207,222,228,239,248
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'def'", "'('", "')'", "':'", 
                     "'return'", "'string['", "']'", "'int'", "'string'", 
                     "'bool'", "'dict'", "'if'", "'else'", "'for'", "'in'", 
                     "'break'", "'CiteAPA'", "'CiteMLA'", "'CiteCMS'", "'CiteCSE'", 
                     "'print('", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", 
                     "'<='", "'>='", "'=='", "'!='", "'and'", "'or'", "'='", 
                     "'+='", "'True'", "'False'", "'\"'", "'{'", "'}'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "' '" ]

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
                      "<INVALID>", "<INVALID>", "CHAR", "DIGIT", "NEWLINE", 
                      "SPACE" ]

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
    CHAR=42
    DIGIT=43
    NEWLINE=44
    SPACE=45

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

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


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
            self.block()
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
            self.state = 57
            self.match(ExprParser.T__1)
            self.state = 58
            self.id_()
            self.state = 59
            self.match(ExprParser.T__2)
            self.state = 60
            self.type_()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 61
                self.id_()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(ExprParser.T__3)
            self.state = 68
            self.match(ExprParser.T__4)
            self.state = 69
            self.block()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 70
                self.match(ExprParser.T__5)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14156220341760) != 0):
                self.state = 76
                self.expr()
                self.state = 81
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


        def var_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Var_assignContext)
            else:
                return self.getTypedRuleContext(ExprParser.Var_assignContext,i)


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
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.var_decl() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.var_assign() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.statement() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.type_()
                self.state = 101
                self.id_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(ExprParser.T__6)
                self.state = 104
                self.decimal_literal()
                self.state = 105
                self.match(ExprParser.T__7)
                self.state = 106
                self.id_()
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
            self.state = 110
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

        def method_call(self):
            return self.getTypedRuleContext(ExprParser.Method_callContext,0)


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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 113
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 116 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(ExprParser.T__12)
                self.state = 119
                self.expr()
                self.state = 120
                self.match(ExprParser.T__4)
                self.state = 122 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 121
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 124 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 129
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==14:
                            self.state = 126
                            self.match(ExprParser.T__13)
                            self.state = 131
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 135
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==5:
                            self.state = 132
                            self.match(ExprParser.T__4)
                            self.state = 137
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 139 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 138
                                self.expr()

                            else:
                                raise NoViableAltException(self)
                            self.state = 141 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                 
                    self.state = 147
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.match(ExprParser.T__14)
                self.state = 149
                self.expr()
                self.state = 150
                self.match(ExprParser.T__15)
                self.state = 151
                self.expr()
                self.state = 152
                self.match(ExprParser.T__4)
                self.state = 154 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 153
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 156 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(ExprParser.T__16)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 159
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 162 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.id_()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(ExprParser.T__17)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(ExprParser.T__18)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.match(ExprParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
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


        def literal(self):
            return self.getTypedRuleContext(ExprParser.LiteralContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(ExprParser.Var_assignContext,0)


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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.var_assign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.id_()
                self.state = 177
                self.operation()
                self.state = 178
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.match(ExprParser.T__21)
                self.state = 181
                self.id_()
                self.state = 182
                self.match(ExprParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 184
                self.id_()
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


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.method_name()
            self.state = 188
            self.match(ExprParser.T__2)
            self.state = 189
            self.expr()
            self.state = 190
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
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self.state = 192
                self.type_()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self.id_()
            self.state = 199
            self.assign_op()
            self.state = 200
            self.literal()
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
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.arithm_op()
                pass
            elif token in [27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.rel_op()
                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.eq_op()
                pass
            elif token in [33, 34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.cond_op()
                pass
            elif token in [35, 36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
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
            self.state = 209
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
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
            self.state = 211
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
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
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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
            self.state = 215
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
            self.state = 217
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
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.int_literal()
                pass
            elif token in [37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.bool_literal()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
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
            self.state = 224
            self.match(ExprParser.CHAR)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 225
                    self.char_num() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 231
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
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
            self.state = 233
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
            self.state = 235
            self.match(ExprParser.DIGIT)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 236
                    self.match(ExprParser.DIGIT) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 242
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
            self.state = 244
            self.match(ExprParser.T__38)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 245
                self.match(ExprParser.CHAR)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.match(ExprParser.T__38)
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
            self.state = 253
            self.match(ExprParser.T__39)
            self.state = 254
            self.literal()
            self.state = 255
            self.match(ExprParser.T__4)
            self.state = 256
            self.literal()
            self.state = 257
            self.match(ExprParser.T__40)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





