# Generated from WhileLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#program.
    def enterProgram(self, ctx:WhileLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLangParser#program.
    def exitProgram(self, ctx:WhileLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStmt.
    def enterWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStmt.
    def exitWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#condition.
    def enterCondition(self, ctx:WhileLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#condition.
    def exitCondition(self, ctx:WhileLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#simpleExpr.
    def enterSimpleExpr(self, ctx:WhileLangParser.SimpleExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#simpleExpr.
    def exitSimpleExpr(self, ctx:WhileLangParser.SimpleExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#value.
    def enterValue(self, ctx:WhileLangParser.ValueContext):
        pass

    # Exit a parse tree produced by WhileLangParser#value.
    def exitValue(self, ctx:WhileLangParser.ValueContext):
        pass


    # Enter a parse tree produced by WhileLangParser#variable.
    def enterVariable(self, ctx:WhileLangParser.VariableContext):
        pass

    # Exit a parse tree produced by WhileLangParser#variable.
    def exitVariable(self, ctx:WhileLangParser.VariableContext):
        pass


    # Enter a parse tree produced by WhileLangParser#body.
    def enterBody(self, ctx:WhileLangParser.BodyContext):
        pass

    # Exit a parse tree produced by WhileLangParser#body.
    def exitBody(self, ctx:WhileLangParser.BodyContext):
        pass


    # Enter a parse tree produced by WhileLangParser#incStmt.
    def enterIncStmt(self, ctx:WhileLangParser.IncStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#incStmt.
    def exitIncStmt(self, ctx:WhileLangParser.IncStmtContext):
        pass



del WhileLangParser