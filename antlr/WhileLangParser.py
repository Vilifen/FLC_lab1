# Generated from WhileLang.g4 by ANTLR 4.13.2
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
        4,1,12,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,37,8,4,1,5,1,5,1,6,4,6,42,8,6,11,6,
        12,6,43,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,43,0,16,
        1,0,0,0,2,19,1,0,0,0,4,28,1,0,0,0,6,30,1,0,0,0,8,36,1,0,0,0,10,38,
        1,0,0,0,12,41,1,0,0,0,14,45,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,
        18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,4,0,0,21,22,3,4,2,0,22,23,5,5,
        0,0,23,24,5,6,0,0,24,25,3,12,6,0,25,26,5,7,0,0,26,27,5,8,0,0,27,
        3,1,0,0,0,28,29,3,6,3,0,29,5,1,0,0,0,30,31,3,10,5,0,31,32,5,3,0,
        0,32,33,3,8,4,0,33,7,1,0,0,0,34,37,3,10,5,0,35,37,5,10,0,0,36,34,
        1,0,0,0,36,35,1,0,0,0,37,9,1,0,0,0,38,39,5,9,0,0,39,11,1,0,0,0,40,
        42,3,14,7,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,
        0,0,44,13,1,0,0,0,45,46,5,9,0,0,46,47,5,2,0,0,47,48,5,8,0,0,48,15,
        1,0,0,0,2,36,43
    ]

class WhileLangParser ( Parser ):

    grammarFileName = "WhileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "WHILE", "INC_OP", "REL_OP", "LPAR", 
                      "RPAR", "LBRACE", "RBRACE", "SEMI", "ID", "NUMBER", 
                      "WORD", "WS" ]

    RULE_program = 0
    RULE_whileStmt = 1
    RULE_condition = 2
    RULE_simpleExpr = 3
    RULE_value = 4
    RULE_variable = 5
    RULE_body = 6
    RULE_incStmt = 7

    ruleNames =  [ "program", "whileStmt", "condition", "simpleExpr", "value", 
                   "variable", "body", "incStmt" ]

    EOF = Token.EOF
    WHILE=1
    INC_OP=2
    REL_OP=3
    LPAR=4
    RPAR=5
    LBRACE=6
    RBRACE=7
    SEMI=8
    ID=9
    NUMBER=10
    WORD=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whileStmt(self):
            return self.getTypedRuleContext(WhileLangParser.WhileStmtContext,0)


        def EOF(self):
            return self.getToken(WhileLangParser.EOF, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = WhileLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.whileStmt()
            self.state = 17
            self.match(WhileLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(WhileLangParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(WhileLangParser.LPAR, 0)

        def condition(self):
            return self.getTypedRuleContext(WhileLangParser.ConditionContext,0)


        def RPAR(self):
            return self.getToken(WhileLangParser.RPAR, 0)

        def LBRACE(self):
            return self.getToken(WhileLangParser.LBRACE, 0)

        def body(self):
            return self.getTypedRuleContext(WhileLangParser.BodyContext,0)


        def RBRACE(self):
            return self.getToken(WhileLangParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = WhileLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(WhileLangParser.WHILE)
            self.state = 20
            self.match(WhileLangParser.LPAR)
            self.state = 21
            self.condition()
            self.state = 22
            self.match(WhileLangParser.RPAR)
            self.state = 23
            self.match(WhileLangParser.LBRACE)
            self.state = 24
            self.body()
            self.state = 25
            self.match(WhileLangParser.RBRACE)
            self.state = 26
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleExpr(self):
            return self.getTypedRuleContext(WhileLangParser.SimpleExprContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = WhileLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.simpleExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(WhileLangParser.VariableContext,0)


        def REL_OP(self):
            return self.getToken(WhileLangParser.REL_OP, 0)

        def value(self):
            return self.getTypedRuleContext(WhileLangParser.ValueContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_simpleExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpr" ):
                listener.enterSimpleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpr" ):
                listener.exitSimpleExpr(self)




    def simpleExpr(self):

        localctx = WhileLangParser.SimpleExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simpleExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.variable()
            self.state = 31
            self.match(WhileLangParser.REL_OP)
            self.state = 32
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(WhileLangParser.VariableContext,0)


        def NUMBER(self):
            return self.getToken(WhileLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = WhileLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.variable()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(WhileLangParser.NUMBER)
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


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = WhileLangParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(WhileLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def incStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.IncStmtContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.IncStmtContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = WhileLangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.incStmt()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def INC_OP(self):
            return self.getToken(WhileLangParser.INC_OP, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_incStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncStmt" ):
                listener.enterIncStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncStmt" ):
                listener.exitIncStmt(self)




    def incStmt(self):

        localctx = WhileLangParser.IncStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_incStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(WhileLangParser.ID)
            self.state = 46
            self.match(WhileLangParser.INC_OP)
            self.state = 47
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





