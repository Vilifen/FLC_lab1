from antlr4 import *
from .WhileLoopLexer import WhileLoopLexer
from .WhileLoopParser import WhileLoopParser
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            "lexeme": offendingSymbol.text if offendingSymbol else "",
            "line": line,
            "col": column,
            "msg": msg
        })


def run_antlr_analysis(text):
    input_stream = InputStream(text)
    lexer = WhileLoopLexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = WhileLoopParser(stream)

    error_listener = MyErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    tokens_data = []
    stream.fill()

    for token in stream.tokens:
        if token.type != Token.EOF:
            t_type = token.type

            if t_type < len(lexer.symbolicNames):
                type_name = lexer.symbolicNames[t_type]
            else:
                type_name = f"TOKEN_{t_type}"

            tokens_data.append({
                "code": t_type,
                "type": type_name,
                "lexeme": token.text,
                "line": token.line,
                "col": token.column
            })

    return tokens_data, error_listener.errors