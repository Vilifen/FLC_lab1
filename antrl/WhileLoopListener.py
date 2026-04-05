# Generated from WhileLoop.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileLoopParser import WhileLoopParser
else:
    from WhileLoopParser import WhileLoopParser

# This class defines a complete listener for a parse tree produced by WhileLoopParser.
class WhileLoopListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLoopParser#program.
    def enterProgram(self, ctx:WhileLoopParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#program.
    def exitProgram(self, ctx:WhileLoopParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#whileStatement.
    def enterWhileStatement(self, ctx:WhileLoopParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#whileStatement.
    def exitWhileStatement(self, ctx:WhileLoopParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#condition.
    def enterCondition(self, ctx:WhileLoopParser.ConditionContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#condition.
    def exitCondition(self, ctx:WhileLoopParser.ConditionContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#comparison.
    def enterComparison(self, ctx:WhileLoopParser.ComparisonContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#comparison.
    def exitComparison(self, ctx:WhileLoopParser.ComparisonContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#logicalOp.
    def enterLogicalOp(self, ctx:WhileLoopParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#logicalOp.
    def exitLogicalOp(self, ctx:WhileLoopParser.LogicalOpContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#comparisonOp.
    def enterComparisonOp(self, ctx:WhileLoopParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#comparisonOp.
    def exitComparisonOp(self, ctx:WhileLoopParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#body.
    def enterBody(self, ctx:WhileLoopParser.BodyContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#body.
    def exitBody(self, ctx:WhileLoopParser.BodyContext):
        pass


    # Enter a parse tree produced by WhileLoopParser#instruction.
    def enterInstruction(self, ctx:WhileLoopParser.InstructionContext):
        pass

    # Exit a parse tree produced by WhileLoopParser#instruction.
    def exitInstruction(self, ctx:WhileLoopParser.InstructionContext):
        pass



del WhileLoopParser