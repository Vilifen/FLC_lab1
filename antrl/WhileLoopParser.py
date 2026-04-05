# Generated from WhileLoop.g4 by ANTLR 4.13.2
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
        4,1,19,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,9,
        2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,5,6,52,8,6,10,6,12,6,55,9,
        6,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,3,1,0,7,8,1,0,9,
        14,1,0,15,16,55,0,19,1,0,0,0,2,24,1,0,0,0,4,33,1,0,0,0,6,42,1,0,
        0,0,8,46,1,0,0,0,10,48,1,0,0,0,12,53,1,0,0,0,14,56,1,0,0,0,16,18,
        3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,
        20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,1,
        0,0,25,26,5,2,0,0,26,27,3,4,2,0,27,28,5,3,0,0,28,29,5,4,0,0,29,30,
        3,12,6,0,30,31,5,5,0,0,31,32,5,6,0,0,32,3,1,0,0,0,33,39,3,6,3,0,
        34,35,3,8,4,0,35,36,3,6,3,0,36,38,1,0,0,0,37,34,1,0,0,0,38,41,1,
        0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,5,1,0,0,0,41,39,1,0,0,0,42,
        43,5,17,0,0,43,44,3,10,5,0,44,45,5,18,0,0,45,7,1,0,0,0,46,47,7,0,
        0,0,47,9,1,0,0,0,48,49,7,1,0,0,49,11,1,0,0,0,50,52,3,14,7,0,51,50,
        1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,13,1,0,0,0,
        55,53,1,0,0,0,56,57,5,17,0,0,57,58,7,2,0,0,58,59,5,6,0,0,59,15,1,
        0,0,0,3,19,39,53
    ]

class WhileLoopParser ( Parser ):

    grammarFileName = "WhileLoop.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'('", "')'", "'{'", "'}'", 
                     "';'", "'||'", "'&&'", "'<'", "'>'", "'=='", "'>='", 
                     "'<='", "'!='", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_whileStatement = 1
    RULE_condition = 2
    RULE_comparison = 3
    RULE_logicalOp = 4
    RULE_comparisonOp = 5
    RULE_body = 6
    RULE_instruction = 7

    ruleNames =  [ "program", "whileStatement", "condition", "comparison", 
                   "logicalOp", "comparisonOp", "body", "instruction" ]

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
    ID=17
    NUMBER=18
    WS=19

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

        def EOF(self):
            return self.getToken(WhileLoopParser.EOF, 0)

        def whileStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.WhileStatementContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.WhileStatementContext,i)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = WhileLoopParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 16
                self.whileStatement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(WhileLoopParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(WhileLoopParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(WhileLoopParser.BodyContext,0)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = WhileLoopParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(WhileLoopParser.T__0)
            self.state = 25
            self.match(WhileLoopParser.T__1)
            self.state = 26
            self.condition()
            self.state = 27
            self.match(WhileLoopParser.T__2)
            self.state = 28
            self.match(WhileLoopParser.T__3)
            self.state = 29
            self.body()
            self.state = 30
            self.match(WhileLoopParser.T__4)
            self.state = 31
            self.match(WhileLoopParser.T__5)
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

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.ComparisonContext,i)


        def logicalOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.LogicalOpContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.LogicalOpContext,i)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = WhileLoopParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.comparison()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 34
                self.logicalOp()
                self.state = 35
                self.comparison()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLoopParser.ID, 0)

        def comparisonOp(self):
            return self.getTypedRuleContext(WhileLoopParser.ComparisonOpContext,0)


        def NUMBER(self):
            return self.getToken(WhileLoopParser.NUMBER, 0)

        def getRuleIndex(self):
            return WhileLoopParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = WhileLoopParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(WhileLoopParser.ID)
            self.state = 43
            self.comparisonOp()
            self.state = 44
            self.match(WhileLoopParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLoopParser.RULE_logicalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOp" ):
                listener.enterLogicalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOp" ):
                listener.exitLogicalOp(self)




    def logicalOp(self):

        localctx = WhileLoopParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_logicalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLoopParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = WhileLoopParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.InstructionContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.InstructionContext,i)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = WhileLoopParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 50
                self.instruction()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLoopParser.ID, 0)

        def getRuleIndex(self):
            return WhileLoopParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = WhileLoopParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(WhileLoopParser.ID)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self.match(WhileLoopParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





