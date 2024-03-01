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
        4,1,43,243,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,1,1,
        1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,1,5,1,76,8,1,10,1,12,1,79,9,1,
        1,2,4,2,82,8,2,11,2,12,2,83,1,2,4,2,87,8,2,11,2,12,2,88,3,2,91,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,101,8,3,1,4,1,4,1,5,1,5,4,
        5,107,8,5,11,5,12,5,108,1,5,1,5,1,5,1,5,4,5,115,8,5,11,5,12,5,116,
        1,5,5,5,120,8,5,10,5,12,5,123,9,5,1,5,5,5,126,8,5,10,5,12,5,129,
        9,5,1,5,4,5,132,8,5,11,5,12,5,133,1,5,1,5,1,5,1,5,1,5,1,5,4,5,142,
        8,5,11,5,12,5,143,1,5,1,5,4,5,148,8,5,11,5,12,5,149,3,5,152,8,5,
        1,6,1,6,1,6,5,6,157,8,6,10,6,12,6,160,9,6,1,6,1,6,1,6,1,7,1,7,1,
        8,1,8,1,8,5,8,170,8,8,10,8,12,8,173,9,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,184,8,8,1,9,1,9,1,9,1,9,1,9,3,9,191,8,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,3,15,206,
        8,15,1,16,1,16,5,16,210,8,16,10,16,12,16,213,9,16,1,17,1,17,1,18,
        1,18,1,19,1,19,5,19,221,8,19,10,19,12,19,224,9,19,1,20,1,20,1,21,
        1,21,5,21,230,8,21,10,21,12,21,233,9,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,0,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,0,8,1,0,9,12,1,0,21,24,1,0,25,28,1,0,
        29,30,1,0,31,32,1,0,33,34,1,0,40,41,1,0,35,36,253,0,49,1,0,0,0,2,
        55,1,0,0,0,4,90,1,0,0,0,6,100,1,0,0,0,8,102,1,0,0,0,10,151,1,0,0,
        0,12,153,1,0,0,0,14,164,1,0,0,0,16,183,1,0,0,0,18,190,1,0,0,0,20,
        192,1,0,0,0,22,194,1,0,0,0,24,196,1,0,0,0,26,198,1,0,0,0,28,200,
        1,0,0,0,30,205,1,0,0,0,32,207,1,0,0,0,34,214,1,0,0,0,36,216,1,0,
        0,0,38,218,1,0,0,0,40,225,1,0,0,0,42,227,1,0,0,0,44,236,1,0,0,0,
        46,48,3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,1,0,0,53,54,3,4,2,0,54,
        1,1,0,0,0,55,56,5,2,0,0,56,57,3,32,16,0,57,58,5,3,0,0,58,62,3,8,
        4,0,59,61,3,32,16,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,4,0,0,66,67,5,5,0,
        0,67,71,3,4,2,0,68,70,5,6,0,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,
        1,0,0,0,71,72,1,0,0,0,72,77,1,0,0,0,73,71,1,0,0,0,74,76,3,16,8,0,
        75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,3,1,0,
        0,0,79,77,1,0,0,0,80,82,3,6,3,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,91,1,0,0,0,85,87,3,10,5,0,86,85,1,0,0,0,
        87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,81,1,
        0,0,0,90,86,1,0,0,0,91,5,1,0,0,0,92,93,3,8,4,0,93,94,3,32,16,0,94,
        101,1,0,0,0,95,96,5,7,0,0,96,97,3,38,19,0,97,98,5,8,0,0,98,99,3,
        32,16,0,99,101,1,0,0,0,100,92,1,0,0,0,100,95,1,0,0,0,101,7,1,0,0,
        0,102,103,7,0,0,0,103,9,1,0,0,0,104,152,3,12,6,0,105,107,3,16,8,
        0,106,105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,
        0,109,152,1,0,0,0,110,111,5,13,0,0,111,112,3,16,8,0,112,114,5,5,
        0,0,113,115,3,16,8,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,
        0,0,116,117,1,0,0,0,117,121,1,0,0,0,118,120,5,14,0,0,119,118,1,0,
        0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,127,1,0,
        0,0,123,121,1,0,0,0,124,126,5,5,0,0,125,124,1,0,0,0,126,129,1,0,
        0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,131,1,0,0,0,129,127,1,0,
        0,0,130,132,3,16,8,0,131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,
        0,0,133,134,1,0,0,0,134,152,1,0,0,0,135,136,5,15,0,0,136,137,3,32,
        16,0,137,138,5,16,0,0,138,139,3,16,8,0,139,141,5,5,0,0,140,142,3,
        16,8,0,141,140,1,0,0,0,142,143,1,0,0,0,143,141,1,0,0,0,143,144,1,
        0,0,0,144,152,1,0,0,0,145,152,5,17,0,0,146,148,3,16,8,0,147,146,
        1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,152,
        1,0,0,0,151,104,1,0,0,0,151,106,1,0,0,0,151,110,1,0,0,0,151,135,
        1,0,0,0,151,145,1,0,0,0,151,147,1,0,0,0,152,11,1,0,0,0,153,154,3,
        14,7,0,154,158,5,18,0,0,155,157,3,16,8,0,156,155,1,0,0,0,157,160,
        1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,161,1,0,0,0,160,158,
        1,0,0,0,161,162,5,19,0,0,162,163,5,4,0,0,163,13,1,0,0,0,164,165,
        3,32,16,0,165,15,1,0,0,0,166,184,3,12,6,0,167,184,3,30,15,0,168,
        170,3,8,4,0,169,168,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,
        172,1,0,0,0,172,174,1,0,0,0,173,171,1,0,0,0,174,175,3,30,15,0,175,
        176,3,28,14,0,176,177,3,30,15,0,177,184,1,0,0,0,178,179,5,20,0,0,
        179,180,5,3,0,0,180,181,3,16,8,0,181,182,5,4,0,0,182,184,1,0,0,0,
        183,166,1,0,0,0,183,167,1,0,0,0,183,171,1,0,0,0,183,178,1,0,0,0,
        184,17,1,0,0,0,185,191,3,20,10,0,186,191,3,22,11,0,187,191,3,24,
        12,0,188,191,3,26,13,0,189,191,3,28,14,0,190,185,1,0,0,0,190,186,
        1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,0,190,189,1,0,0,0,191,19,1,
        0,0,0,192,193,7,1,0,0,193,21,1,0,0,0,194,195,7,2,0,0,195,23,1,0,
        0,0,196,197,7,3,0,0,197,25,1,0,0,0,198,199,7,4,0,0,199,27,1,0,0,
        0,200,201,7,5,0,0,201,29,1,0,0,0,202,206,3,36,18,0,203,206,3,40,
        20,0,204,206,3,42,21,0,205,202,1,0,0,0,205,203,1,0,0,0,205,204,1,
        0,0,0,206,31,1,0,0,0,207,211,5,40,0,0,208,210,3,34,17,0,209,208,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,33,1,
        0,0,0,213,211,1,0,0,0,214,215,7,6,0,0,215,35,1,0,0,0,216,217,3,38,
        19,0,217,37,1,0,0,0,218,222,5,41,0,0,219,221,5,41,0,0,220,219,1,
        0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,39,1,0,
        0,0,224,222,1,0,0,0,225,226,7,7,0,0,226,41,1,0,0,0,227,231,5,37,
        0,0,228,230,5,40,0,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,1,0,
        0,0,231,232,1,0,0,0,232,234,1,0,0,0,233,231,1,0,0,0,234,235,5,37,
        0,0,235,43,1,0,0,0,236,237,5,38,0,0,237,238,3,30,15,0,238,239,5,
        5,0,0,239,240,3,30,15,0,240,241,5,39,0,0,241,45,1,0,0,0,24,49,62,
        71,77,83,88,90,100,108,116,121,127,133,143,149,151,158,171,183,190,
        205,211,222,231
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'def'", "'('", "')'", "':'", 
                     "'return'", "'string['", "']'", "'int'", "'string'", 
                     "'bool'", "'dict'", "'if'", "'else'", "'for'", "'in'", 
                     "'break'", "'()'", "','", "'print'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "'and'", "'or'", "'='", "'+='", "'True'", "'False'", 
                     "'\"'", "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
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
                      "CHAR", "DIGIT", "NEWLINE", "SPACE" ]

    RULE_program = 0
    RULE_method_decl = 1
    RULE_block = 2
    RULE_var_decl = 3
    RULE_type = 4
    RULE_statement = 5
    RULE_method_call = 6
    RULE_method_name = 7
    RULE_expr = 8
    RULE_operation = 9
    RULE_arithm_op = 10
    RULE_rel_op = 11
    RULE_eq_op = 12
    RULE_cond_op = 13
    RULE_assign_op = 14
    RULE_literal = 15
    RULE_id = 16
    RULE_char_num = 17
    RULE_int_literal = 18
    RULE_decimal_literal = 19
    RULE_bool_literal = 20
    RULE_string_literal = 21
    RULE_dict = 22

    ruleNames =  [ "program", "method_decl", "block", "var_decl", "type", 
                   "statement", "method_call", "method_name", "expr", "operation", 
                   "arithm_op", "rel_op", "eq_op", "cond_op", "assign_op", 
                   "literal", "id", "char_num", "int_literal", "decimal_literal", 
                   "bool_literal", "string_literal", "dict" ]

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
    CHAR=40
    DIGIT=41
    NEWLINE=42
    SPACE=43

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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 46
                self.method_decl()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(ExprParser.T__0)
            self.state = 53
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
            self.state = 55
            self.match(ExprParser.T__1)
            self.state = 56
            self.id_()
            self.state = 57
            self.match(ExprParser.T__2)
            self.state = 58
            self.type_()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 59
                self.id_()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(ExprParser.T__3)
            self.state = 66
            self.match(ExprParser.T__4)
            self.state = 67
            self.block()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 68
                self.match(ExprParser.T__5)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3539054108160) != 0):
                self.state = 74
                self.expr()
                self.state = 79
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
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 80
                        self.var_decl()

                    else:
                        raise NoViableAltException(self)
                    self.state = 83 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 85
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 88 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass


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
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.type_()
                self.state = 93
                self.id_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(ExprParser.T__6)
                self.state = 96
                self.decimal_literal()
                self.state = 97
                self.match(ExprParser.T__7)
                self.state = 98
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
            self.state = 102
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


        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 105
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(ExprParser.T__12)
                self.state = 111
                self.expr()
                self.state = 112
                self.match(ExprParser.T__4)
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
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 118
                    self.match(ExprParser.T__13)
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 124
                    self.match(ExprParser.T__4)
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 130
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 133 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(ExprParser.T__14)
                self.state = 136
                self.id_()
                self.state = 137
                self.match(ExprParser.T__15)
                self.state = 138
                self.expr()
                self.state = 139
                self.match(ExprParser.T__4)
                self.state = 141 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 140
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 143 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.match(ExprParser.T__16)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 147 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 146
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 149 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.method_name()
            self.state = 154
            self.match(ExprParser.T__17)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3539054108160) != 0):
                self.state = 155
                self.expr()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(ExprParser.T__18)
            self.state = 162
            self.match(ExprParser.T__3)
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
        self.enterRule(localctx, 14, self.RULE_method_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.id_()
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


        def assign_op(self):
            return self.getTypedRuleContext(ExprParser.Assign_opContext,0)


        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TypeContext)
            else:
                return self.getTypedRuleContext(ExprParser.TypeContext,i)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


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
        self.enterRule(localctx, 16, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                    self.state = 168
                    self.type_()
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 174
                self.literal()
                self.state = 175
                self.assign_op()
                self.state = 176
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(ExprParser.T__19)
                self.state = 179
                self.match(ExprParser.T__2)
                self.state = 180
                self.expr()
                self.state = 181
                self.match(ExprParser.T__3)
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
        self.enterRule(localctx, 18, self.RULE_operation)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.arithm_op()
                pass
            elif token in [25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.rel_op()
                pass
            elif token in [29, 30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.eq_op()
                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.cond_op()
                pass
            elif token in [33, 34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
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
        self.enterRule(localctx, 20, self.RULE_arithm_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 24, self.RULE_eq_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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
        self.enterRule(localctx, 26, self.RULE_cond_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 28, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
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
        self.enterRule(localctx, 30, self.RULE_literal)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.int_literal()
                pass
            elif token in [35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.bool_literal()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
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
        self.enterRule(localctx, 32, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ExprParser.CHAR)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    self.char_num() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_char_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
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
        self.enterRule(localctx, 36, self.RULE_int_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
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
        self.enterRule(localctx, 38, self.RULE_decimal_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ExprParser.DIGIT)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 219
                    self.match(ExprParser.DIGIT) 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
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
        self.enterRule(localctx, 42, self.RULE_string_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(ExprParser.T__36)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 228
                self.match(ExprParser.CHAR)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.match(ExprParser.T__36)
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
        self.enterRule(localctx, 44, self.RULE_dict)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ExprParser.T__37)
            self.state = 237
            self.literal()
            self.state = 238
            self.match(ExprParser.T__4)
            self.state = 239
            self.literal()
            self.state = 240
            self.match(ExprParser.T__38)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





